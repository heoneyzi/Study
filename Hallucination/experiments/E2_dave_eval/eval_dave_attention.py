# Copyright (2025) Tsinghua University, Bytedance Ltd. and/or its affiliates
# Licensed under the Apache License, Version 2.0
#
# Per-task attention analysis for the DAVE benchmark on video-SALMONN-2.
#
#   - DAVE loading / task prompts / scoring     : adapted from eval_dave.py
#   - attention extraction (last layer, per modality top-10)
#                                                : adapted from the AVHBench attention script
#                                                  (../E1_avhbench_attention/avhbench_attention_log.py)
#
# Output layout (one folder per sample, one subfolder per task):
#
#   <output_dir>/<idx>_<audio_class>/<task>/main_result_with_log.json
#   <output_dir>/<idx>_<audio_class>/<task>/video_total10_attention_log.json
#   <output_dir>/<idx>_<audio_class>/<task>/video_individual10_attention_log.json
#   <output_dir>/<idx>_<audio_class>/<task>/audio_total10_attention_log.json       (only when use_audio=True)
#   <output_dir>/<idx>_<audio_class>/<task>/audio_individual10_attention_log.json
#   <output_dir>/<idx>_<audio_class>/<task>/text_total10_attention_log.json
#   <output_dir>/<idx>_<audio_class>/<task>/text_individual10_attention_log.json
#
# Plus a top-level <output_dir>/summary.json with per-task accuracy.
#
# Place inside a clone of video-SALMONN-2 (https://github.com/bytedance/video-SALMONN-2) and run e.g.:
#     python eval_dave_attention.py --split epic --max-samples 50 --cache-dir <hf-datasets-cache>
#
# Written by Jiheon Kang. Portfolio copy: machine-specific default paths were removed.

import argparse
import gc
import json
import os
import random
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch
from tqdm import tqdm

project_root = Path(__file__).parent / "video_SALMONN2_plus"
sys.path.insert(0, str(project_root))

from qwenvl.model.modeling_qwen2_5_vl import video_SALMONN2_plus  # noqa: E402
from qwenvl.data.dataset import make_supervised_data_module  # noqa: E402
from qwenvl.data.image_processing_qwen2_vl_fast import Qwen2VLImageProcessorFast  # noqa: E402
from qwenvl.train.argument import DataArguments  # noqa: E402
from transformers import AutoTokenizer, WhisperFeatureExtractor  # noqa: E402

from liger_kernel.transformers.qwen2vl_mrope import liger_multimodal_rotary_pos_emb  # noqa: E402
from liger_kernel.transformers.rms_norm import LigerRMSNorm  # noqa: E402
from liger_kernel.transformers.swiglu import LigerSwiGLUMLP  # noqa: E402

from datasets import load_dataset  # noqa: E402


# ---------------------------------------------------------------------------
# Model / data setup
# ---------------------------------------------------------------------------

def apply_liger_kernel_to_qwen2_5_vl() -> None:
    from qwenvl.model import modeling_qwen2_5_vl
    modeling_qwen2_5_vl.apply_multimodal_rotary_pos_emb = liger_multimodal_rotary_pos_emb
    modeling_qwen2_5_vl.Qwen2RMSNorm = LigerRMSNorm
    modeling_qwen2_5_vl.Qwen2MLP = LigerSwiGLUMLP


def prepare_inputs(inputs: Dict[str, Any]) -> Dict[str, torch.Tensor]:
    for k in ("video", "image", "prompt", "ref", "audio", "use_audio", "should_use"):
        inputs.pop(k, None)
    device = f"cuda:{torch.cuda.current_device()}"
    return {k: v.to(device) for k, v in inputs.items() if isinstance(v, torch.Tensor)}


