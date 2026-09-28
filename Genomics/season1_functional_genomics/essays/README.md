<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › **Essays**</sub>

# Essays — my own takes

Two notes where I argue rather than summarise: whether genome LMs should shed or keep inductive bias, and what the YAICON experiments (gDTR, ΔH) left open.

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

첫 번째 글은 "데이터와 규모만 늘리면 된다"는 Bitter Lesson이 유전체 언어 모델에도 통하는지 묻습니다. DNABERT부터 Evo 2까지 세대별로 어떤 가정(토크나이저, 학습 데이터 선택, 손실 가중치)이 모델에 들어갔는지 따라가 보면, 최신 모델일수록 오히려 생물학적 사전지식을 다시 넣고 있다는 것이 제 결론입니다. 아이에게 백과사전을 통째로 주는 것보다 목차와 중요한 장을 표시해 주는 편이 나을 때가 있는 것과 비슷합니다. 두 번째 글은 YAICON 실험(층별 settling을 보는 gDTR, 중요한 층과 정보가 남은 층을 비교한 ΔH)을 돌아보며 남은 질문과 지표 아이디어를 정리했고, 이 흐름이 GDTR 논문으로 이어졌습니다.

</details>

| Note | Author | Date | What it is |
|---|---|---|---|
| [Inductive bias in gLMs? (essay)](01_inductive_bias_in_glms.md) | 강지헌 (me) | 2026 S1 | My essay: does "less inductive bias" (the bitter lesson) suit genome LMs? DNABERT → NT → DNABERT-2/HyenaDNA → Caduceus/Evo → Evo 2, and where biological priors re-enter. |
| [야이콘 방향성 · gDTR & ΔH](02_yaicon_direction_gdtr.md) | 강지헌 (me) | 2026 | Reflection on the YAICON project: Task 1 gDTR (layer-wise settling) and Task 2 ΔH (representative vs load-bearing layers) — open questions and metric ideas. |

**Related:** [11th meeting — where the DTR idea came up](../meetings/10_meeting11_2026-04-05.md) · [02_Paper/GDTR](https://github.com/heoneyzi/Paper/blob/main/GDTR/README.md) · [01_Medical/GDTR](https://github.com/heoneyzi/Medical/blob/main/GDTR/README.md)

---
<sub>[← Meetings](../meetings/README.md) · [Season 1](../README.md) · [Season 2 →](../../season2_functional_genomics_2/README.md)</sub>
