<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › **02 · Paper reviews**</sub>

# 📝 02 · Paper reviews — DAMRO, AGLA, ARGUS

Three close readings that shaped the phase-1 team idea (May–June 2025). Each covers a different lever: DAMRO for vision-side attention sinks, AGLA for prompt-aware attention, ARGUS for grounded visual chain-of-thought. The notes are in Korean.

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

1단계 팀 아이디어의 뼈대가 된 논문 세 편의 리뷰입니다. DAMRO 리뷰에는 논문의 근거가 충분한지, CLS 토큰으로 이상치를 고르는 방식이 타당한지 등 직접 던진 질문이 담겨 있고, 이 질문들에서 본인의 아이디어가 출발했습니다. AGLA는 질문과 관련된 이미지 영역만 남겨 보도록(Grad-CAM 기반 마스킹) 만드는 방법으로, 이후 아이디어 회의의 핵심 참고 논문이 되었습니다. ARGUS는 관심 영역을 다시 잘라 보는 '시각적 CoT' 구조를 정리했습니다.

</details>

| # | Note | What it covers | Date |
|---|---|---|---|
| 6 | [DAMRO](01_damro.md) | ViT and LLM attention both pile onto a few background "outlier" tokens; CLS-based selection plus contrastive decoding; three critical questions of his own | 2025-05 |
| 7 | [AGLA](02_agla.md) | Prompt-aware local attention via Grad-CAM image–prompt matching, assembled with global attention; code walk-through | 2025-06 |
| 8 | [ARGUS](03_argus.md) | Mixture-of-encoder LVLM with ROI sampling and re-engagement (grounded chain-of-thought) | 2025-06 |

---
<sub>[← 01 · Foundations](../01_foundations/README.md) · [📑 Hallucination index](../README.md) · [03 · Research log →](../03_research_log/README.md)</sub>