def build_data_args(model_path: str) -> DataArguments:
    # Conservative settings (mirroring the AVHBench attention script) so attention extraction
    # with attn_implementation="eager" fits in memory across all 7 DAVE tasks.
    data_args = DataArguments()
    data_args.video_max_frames = 16
    data_args.video_min_frames = 16
    data_args.base_interval = 0.1
    data_args.max_pixels = 20000
    data_args.video_max_frame_pixels = 20000
    data_args.run_test = True
    data_args.image_processor = Qwen2VLImageProcessorFast.from_pretrained(model_path)
    data_args.audio_processor = WhisperFeatureExtractor(
        feature_size=data_args.feature_size,
        sampling_rate=data_args.sampling_rate,
        hop_length=data_args.hop_length,
        chunk_length=data_args.chunk_length,
    )
    data_args.model_type = "qwen2.5vl"
    return data_args


# ---------------------------------------------------------------------------
# DAVE prompts and per-task media routing
# ---------------------------------------------------------------------------

LETTERS = ["A", "B", "C", "D", "E"]


def fmt_choices(options: List[str]) -> str:
    return "\n".join(f"({LETTERS[i]}) {opt}" for i, opt in enumerate(options))


def build_prompt(task: str, sample: Dict[str, Any]) -> str:
    sound_effect = sample["audio_class"]
    options = sample["choice_metadata"][task]["choices"]

    if task == "audio_visual_alignment":
        return (
            f"What is the person in the video doing when {sound_effect} is heard?\n\n"
            f"{fmt_choices(options)}\n\nAnswer only with the letter."
        )
    if task == "visual_only":
        return (
            "What action is happening during the highlighted segment?\n\n"
            f"{fmt_choices(options)}\n\nAnswer only with the letter."
        )
    if task == "audio_only":
        return (
            "What action is associated with the sound you hear?\n\n"
            f"{fmt_choices(options)}\n\nAnswer only with the letter."
        )
    if task == "text_only":
        event_descriptions = [event["narration"] for event in sample["events"]]
        return (
            f"Given these event descriptions: {', '.join(event_descriptions)}\n"
            f"Which action is most likely associated with the sound '{sound_effect}'?\n\n"
            f"{fmt_choices(options)}\n\nAnswer only with the letter."
        )
    if task == "temporal_ordering":
        return (
            "Order these events chronologically:\n\n"
            f"{fmt_choices(options)}\n\n"
            "Provide the correct temporal order as a list like ['(A)', '(B)', '(C)', '(D)']."
        )
    if task == "action_recognition":
        return (
            "Which action occurs during the overlayed audio segment?\n\n"
            f"{fmt_choices(options)}\n\nAnswer only with the letter."
        )
    if task == "audio_classification":
        return (
            "What sound is overlayed on the video?\n\n"
            f"{fmt_choices(options)}\n\nAnswer only with the letter."
        )
    raise ValueError(f"Unknown task: {task}")


TASK_MEDIA = {
    "audio_visual_alignment": ("video_with_overlayed_audio_path", True),
    "visual_only":            ("silent_video_path",               False),
    "audio_only":             ("video_with_overlayed_audio_path", True),
    "text_only":              ("silent_video_path",               False),
    "temporal_ordering":      ("silent_video_path",               False),
    "action_recognition":     ("video_with_overlayed_audio_path", True),
    "audio_classification":   ("video_with_overlayed_audio_path", True),
}

TASKS = list(TASK_MEDIA.keys())


# ---------------------------------------------------------------------------
# Answer parsing / scoring
# ---------------------------------------------------------------------------

LETTER_RE = re.compile(r"\(?([A-E])\)?", re.IGNORECASE)
ORDER_RE = re.compile(r"\(?([A-D])\)?", re.IGNORECASE)


def parse_letter(text: str) -> Optional[int]:
    m = LETTER_RE.search(text)
    return None if not m else LETTERS.index(m.group(1).upper())


def parse_order(text: str) -> List[str]:
    return [f"({c.upper()})" for c in ORDER_RE.findall(text)][:4]


def score(task: str, prediction: str, meta: Dict[str, Any]) -> Optional[bool]:
    gt = meta.get("ground_truth")
    if gt is None:
        return None
    if task == "temporal_ordering":
        pred_order = parse_order(prediction)
        return pred_order == list(gt) if len(pred_order) == 4 else False
    if task == "action_recognition":
        pred_idx = parse_letter(prediction)
        if isinstance(gt, (list, tuple, str)):
            return pred_idx is not None and pred_idx == gt[0]
        return pred_idx is not None and pred_idx == gt
    pred_idx = parse_letter(prediction)
    return pred_idx is not None and pred_idx == gt


