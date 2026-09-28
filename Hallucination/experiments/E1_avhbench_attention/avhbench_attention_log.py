# Copyright (2025) Tsinghua University, Bytedance Ltd. and/or its affiliates
# Licensed under the Apache License, Version 2.0 (see ../LICENSE-video-SALMONN-2)
#
# AVHBench attention logging for video-SALMONN 2+ (per-modality attention of every generated token).
# Written by Jiheon Kang on top of video_SALMONN2_plus/inference.py (originally inference_demo2.py).
# Place inside video-SALMONN-2/video_SALMONN2_plus/ (it imports the local `qwenvl` package) and run:
#   python avhbench_attention_log.py --qa-json <AVHBench>/QA.json --video-dir <AVHBench>/videos
# Portfolio copy: the hard-coded server paths were replaced by the command-line options below.

import argparse
import os
import json
import logging
import torch
import gc
import sys
import numpy as np
from pathlib import Path
from tqdm import tqdm

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from qwenvl.model.modeling_qwen2_5_vl import video_SALMONN2_plus
from qwenvl.data.dataset import make_supervised_data_module
from qwenvl.data.image_processing_qwen2_vl_fast import Qwen2VLImageProcessorFast
from qwenvl.train.argument import DataArguments
from transformers import AutoTokenizer, WhisperFeatureExtractor

from liger_kernel.transformers.qwen2vl_mrope import liger_multimodal_rotary_pos_emb
from liger_kernel.transformers.rms_norm import LigerRMSNorm
from liger_kernel.transformers.swiglu import LigerSwiGLUMLP

parser = argparse.ArgumentParser(description="Log per-modality attention of video-SALMONN 2+ on AVHBench")
parser.add_argument("--qa-json", required=True, help="AVHBench QA.json (fields: video_id, task, text, label)")
parser.add_argument("--video-dir", required=True, help="folder holding <video_id>.mp4")
parser.add_argument("--output-dir", default="att_log_AVHB", help="one sub-folder per <video_id>_<task_idx>")
args = parser.parse_args()

def apply_liger_kernel_to_qwen2_5_vl():
    print("Applying Liger kernels to Qwen2.5-VL model...")
    from qwenvl.model import modeling_qwen2_5_vl
    modeling_qwen2_5_vl.apply_multimodal_rotary_pos_emb = liger_multimodal_rotary_pos_emb
    modeling_qwen2_5_vl.Qwen2RMSNorm = LigerRMSNorm
    modeling_qwen2_5_vl.Qwen2MLP = LigerSwiGLUMLP

apply_liger_kernel_to_qwen2_5_vl()

def prepare_inputs(inputs):
    inputs.pop("video", None)
    inputs.pop("image", None)
    inputs.pop("prompt", None)
    inputs.pop("ref", None)
    inputs.pop("audio", None)
    inputs.pop("use_audio", False)
    inputs.pop("should_use", True)
    inputs = {k: v.to(f"cuda:{torch.cuda.current_device()}") for k, v in inputs.items() if isinstance(v, torch.Tensor)}
    return inputs

def prepare_dataset(model_path):
    data_args = DataArguments()
    data_args.video_max_frames = 16    # OOM 방지를 위해 조정 권장
    data_args.video_min_frames = 16
    data_args.base_interval = 0.1
    data_args.max_pixels = 20000       # OOM 방지를 위해 조정 권장
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

# ==========================================
# 1. 모델 및 데이터로더 초기화
# ==========================================
model_path = "tsinghua-ee/video-SALMONN2_plus_3B_full"
data_args = prepare_dataset(model_path)

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    model_max_length=131072,
    padding_side="right",
    use_fast=False,
)

model = video_SALMONN2_plus.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    attn_implementation="eager",
    device_map="auto" 
)

data_module = make_supervised_data_module(tokenizer=tokenizer, data_args=data_args)
test_data = data_module["train_dataset"]

# ==========================================
# 2. 분석용 헬퍼 함수 정의
# ==========================================
def get_total_top10(mod_idx, attention_history, tokens):
    if not mod_idx: return []
    mod_history = attention_history[:, mod_idx] 
    token_sums_overall = mod_history.sum(axis=0) 
    top10_relative_idx = token_sums_overall.argsort()[-10:][::-1]
    
    res = []
    for rank, rel_i in enumerate(top10_relative_idx):
        abs_i = mod_idx[rel_i]
        token_str = tokens[abs_i].replace('Ġ', ' ')
        res.append({
            "rank": rank + 1,
            "absolute_index": int(abs_i),
            "token": token_str,
            "total_attention_sum": float(token_sums_overall[rel_i])
        })
    return res

def get_individual_top10(mod_idx, attention_history, tokens, generated_tokens):
    if not mod_idx: return []
    mod_history = attention_history[:, mod_idx] 
    num_steps = mod_history.shape[0]
    
    res = []
    for t in range(num_steps):
        step_scores = mod_history[t]
        top10_relative_idx = step_scores.argsort()[-10:][::-1]
        
        step_top10 = []
        for rank, rel_i in enumerate(top10_relative_idx):
            abs_i = mod_idx[rel_i]
            token_str = tokens[abs_i].replace('Ġ', ' ')
            step_top10.append({
                "rank": rank + 1,
                "absolute_index": int(abs_i),
                "token": token_str,
                "score": float(step_scores[rel_i])
            })
            
        res.append({
            "t": t,
            "generated_token": generated_tokens[t].replace('Ġ', ' '),
            "top10_tokens": step_top10
        })
    return res

# ==========================================
# 3. 데이터셋 순회 및 추론/어텐션 추출 파이프라인
# ==========================================
QA_JSON_PATH = args.qa_json
VIDEO_DIR = args.video_dir
OUTPUT_BASE_DIR = args.output_dir

