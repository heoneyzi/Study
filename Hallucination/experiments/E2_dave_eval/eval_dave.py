# Copyright (2025) Tsinghua University, Bytedance Ltd. and/or its affiliates
# Licensed under the Apache License, Version 2.0
#
# Run video-SALMONN2_plus on the DAVE benchmark across all 7 tasks.
# Place this file inside a clone of video-SALMONN-2 (https://github.com/bytedance/video-SALMONN-2)
# and run:
#   python eval_dave.py --split epic --max-samples 50 --cache-dir <hf-datasets-cache>
#
# Written by Jiheon Kang; model setup adapted from video_SALMONN2_plus/inference.py (Apache-2.0),
# prompts follow the DAVE dataset card (https://huggingface.co/datasets/gorjanradevski/dave).
# Portfolio copy: machine-specific paths were replaced by the --cache-dir / --path-remap options.

import argparse
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

# Make the bundled video_SALMONN2_plus package importable.
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
# Model setup (mirrors video_SALMONN2_plus/inference.py)
# ---------------------------------------------------------------------------

def apply_liger_kernel_to_qwen2_5_vl(
    rope: bool = True,
    rms_norm: bool = True,
    swiglu: bool = True,
) -> None:
    from qwenvl.model import modeling_qwen2_5_vl
    if rope:
        modeling_qwen2_5_vl.apply_multimodal_rotary_pos_emb = liger_multimodal_rotary_pos_emb
    if rms_norm:
        modeling_qwen2_5_vl.Qwen2RMSNorm = LigerRMSNorm
    if swiglu:
        modeling_qwen2_5_vl.Qwen2MLP = LigerSwiGLUMLP


def prepare_inputs(inputs: Dict[str, Any]) -> Dict[str, torch.Tensor]:
    for k in ("video", "image", "prompt", "ref", "audio", "use_audio", "should_use"):
        inputs.pop(k, None)
    device = f"cuda:{torch.cuda.current_device()}"
    return {k: v.to(device) for k, v in inputs.items() if isinstance(v, torch.Tensor)}


def build_data_args(model_path: str) -> DataArguments:
    data_args = DataArguments()
    data_args.video_max_frames = 768
    data_args.video_min_frames = 16
    data_args.base_interval = 0.1
    data_args.max_pixels = 61250
    data_args.video_max_frame_pixels = 61250
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
# Prompt builders — one per DAVE task. Mirrors dave_data.py.
# ---------------------------------------------------------------------------

LETTERS = ["A", "B", "C", "D", "E"]


def fmt_choices(options: List[str]) -> str:
    return "\n".join(f"({LETTERS[i]}) {opt}" for i, opt in enumerate(options))


def build_prompt(task: str, sample: Dict[str, Any]) -> str:
    sound_effect = sample["audio_class"]
    meta = sample["choice_metadata"][task]
    options = meta["choices"]

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


# Which media each task consumes. video-SALMONN-2 always takes a video file;
# use_audio=True asks the model to also ingest its soundtrack.
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
    if not m:
        return None
    return LETTERS.index(m.group(1).upper())


def parse_order(text: str) -> List[str]:
    return [f"({c.upper()})" for c in ORDER_RE.findall(text)][:4]


def score(task: str, prediction: str, meta: Dict[str, Any]) -> Optional[bool]:
    gt = meta.get("ground_truth")
    
    # 1. 정답(gt)이 데이터셋에 아예 없는(None) 경우 채점을 건너뜀 (에러 방지)
    if gt is None:
        return None

    if task == "temporal_ordering":
        pred_order = parse_order(prediction)
        return pred_order == list(gt) if len(pred_order) == 4 else False
        
    if task == "action_recognition":
        pred_idx = parse_letter(prediction)
        # 2. 정답이 리스트 형태일 때와 단순 정수일 때를 모두 안전하게 처리
        if isinstance(gt, (list, tuple, str)):
            return pred_idx is not None and pred_idx == gt[0]
        else:
            return pred_idx is not None and pred_idx == gt
            
    pred_idx = parse_letter(prediction)
    return pred_idx is not None and pred_idx == gt