# ---------------------------------------------------------------------------
# Attention helpers (carried over from the AVHBench attention script)
# ---------------------------------------------------------------------------

def get_total_top10(mod_idx, attention_history, tokens):
    if not mod_idx:
        return []
    mod_history = attention_history[:, mod_idx]
    token_sums_overall = mod_history.sum(axis=0)
    top10_relative_idx = token_sums_overall.argsort()[-10:][::-1]
    res = []
    for rank, rel_i in enumerate(top10_relative_idx):
        abs_i = mod_idx[rel_i]
        res.append({
            "rank": rank + 1,
            "absolute_index": int(abs_i),
            "token": tokens[abs_i].replace("Ġ", " "),
            "total_attention_sum": float(token_sums_overall[rel_i]),
        })
    return res


def get_individual_top10(mod_idx, attention_history, tokens, generated_tokens):
    if not mod_idx:
        return []
    mod_history = attention_history[:, mod_idx]
    res = []
    for t in range(mod_history.shape[0]):
        step_scores = mod_history[t]
        top10_relative_idx = step_scores.argsort()[-10:][::-1]
        step_top10 = [
            {
                "rank": rank + 1,
                "absolute_index": int(mod_idx[rel_i]),
                "token": tokens[mod_idx[rel_i]].replace("Ġ", " "),
                "score": float(step_scores[rel_i]),
            }
            for rank, rel_i in enumerate(top10_relative_idx)
        ]
        res.append({
            "t": t,
            "generated_token": generated_tokens[t].replace("Ġ", " "),
            "top10_tokens": step_top10,
        })
    return res


def build_attention_history(outputs, seq_len: int) -> np.ndarray:
    """Average the last-layer attention across heads at every generation step.

    Step 0 reads the attention from the *last* prefix position (the prompt's final
    token) toward the prefix; subsequent steps read from the newly-generated query
    token. This mirrors the AVHBench attention script.
    """
    num_steps = len(outputs.attentions)
    attention_history = np.zeros((num_steps, seq_len), dtype=np.float32)
    for step, token_attention in enumerate(outputs.attentions):
        last_layer_attn = token_attention[-1]
        if step == 0:
            attn_weights = last_layer_attn[0, :, -1, :seq_len]
        else:
            attn_weights = last_layer_attn[0, :, 0, :seq_len]
        attention_history[step] = attn_weights.mean(dim=0).float().cpu().numpy()
    return attention_history


def classify_token_indices(tokens: List[str]):
    video_idx = [i for i, t in enumerate(tokens) if "<|video_pad|>" in t or "<|vision_" in t]
    audio_idx = [i for i, t in enumerate(tokens) if "<|audio_pad|>" in t]
    text_idx = [i for i in range(len(tokens)) if i not in video_idx and i not in audio_idx]
    return video_idx, audio_idx, text_idx


# ---------------------------------------------------------------------------
# Per-task inference + attention extraction
# ---------------------------------------------------------------------------

