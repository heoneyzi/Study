<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › **05 · Audio-visual**</sub>

# 🎧 05 · Audio-visual — hallucination in video + audio LLMs (Jan – May 2026)

The pivot from image–text models to models that watch and listen. It starts with a dissection of AVCD (NeurIPS 2025) and a hands-on setup of video-SALMONN 2+. An attention analysis on AVHBench (65 plots) follows, then a survey of video and audio hallucination papers and the design of a temporal audio–video benchmark. The notes are in Korean. The code for these runs is in [experiments/](../experiments/README.md).

| # | Note | What it covers | Date |
|---|---|---|---|
| 20 | [Video–audio LLM hallucination](01_video_audio_llm_hallucination.md) | Why move beyond vision; AVCD dissected and critiqued; AV benchmarks (MUSIC-AVQA, AVHBench); audio-LLM decoding (AAD) | 2026-01 |
| 21 | [video-SALMONN 2+ setup](02_video_salmonn2plus_setup.md) | Environment, frame and pixel budgets, prompt token layout | 2026-03 |
| 22 | [video-SALMONN 2+ first results](03_video_salmonn2plus_first_results.md) | 33 AVHBench answers marked 🟦 / 🟥 / 🟧 with layer-wise and per-token modality attention, top audio segments and video patches | 2026-03 |
| 23 | [Video & audio hallucination survey](04_video_audio_hallucination_survey.md) | SEASON, spatiotemporal contrastive decoding, VidHalluc, AAD, ACD error profiles, audio steering, benchmarks | 2026-03 |
| 24 | [Benchmark ideation](05_benchmark_ideation.md) | **His design:** temporal audio–video matching benchmark (question types, data construction, open questions) | 2026 |
| 25 | [Audio datasets](06_audio_datasets.md) | Candidate grounding datasets (ActivityNet Captions, VidSTG, Charades, DiDeMo …) and sound-effect libraries | 2026-04 |
| 26 | [Latest AVLMs](07_latest_avlms.md) | Shortlist of audio-visual models to evaluate | 2026 |

---
<sub>[← 04 · MCoT & attention](../04_mcot_attention/README.md) · [📑 Hallucination index](../README.md) · [🧪 Experiments →](../experiments/README.md)</sub>