# ---------------------------------------------------------------------------
# Inference loop
# ---------------------------------------------------------------------------

def run_one(model, tokenizer, test_data, video_path: str, use_audio: bool,
            prompt: str, max_new_tokens: int) -> str:
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
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    trimmed = outputs[0, len(inputs["input_ids"][0]):]
    return tokenizer.decode(trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", default="tsinghua-ee/video-SALMONN2_plus_3B_full")
    parser.add_argument("--split", default="epic", choices=["epic", "ego4d"])
    parser.add_argument("--cache-dir", default=None,
                        help="HF datasets cache directory holding the DAVE dataset.")
    parser.add_argument("--path-remap", nargs=2, default=None, metavar=("OLD_PREFIX", "NEW_PREFIX"),
                        help="Rewrite the video-path prefix stored in cached DAVE rows "
                             "(needed when the cache was built on another machine).")
    parser.add_argument("--max-samples", type=int, default=50,
                        help="Number of DAVE samples to evaluate. Use -1 for all.")
    parser.add_argument("--tasks", nargs="+", default=TASKS,
                        help="Subset of DAVE tasks to evaluate.")
    parser.add_argument("--output", default="dave_results.json")
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
    print(f"Loading model {args.model_path} ...")
    model = video_SALMONN2_plus.from_pretrained(
        args.model_path,
        attn_implementation="flash_attention_2",
        torch_dtype=torch.bfloat16,
        device_map="cpu",
    )
    model.cuda()
    model.eval()

    data_module = make_supervised_data_module(tokenizer=tokenizer, data_args=data_args)
    test_data = data_module["train_dataset"]

    per_sample: List[Dict[str, Any]] = []
    correct = {t: 0 for t in args.tasks}
    total = {t: 0 for t in args.tasks}

    t0 = time.time()
    for sample in tqdm(dataset, desc="DAVE"):
        sample_log: Dict[str, Any] = {"audio_class": sample["audio_class"], "tasks": {}}
        for task in args.tasks:
            if task not in sample["choice_metadata"]:
                continue
            video_key, use_audio = TASK_MEDIA[task]
            video_path = sample[video_key]
            if args.path_remap:
                video_path = video_path.replace(*args.path_remap)
            # -------------------------------------------------------------
            prompt = build_prompt(task, sample)
            try:
                pred = run_one(model, tokenizer, test_data, video_path, use_audio,
                               prompt, args.max_new_tokens)
            except Exception as e:
                pred = f"<ERROR: {type(e).__name__}: {e}>"
            ok = score(task, pred, sample["choice_metadata"][task]) if not pred.startswith("<ERROR") else None
            sample_log["tasks"][task] = {
                "prompt": prompt,
                "prediction": pred,
                "ground_truth": sample["choice_metadata"][task]["ground_truth"],
                "correct": ok,
            }
            if ok is not None:
                total[task] += 1
                if ok:
                    correct[task] += 1
        per_sample.append(sample_log)

    accuracy = {t: (correct[t] / total[t] if total[t] else None) for t in args.tasks}
    elapsed = time.time() - t0

    results = {
        "model_path": args.model_path,
        "split": args.split,
        "num_samples": len(dataset),
        "seed": args.seed,
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "elapsed_sec": elapsed,
        "per_sample": per_sample,
    }
    out_path = Path(args.output)
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    print("\n=== DAVE results ===")
    for t in args.tasks:
        acc = accuracy[t]
        print(f"  {t:<24s}  acc = {acc:.4f}  ({correct[t]}/{total[t]})" if acc is not None
              else f"  {t:<24s}  acc = N/A")
    print(f"Elapsed: {elapsed:.1f}s — saved {out_path.resolve()}")


if __name__ == "__main__":
    main()
