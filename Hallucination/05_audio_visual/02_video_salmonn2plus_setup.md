# video-SALMONN 2+ 환경 세팅

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › [05 · Audio-visual](README.md)</sub>

> 🗓️ 2026-03 · Audio-Visual LLM 환각 (3단계)

> 업스트림: [bytedance/video-SALMONN-2](https://github.com/bytedance/video-SALMONN-2) — 이 설정으로 돌린 실험은 [experiments/](../experiments/README.md) 참고.

---

```bash
# 가상환경 맞추기

conda create -n salmonn python=3.10 -y

conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main

conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

conda activate salmonn

pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 numpy==1.24.4

pip install psutil

pip install flash-attn==2.7.4.post1 --no-build-isolation --no-cache-dir
pip install liger_kernel==0.5.10 --no-build-isolation

pip install accelerate==1.7.0 decord==0.6.0 deepspeed==0.16.0 peft==0.15.2 tokenizers==0.21.0 torchcodec==0.4.0 transformers==4.51.3

apt-get update

apt-get install ffmpeg -y
```

```
data_args.video_max_frames = 768
data_args.video_min_frames = 16
data_args.base_interval = 0.1
data_args.max_pixels = 61250
data_args.video_max_frame_pixels = 61250
```

RANK 0 video_embeds: torch.Size(\[29205, 2048\])<br>RANK 0 audio_embeds: torch.Size(\[60, 2048\])

As the video progresses, the skewers continue to cook, their surfaces becoming more golden brown, suggesting they are nearing completion. The overall scene conveys a sense of authenticity and tradition associated with the preparation of lamb skewers from the Hulunbuir Grassland, emphasizing the quality and origin of the ingredients used.

```
data_args.video_max_frames = 16 #768
data_args.video_min_frames = 16
data_args.base_interval = 0.1
data_args.max_pixels = 20000 #61250
data_args.video_max_frame_pixels = 20000 #61250
```

RANK 0 video_embeds: torch.Size(\[144, 2048\])<br>RANK 0 audio_embeds: torch.Size(\[60, 2048\])

There is no specific mention of any text or additional objects within this clip, keeping the focus solely on the mechanical component and its surroundings. The video does not show any movement or changes in the scene, maintaining a static view throughout the duration of the clip.

Token Index    0: \<\|im_start\|\><br>Token Index    1: system<br>Token Index    2: Ċ<br>Token Index    3: You<br>Token Index    4: Ġare<br>Token Index    5: Ġa<br>Token Index    6: Ġhelpful<br>Token Index    7: Ġassistant<br>Token Index    8: .<br>Token Index    9: \<\|im_end\|\><br>Token Index   10: Ċ<br>Token Index   11: \<\|im_start\|\><br>Token Index   12: user<br>Token Index   13: Ċ<br>Token Index   14: \<\|vision_start\|\><br>Token Index   15: \<\|video_pad\|\><br>…<br>Token Index  163: \<\|video_pad\|\><br>Token Index  164: \<\|audio_pad\|\><br>…<br>Token Index  218: \<\|audio_pad\|\><br>Token Index  219: \<\|vision_end\|\><br>Token Index  251: Ġand<br>Token Index  252: Ġensure<br>Token Index  253: Ġthat<br>Token Index  254: Ġyour<br>Token Index  255: Ġdescriptions<br>Token Index  256: Ġof<br>Token Index  257: Ġthe<br>Token Index  258: Ġaudio<br>Token Index  259: Ġand<br>Token Index  260: Ġvideo<br>Token Index  261: Ġare<br>Token Index  262: Ġclosely<br>Token Index  263: Ġaligned<br>Token Index  264: .<br>Token Index  265: \<\|im_end\|\><br>Token Index  266: Ċ<br>Token Index  267: \<\|im_start\|\><br>Token Index  268: assistant<br>Token Index  269: Ċ

---
<sub>[← Video-Audio LLM Hallucination — AVCD 분석과 방향 전환](01_video_audio_llm_hallucination.md) · [📑 목차](../README.md) · [video-SALMONN 2+ 1차 결과 분석 →](03_video_salmonn2plus_first_results.md)</sub>
