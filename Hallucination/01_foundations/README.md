<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › **01 · Foundations**</sub>

# 📘 01 · Foundations — what hallucination is and why models do it

Background reading from May–June 2025: a survey of multimodal hallucination, plus two overviews Jiheon wrote on the two suspected causes, attention that misses the image and a language prior that overrides it. A short side track covers hallucination in code LLMs. The notes are in Korean.

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

멀티모달 환각을 공부하기 시작하며 정리한 기초 노트 모음입니다. 서베이 논문으로 환각의 종류(객체·속성·관계)와 원인(데이터·모델 구조·학습·추론)을 먼저 훑었습니다. 이어서 두 가지 원인 가설을 각각 개요로 정리했습니다. 하나는 어텐션이 이미지를 제대로 보지 못한다는 것(PAI, DAMRO 등), 다른 하나는 언어 사전지식이 이미지 정보를 덮어쓴다는 것(TVC, OPERA, AGLA 등)입니다. 코드 LLM의 환각(CodeHalu)은 '환각과 에러의 차이'를 생각해 보기 위한 번외 노트입니다.

</details>

| # | Note | What it covers | Date |
|---|---|---|---|
| 1 | [MLLM hallucination survey](01_mllm_hallucination_survey.md) | Hallucination types; causes across data, model, training and inference; evaluation and mitigation families | 2025-05 |
| 2 | [Overview ① Visual attention](02_visual_attention_overview.md) | How attention is wired in an LVLM, and six attention interventions (PAI, DAMRO, PAINT, IMCCD, attention calibration, hallucination heads) with his critique | 2025-05 |
| 3 | [Overview ② Language prior](03_language_prior_overview.md) | Visual forgetting (TVC), attention-guided decoding, head suppression, OPERA, M3ID; AGLA marked as the key paper | 2025-06 |
| 4 | [Code hallucination (side track)](04_code_hallucination.md) | Reading-list stub | — |
| 5 | [CodeHalu](05_codehalu.md) | Execution-based definition and a four-type taxonomy of code hallucination | — |

---
<sub>[📑 Hallucination index](../README.md) · [02 · Paper reviews →](../02_paper_reviews/README.md)</sub>