def safe_name(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")[:64] or "unk"


def run_task_with_attention(
    model,
    tokenizer,
    test_data,
    video_path: str,
    use_audio: bool,
    prompt: str,
    max_new_tokens: int,
    out_dir: Path,
    task: str,
    meta: Dict[str, Any],
    sample_meta: Dict[str, Any],
) -> Dict[str, Any]:
    input_dict = {
        "video": video_path,
        "use_audio": use_audio,
        "conversations": [
            {"from": "human", "value": f"<video>\n{prompt}"},
            {"from": "gpt", "value": ""},
        ],
    }
    inputs = test_data._get_item(input_dict)
    inputs = prepare_inputs(inputs)

    input_ids = inputs["input_ids"][0]
    tokens = tokenizer.convert_ids_to_tokens(input_ids)
    seq_len = len(input_ids)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            output_attentions=True,
            return_dict_in_generate=True,
        )

    output_trimmed = outputs.sequences[0, seq_len:]
    output_text = tokenizer.decode(
        output_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    ).strip()
    generated_tokens = tokenizer.convert_ids_to_tokens(output_trimmed)

    attention_history = build_attention_history(outputs, seq_len)
    num_steps = attention_history.shape[0]

    video_idx, audio_idx, text_idx = classify_token_indices(tokens)

    video_sums = attention_history[:, video_idx].sum(axis=1) if video_idx else np.zeros(num_steps)
    audio_sums = attention_history[:, audio_idx].sum(axis=1) if audio_idx else np.zeros(num_steps)
    text_sums = attention_history[:, text_idx].sum(axis=1) if text_idx else np.zeros(num_steps)
    total_input_sums = video_sums + audio_sums + text_sums
    self_gen_sums = 1.0 - total_input_sums

    # Step-by-step modality breakdown
    attention_log, tokens_per_t = [], []
    for t in range(num_steps):
        tok_str = generated_tokens[t].replace("Ġ", " ")
        tokens_per_t.append(tok_str)
        attention_log.append({
            "t": t,
            "token": tok_str,
            "absolute_attention": {
                "total_input": float(total_input_sums[t]),
                "self_generated": float(self_gen_sums[t]),
                "video": float(video_sums[t]),
                "audio": float(audio_sums[t]),
                "text_prompt": float(text_sums[t]),
            },
        })

    # Sample-level aggregated focus (mean over the full generated answer)
    aggregated = {
        "mean_video": float(video_sums.mean()),
        "mean_audio": float(audio_sums.mean()),
        "mean_text_prompt": float(text_sums.mean()),
        "mean_self_generated": float(self_gen_sums.mean()),
        "num_video_tokens": len(video_idx),
        "num_audio_tokens": len(audio_idx),
        "num_text_tokens": len(text_idx),
    }

    pred_ok = score(task, output_text, meta)

    main_result = {
        **sample_meta,
        "task": task,
        "prompt": prompt,
        "video_path": video_path,
        "use_audio": use_audio,
        "ground_truth": meta.get("ground_truth"),
        "choices": meta.get("choices"),
        "generated_result": output_text,
        "correct": pred_ok,
        "aggregated_attention": aggregated,
        "tokens_per_t": tokens_per_t,
        "attention_log": attention_log,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "main_result_with_log.json").write_text(
        json.dumps(main_result, indent=4, ensure_ascii=False)
    )

    modalities = {"video": video_idx, "audio": audio_idx, "text": text_idx}
    for mod_name, mod_idx in modalities.items():
        if not mod_idx:
            continue
        (out_dir / f"{mod_name}_total10_attention_log.json").write_text(
            json.dumps(
                get_total_top10(mod_idx, attention_history, tokens),
                indent=4, ensure_ascii=False,
            )
        )
        (out_dir / f"{mod_name}_individual10_attention_log.json").write_text(
            json.dumps(
                get_individual_top10(mod_idx, attention_history, tokens, generated_tokens),
                indent=4, ensure_ascii=False,
            )
        )

    # Free per-task tensors before next task
    del inputs, outputs, attention_history
    torch.cuda.empty_cache()
    gc.collect()

    return {
        "prediction": output_text,
        "correct": pred_ok,
        "aggregated_attention": aggregated,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", default="tsinghua-ee/video-SALMONN2_plus_3B_full")
    parser.add_argument("--split", default="epic", choices=["epic", "ego4d"])
    parser.add_argument("--cache-dir", default=None,
                        help="HF datasets cache directory holding the DAVE dataset.")
    parser.add_argument("--video-path-local-prefix", default=None,
                        help="Prefix baked into cached DAVE samples (cache built on another machine); "
                             "remapped onto --cache-dir when both are given.")
    parser.add_argument("--max-samples", type=int, default=50)
    parser.add_argument("--tasks", nargs="+", default=TASKS)
    parser.add_argument("--output-dir", default="att_log_DAVE")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max-new-tokens", type=int, default=32)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    apply_liger_kernel_to_qwen2_5_vl()

    print(f"Loading DAVE split={args.split} from cache_dir={args.cache_dir} ...")
    dataset = load_dataset(
        "gorjanradevski/dave",
        split=args.split,
        cache_dir=args.cache_dir,
        trust_remote_code=True,
    )
    if args.max_samples > 0:
        n = min(args.max_samples, len(dataset))
        indices = random.sample(range(len(dataset)), n)
        dataset = dataset.select(indices)
    print(f"  -> {len(dataset)} samples")

    data_args = build_data_args(args.model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_path,
        model_max_length=131072,
        padding_side="right",
        use_fast=False,
    )
    print(f"Loading model {args.model_path} (eager attention for attn extraction) ...")
    model = video_SALMONN2_plus.from_pretrained(
        args.model_path,
        attn_implementation="eager",
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    model.eval()

    data_module = make_supervised_data_module(tokenizer=tokenizer, data_args=data_args)
    test_data = data_module["train_dataset"]

    out_base = Path(args.output_dir)
    out_base.mkdir(parents=True, exist_ok=True)

    correct = {t: 0 for t in args.tasks}
    total = {t: 0 for t in args.tasks}
    per_sample_index: List[Dict[str, Any]] = []

    t0 = time.time()
    for idx, sample in enumerate(tqdm(dataset, desc="DAVE-attn")):
        audio_class = sample["audio_class"]
        sample_dir = out_base / f"{idx:05d}_{safe_name(audio_class)}"
        sample_meta = {
            "sample_idx": idx,
            "audio_class": audio_class,
            "split": args.split,
        }
        sample_index_entry: Dict[str, Any] = {
            "sample_idx": idx, "audio_class": audio_class, "tasks": {}
        }

        for task in args.tasks:
            if task not in sample["choice_metadata"]:
                continue
            video_key, use_audio = TASK_MEDIA[task]
            video_path = sample[video_key]
            if args.video_path_local_prefix and args.cache_dir:
                video_path = video_path.replace(args.video_path_local_prefix, args.cache_dir)
            prompt = build_prompt(task, sample)
            task_dir = sample_dir / task
            try:
                result = run_task_with_attention(
                    model, tokenizer, test_data,
                    video_path=video_path,
                    use_audio=use_audio,
                    prompt=prompt,
                    max_new_tokens=args.max_new_tokens,
                    out_dir=task_dir,
                    task=task,
                    meta=sample["choice_metadata"][task],
                    sample_meta=sample_meta,
                )
            except Exception as e:
                err = f"<ERROR: {type(e).__name__}: {e}>"
                task_dir.mkdir(parents=True, exist_ok=True)
                (task_dir / "error.json").write_text(
                    json.dumps({**sample_meta, "task": task, "error": err}, indent=4)
                )
                sample_index_entry["tasks"][task] = {"error": err}
                torch.cuda.empty_cache(); gc.collect()
                continue

            sample_index_entry["tasks"][task] = {
                "prediction": result["prediction"],
                "correct": result["correct"],
                "use_audio": use_audio,
                "aggregated_attention": result["aggregated_attention"],
            }
            if result["correct"] is not None:
                total[task] += 1
                if result["correct"]:
                    correct[task] += 1

        per_sample_index.append(sample_index_entry)

    summary = {
        "model_path": args.model_path,
        "split": args.split,
        "num_samples": len(dataset),
        "seed": args.seed,
        "accuracy": {t: (correct[t] / total[t] if total[t] else None) for t in args.tasks},
        "correct": correct,
        "total": total,
        "elapsed_sec": time.time() - t0,
        "per_sample": per_sample_index,
    }
    (out_base / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))

    print("\n=== DAVE attention-eval summary ===")
    for t in args.tasks:
        acc = summary["accuracy"][t]
        if acc is None:
            print(f"  {t:<24s}  acc = N/A")
        else:
            print(f"  {t:<24s}  acc = {acc:.4f}  ({correct[t]}/{total[t]})")
    print(f"Attention logs written under: {out_base.resolve()}")


if __name__ == "__main__":
    main()
