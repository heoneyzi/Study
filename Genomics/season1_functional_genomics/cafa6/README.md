<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › **CAFA 6**</sub>

# CAFA 6 — protein function prediction (Jan – Feb 2026)

Kick-off planning and each member's CAFA 6 route. CAFA 6 asks for a protein's Gene Ontology functions from its amino-acid sequence alone; the team finished with a **Bronze Medal**. The full project write-up and code are in [01_Medical/CAFA6](https://github.com/heoneyzi/Medical/blob/main/CAFA6/README.md).

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

CAFA 6는 단백질의 아미노산 서열만 보고 그 단백질이 하는 일(GO term)을 맞히는 국제 대회입니다. 이 폴더에는 킥오프 때의 방향 논의와 후보 대회 비교, 그리고 팀원별 시도(유민: 공개 솔루션·GOA 조사, 윤진: ESM-C 임베딩과 GO 그래프 GCN, 수빈: JEPA, 지헌: ProtT5 임베딩과 데이터셋 정리)가 담겨 있습니다. 비유하자면 처음 보는 사람의 이력서(서열)만 보고 직업(기능)을 여러 개 맞히는 문제인데, 직업 분류표가 트리 구조라 "외과의"라면 "의사"도 함께 맞혀야 합니다. 대회 전체 정리와 코드는 01_Medical/CAFA6 폴더에 있습니다.

</details>

## 👥 Who tried what

| Member | Route | Source |
|---|---|---|
| 정유민 | Public solutions, GOA annotations, GO retriever | [week-1 survey](04_yumin_cafa6_week1.md) · [3차 회의](../meetings/03_meeting03_2026-01-21.md) |
| 조윤진 (team lead) | ESM-C embeddings with pooling variants + GCN over the GO DAG | [first attempt](05_yoonjin_code_attempt1.md) · [method](06_yoonjin_method.md) |
| 강지헌 (me) | ProtT5 (T5) embedding comparison; dataset walkthrough and ideas | [3차](../meetings/03_meeting03_2026-01-21.md) · [4차 회의](../meetings/04_meeting04_2026-01-29.md) · [01_Medical/CAFA6 notes](https://github.com/heoneyzi/Medical/blob/main/CAFA6/notes/README.md) |
| 박수빈 | JEPA-style label-representation learning | [JEPA note](07_subin_cafa6_jepa.md) |

<sub>Only routes documented in the Notion archive are listed.</sub>

## 📄 Notes

| Note | Author | Date | What it is |
|---|---|---|---|
| [프로젝트 방향성 · project direction](01_project_direction.md) | 조윤진 · 🤖 | 2026-01 | Kick-off proposal: enter CAFA 6 first (deadline 2 Feb) vs. aim straight at the Virtual Cell Challenge; pasted ChatGPT reading lists on Perturbation-prediction models. |
| [Challenge · candidate challenges](02_challenge_candidates.md) | 조윤진 | 2026-01 | Side-by-side comparison of candidate challenges (CAGI7 RGP-CRAM, CAFA 6, Virtual Cell Challenge, DREAM Target 2035): task, data, access, metric, prizes. |
| [perplexity가 알려준 논문 · leads](03_perplexity_paper_leads.md) | 조윤진 · 🤖 | 2026-01 | Perplexity-generated leads: single-cell foundation models, Nicheformer, GNN-based GRN inference, plant single-cell FMs, Genos. |
| [[유민] CAFA6 첫주 · week-1 survey](04_yumin_cafa6_week1.md) | 정유민 | 2026-01-21 | Public CAFA 6 kernels and datasets (GOA + ProtT5 ensembles, shared pLM embeddings) and notes on top CAFA 5 solutions (GCN refinement). |
| [[지헌] CAFA6 톺아보기 ↗](https://github.com/heoneyzi/Medical/blob/main/CAFA6/notes/README.md) | 강지헌 (me) | 2026-01 | Hub of my CAFA 6 notes (kept in **01_Medical/CAFA6**, not duplicated here). |
| [데이터셋 정리 · dataset walkthrough ↗](https://github.com/heoneyzi/Medical/blob/main/CAFA6/notes/01_dataset.md) | 강지헌 (me) | 2026-01 | File-by-file guide to the CAFA 6 data (FASTA, GO terms, taxonomy, `go-basic.obo`, IA weights, submission format). Canonical copy of 4 identical Notion copies. |
| [아이디어 · modeling ideas ↗](https://github.com/heoneyzi/Medical/blob/main/CAFA6/notes/02_ideas.md) | 강지헌 (me) | 2026-01 | Ideas: GOA-based distillation into ESM-2 + classifier, GO-term tokenization (ESM-3 style), text contrast, DAG-aware losses. |
| [[윤진] 코드 1차 시도 · first attempt](05_yoonjin_code_attempt1.md) | 조윤진 | 2026-01 | ESM-C embeddings with mean / mean⊕max / CLS pooling + linear heads; plan for a GO-DAG GCN; what the IA (information accretion) weights mean. |
| [Method · planned variants](06_yoonjin_method.md) | 조윤진 | 2026-01 | Four planned variants (pooling × GCN over the GO DAG) with the parent ≥ child constraint and CAFA F-max evaluation. |
| [[수빈] CAFA6 시도 · JEPA](07_subin_cafa6_jepa.md) | 박수빈 | 2026-02 | JEPA-style label-representation learning for GO prediction (code: SOL1archive/CAFA6) and reflections on the first submission. |

<sub>↗ My three CAFA 6 notes are kept once, in 01_Medical/CAFA6; the Notion workspace held four identical copies of the dataset walkthrough.</sub>

---
<sub>[Season 1](../README.md) · [Journal club →](../journal_club/README.md)</sub>
