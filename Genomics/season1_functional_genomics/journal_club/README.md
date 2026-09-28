<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › **Journal club**</sub>

# Journal club — genome language models (Feb – Apr 2026)

Five sessions that asked whether DNA "language" models understand regulation — from a field survey to Evo 2 and AlphaGenome. Paper proposals live in [proposals/](proposals/README.md); meeting recaps in [meetings/](../meetings/README.md).

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

매주 한 편씩 유전체 언어 모델(gLM) 관련 논문을 읽고 토론한 기록입니다. 1주차 서베이로 전체 지형(아키텍처·토크나이저·사전학습·평가)을 잡고, 2주차에는 제가 "사전학습된 gLM 표현이 원-핫 인코딩보다 정말 나은가"를 검증한 논문을 발표했습니다. 3주차는 강화학습으로 세포 특이적 DNA 조절 서열을 설계하는 Ctrl-DNA, 4·5주차는 Evo 2와 AlphaGenome을 다뤘습니다. 외국어 사전을 통째로 외운 것(gLM)과 그 언어로 실제 대화를 잘하는 것(세포별 조절 예측)은 다르다는 점이 반복해서 확인되었습니다. 🤖 표시가 있는 하위 페이지는 팀원이 참고용으로 붙여 둔 AI 답변입니다.

</details>

## 🗓️ Sessions

| Week | Paper | Notes by | Session | Notes · recap |
|---|---|---|---|---|
| 1 | *A comprehensive survey of genome language models in bioinformatics* | 조윤진 | 2026-02-15 | [notes](01_week1_glm_survey.md) · [recap](../meetings/07_meeting06_jc1_2026-02-15.md) |
| 2 | *Evaluating the representational power of pre-trained DNA language models for regulatory genomics* | **강지헌 (me, presenter)** | 2026-02-18 | [notes](02_week2_glm_evaluating.md) · [recap](../meetings/08_meeting07_jc2_2026-02-18.md) |
| 3 | *Ctrl-DNA: controllable cell-type-specific regulatory DNA design via constrained RL* | 박수빈 (presenter) | 2026-03-02 | [notes](03_week3_ctrl_dna.md) · [recap](../meetings/09_meeting08_jc3_2026-03-02.md) |
| 4 | *Genome modeling and design across all domains of life with Evo 2* | 정유민 | 11th meeting (Apr) | [notes](04_week4_evo2.md) · [recap](../meetings/10_meeting11_2026-04-05.md) |
| 5 | *Advancing regulatory variant effect prediction with AlphaGenome* | 구민선 | 11th meeting (Apr) | [notes](05_week5_alphagenome.md) · [recap](../meetings/10_meeting11_2026-04-05.md) |

## 📄 All notes

| Note | Author | Date | What it is |
|---|---|---|---|
| [Week 1 · GLM survey](01_week1_glm_survey.md) | 조윤진 | 2026-02-15 | Long summary of *A comprehensive survey of genome language models in bioinformatics*: why gLMs, Transformer/Hyena/SSM, tokenization, pretraining data, evaluation, benchmarks, open problems. |
| [둘이 뭐가 다른데? · Evo 2 vs AlphaGenome](01a_evo2_vs_alphagenome_representations.md) | 조윤진 · 🤖 | 2026-02 | ChatGPT explanation of what an autoregressive gLM's hidden states encode (sequence statistics) vs a sequence-to-function model (functional signal). |
| [뭔 말이냐면 · task-specific models](01b_why_task_specific_models_win.md) | 조윤진 · 🤖 | 2026-02 | ChatGPT explainer: sequence-to-signal regression and variant scoring — why Enformer, DeepSEA, ChromBPNet and CADD still beat general gLMs. |
| [Week 2 · gLM evaluating (my talk)](02_week2_glm_evaluating.md) | 강지헌 (me) | 2026-02-18 | My week-2 talk on *Evaluating the representational power of pre-trained DNA language models for regulatory genomics* (Genome Biology 2025): six tasks, attribution maps, why gLM probes rarely beat one-hot CNNs. |
| [부가설명 · CREs & TFs](02a_cre_tf_explainer.md) | 강지헌 (me) | 2026-02-18 | Plain-language side note: cis-regulatory elements (promoter, enhancer, silencer, insulator) and transcription factors. |
| [저널 2 리뷰 · companion notes](02b_week2_review_notes.md) | 강지헌 (me) | 2026-02 | Which gLMs were compared, how embeddings were probed (penultimate layer, CLS/mean → ridge/MLP/CNN), and my discussion questions. |
| [Week 3 · Ctrl-DNA](03_week3_ctrl_dna.md) | 박수빈 | 2026-03-02 | Ctrl-DNA: constrained RL (CMDP, Lagrangian primal–dual, GRPO-style advantages, TFBS regularizer) for cell-type-specific regulatory DNA design. |
| [Week 4 · Evo 2](04_week4_evo2.md) | 정유민 | 2026-04 | Figure-by-figure Evo 2 review (OpenGenome2, 1 Mb context, zero-shot variant effects, SAE features, genome-scale generation) with discussion prompts on inductive bias. |
| [Week 5 · AlphaGenome](05_week5_alphagenome.md) | 구민선 | 2026-04 | AlphaGenome deep dive: genome tracks, splice-junction modeling, teacher–student distillation, variant case studies (TAL1), MPRA benchmarks, limitations. |
| [전체세션 발표 구성 · talk outline](06_allhands_talk_outline.md) | — | S1 | Outline of an all-hands talk on genome LMs: "Genome GPT?", the 98 % non-coding problem, representation under scrutiny, toward conditional multimodal gLMs. |

---
<sub>[← CAFA 6](../cafa6/README.md) · [Season 1](../README.md) · [Proposals →](proposals/README.md)</sub>
