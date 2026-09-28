<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › **🧪 Experiments**</sub>

# 🧪 Experiments — probing video-SALMONN 2+ for audio-visual hallucination

Two small pilots that turned the phase-3 reading into measurements on a real audio-visual LLM, [video-SALMONN 2+](https://github.com/bytedance/video-SALMONN-2) (Tsinghua University & ByteDance). E1 logs *where* the model attends while answering hallucination-probing questions (AVHBench). E2 scores it on the seven diagnostic tasks of DAVE.

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

오디오-비주얼 LLM인 video-SALMONN 2+를 대상으로 한 두 개의 소규모 파일럿 실험입니다. E1은 AVHBench 질문에 답할 때 생성 토큰마다 영상·오디오·텍스트 중 어디에 어텐션을 주는지 기록합니다. E2는 DAVE 벤치마크의 7가지 진단 과제(소리-행동 정렬, 영상만, 오디오만, 텍스트만, 시간 순서, 행동 인식, 소리 분류)로 모델을 채점합니다. 비유하자면 E1은 학생이 문제를 풀 때 시선이 어디로 가는지 추적한 것이고, E2는 과목별로 나눈 진단 평가지로 약점을 찾은 것입니다. 둘 다 표본이 작아 경향을 보는 용도이며, 코드는 원본 저장소에 넣어 실행하는 스크립트만 담았습니다.

</details>

| # | Question | Model / data | Headline | Folder |
|---|---|---|---|---|
| E1 | Where does the model look when it answers? | 7B (analysis) · AVHBench, 12 videos = 6 original / mismatched pairs, 33 questions | 20 / 27 yes-no answers matched the label; 4 of 6 mismatched pairs called "matching"; answer tokens draw mostly on the text prompt | [E1_avhbench_attention](E1_avhbench_attention/README.md) |
| E2 | Which audio-visual sub-skill breaks? | 3B · DAVE `epic` split, 50 random samples, 7 tasks | AV alignment 0.46 (23/50, chance 0.20); audio classification 0.68; temporal ordering 0.10; 0 / 9 on "none of the above" | [E2_dave_eval](E2_dave_eval/README.md) |

## Provenance & licence

- All scripts here were written by Jiheon Kang on top of the upstream `video_SALMONN2_plus/inference.py`. They keep its copyright header and are distributed under the upstream Apache-2.0 licence ([LICENSE-video-SALMONN-2](LICENSE-video-SALMONN-2)).
- **Not vendored:** the video-SALMONN 2 repository itself (clone it from [bytedance/video-SALMONN-2](https://github.com/bytedance/video-SALMONN-2)). Also left out: an unmodified copy of upstream `inference.py`, the DAVE dataset-card usage example (`dave_data.py`), and two earlier local copies of the DAVE script, superseded by `E2_dave_eval/eval_dave.py`.
- Portfolio copies differ from the originals only in removed machine-specific paths (now command-line options) and provenance comments; the file headers say what changed.
- Not included: datasets, model weights and the raw attention logs (JSON per question).

---
<sub>[← 05 · Audio-visual](../05_audio_visual/README.md) · [📑 Hallucination index](../README.md) · [E1 →](E1_avhbench_attention/README.md)</sub>