with open(QA_JSON_PATH, "r", encoding="utf-8") as f:
    qa_data = json.load(f)

# 동일한 비디오 ID에 대해 몇 번째 태스크인지 카운트하기 위한 딕셔너리
video_task_counter = {}

for entry in tqdm(qa_data, desc="Processing AVHBench"):
    video_id = entry.get("video_id")
    task_name = entry.get("task", "")
    prompt_text = entry.get("text", "")
    label_text = entry.get("label", "")
    
    video_path = os.path.join(VIDEO_DIR, f"{video_id}.mp4")
    
    if not os.path.exists(video_path):
        print(f"[Warning] Video not found: {video_path}. Skipping.")
        continue

    # 태스크 인덱스 계산 (0, 1, 2...)
    if video_id not in video_task_counter:
        video_task_counter[video_id] = 0
    else:
        video_task_counter[video_id] += 1
    task_idx = video_task_counter[video_id]
    
    # 출력 폴더 생성
    output_dir = os.path.join(OUTPUT_BASE_DIR, f"{video_id}_{task_idx}")
    os.makedirs(output_dir, exist_ok=True)
    
    # 모델 입력 준비
    input_dict = {
        "video": video_path,
        "use_audio": True, 
        "conversations": [
            {
                "from": "human",
                "value": f"<video>\n{prompt_text}"
            },
            {
                "from": "gpt",
                "value": ""
            }
        ]
    }

    try:
        inputs = test_data._get_item(input_dict)
        inputs = prepare_inputs(inputs)
    except Exception as e:
        print(f"[Error] Failed to prepare inputs for {video_id}: {e}")
        continue

    input_ids = inputs["input_ids"][0]
    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    # 추론 시작
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=False,
            output_attentions=True,
            return_dict_in_generate=True
        )

    output_trimmed = outputs.sequences[0, len(input_ids):]
    output_text = tokenizer.decode(output_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)

    # ==========================================
    # 4. 어텐션 데이터 파싱 및 저장
    # ==========================================
    video_idx = [i for i, t in enumerate(tokens) if "<|video_pad|>" in t or "<|vision_" in t]
    audio_idx = [i for i, t in enumerate(tokens) if "<|audio_pad|>" in t]
    text_idx = [i for i, t in enumerate(tokens) if i not in video_idx and i not in audio_idx]

    generated_tokens = tokenizer.convert_ids_to_tokens(output_trimmed)
    num_steps = len(generated_tokens)
    seq_len = len(input_ids)

    attention_history = np.zeros((num_steps, seq_len))

    for step, token_attention in enumerate(outputs.attentions):
        last_layer_attn = token_attention[-1]
        if step == 0:
            attn_weights = last_layer_attn[0, :, -1, :seq_len]
        else:
            attn_weights = last_layer_attn[0, :, 0, :seq_len]
            
        avg_attn = attn_weights.mean(dim=0).float().cpu().numpy()
        attention_history[step] = avg_attn

    video_sums = attention_history[:, video_idx].sum(axis=1) if video_idx else np.zeros(num_steps)
    audio_sums = attention_history[:, audio_idx].sum(axis=1) if audio_idx else np.zeros(num_steps)
    text_sums = attention_history[:, text_idx].sum(axis=1) if text_idx else np.zeros(num_steps)

    total_input_sums = video_sums + audio_sums + text_sums
    generated_sums = 1.0 - total_input_sums

    # (1) attention_log.json의 내용 구축 (스텝별 정량적 합계)
    attention_log = []
    tokens_per_t = []
    for t in range(num_steps):
        token_str = generated_tokens[t].replace('Ġ', ' ')
        tokens_per_t.append(token_str)
        attention_log.append({
            "t": t,
            "token": token_str,
            "absolute_attention": {
                "total_input": float(total_input_sums[t]),
                "self_generated": float(generated_sums[t]),
                "video": float(video_sums[t]),
                "audio": float(audio_sums[t]),
                "text_prompt": float(text_sums[t])
            }
        })

    # (2) Main Result JSON 저장
    main_result = {
        "video_id": video_id,
        "task": task_name,
        "text": prompt_text,
        "label": label_text,
        "generated_result": output_text,
        "tokens_per_t": tokens_per_t,
        "attention_log": attention_log
    }
    with open(os.path.join(output_dir, "main_result_with_log.json"), "w", encoding="utf-8") as f:
        json.dump(main_result, f, indent=4, ensure_ascii=False)

    # (3) 모달리티별 Top 10 JSON 저장 (전체 합산 Top 10 / 스텝별 개별 Top 10)
    modalities = {
        "video": video_idx,
        "audio": audio_idx,
        "text": text_idx
    }

    for mod_name, mod_idx in modalities.items():
        if not mod_idx: continue
        
        total10_data = get_total_top10(mod_idx, attention_history, tokens)
        individual10_data = get_individual_top10(mod_idx, attention_history, tokens, generated_tokens)
        
        with open(os.path.join(output_dir, f"{mod_name}_total10_attention_log.json"), "w", encoding="utf-8") as f:
            json.dump(total10_data, f, indent=4, ensure_ascii=False)
            
        with open(os.path.join(output_dir, f"{mod_name}_individual10_attention_log.json"), "w", encoding="utf-8") as f:
            json.dump(individual10_data, f, indent=4, ensure_ascii=False)

    # ==========================================
    # 5. 다음 비디오 처리를 위한 메모리 정리 (OOM 방지)
    # ==========================================
    del inputs
    del outputs
    del attention_history
    torch.cuda.empty_cache()
    gc.collect()

print("\n[INFO] 모든 데이터셋 처리 및 JSON 저장이 완료되었습니다!")