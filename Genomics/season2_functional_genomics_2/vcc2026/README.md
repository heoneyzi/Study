<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › **VCC 2026**</sub>

# VCC 2026 — team notes on zero-shot Perturbation prediction

Arc Institute's Virtual Cell Challenge 2026 gives only the unperturbed control cells of three unseen cell lines and asks how each of 300 CRISPRi knockdowns changes all 18,533 genes (300 × 400 cells × 3 contexts = 360,000 predicted cells). These are the team's working notes; my code and experiments are in [01_Medical/VCC_2026](https://github.com/heoneyzi/Medical/blob/main/VCC_2026/README.md).

| Key number | Value | Scope · source |
|---|---|---|
| Validation targets already measured in Replogle K562 genome-wide | **272 / 300 (91 %)** | 정유민's day-1 log · [PROGRESS](08b_progress_day1.md) |
| KIMCHI-3 on the validation leaderboard | **30 / 181, Overall +0.0876** (from 73rd, +0.0113) | as of 2026-09-06 · [SUMMARY](08a_summary.md) |
| Control-only baseline submission | Overall −0.312 | pipeline check by 김서진 · [하윙](09_stack_context_transfer.md) |
| Effect transfer vs no effect (Jiang24, local proxy) | −1.343 → −0.98 … −0.76 | my analysis, public data · [Baseline 분석](07_baseline_analysis.md) |

> [!IMPORTANT]
> The challenge is ongoing (the team's notes give 2026-10-22 for the test-set release). Leaderboard figures are validation-phase snapshots; local proxy scores are not leaderboard scores.

## 🗺️ Dataset surveys (one per member)

| Note | Author | Date | What it is |
|---|---|---|---|
| [Perturb 필수 데이터셋 · my dataset map](01_datasets_perturb_essentials.md) | 강지헌 (me) | 2026-08 | My map of datasets for zero-shot Perturbation prediction: Jiang24 (multi-cell-line), Replogle 2022, primary CD4⁺ T, scBaseCount/CELLxGENE, VCC 2025 H1, X-Atlas/Orion, GSE264667. |
| [2026 VCC Datasets + New](02_datasets_vcc2026_and_new.md) | 김서연 | 2026-08 | VCC 2026 data spec (3 contexts × 300 targets × 400 cells × 18,533 genes), Arc Virtual Cell Atlas, public gene/chemical Perturbation sets, lineage-coverage gap table. |
| [Lineage-gap datasets](03_datasets_lineage_gap_candidates.md) | 이동현 | 2026-08 | Prioritized candidates for missing lineages: TeloHAEC endothelial, iPSC neurons/astrocytes, iAssembloids, cortical neurogenesis, THP-1 LPS, IGVF cardiomyocytes. |
| [X-Atlas/Pisces & more](04_datasets_pisces_and_more.md) | 정유민 | 2026-08 | X-Atlas/Pisces (25.6M cells, 16 contexts), Feng 2026 iPSC donors, sci-Plex-GxE, Replogle 2020, Perturb-CITE-seq, PerturbAI mouse atlas — priorities and caveats. |
| [Replogle-호환 Dataset](05_datasets_replogle_compatible.md) | 김민석 | 2026-08 | Replogle-compatible additions: the KOLF2.1J hiPSC atlas (same QC) and DepMap/Chronos as gene-importance context. |
| [Replogle Nadig Preprint](06_datasets_replogle_nadig.md) | 김서진 | 2026-08 | Arc's Replogle–Nadig bundle (K562, RPE1, HepG2, Jurkat) as the baseline training set; scPerturb as an alternative. |

## 🔬 Analyses and approaches

| Note | Author | Date | What it is |
|---|---|---|---|
| [Baseline 분석 · frozen baselines](07_baseline_analysis.md) | 강지헌 (me) | 2026-09 | My analysis: the big jump comes from transferring already-measured CRISPRi effects; the representation used for matching (raw/PCA vs frozen FM embeddings) adds little and is condition-dependent. |
| [1st week · hub](08_week1_hub.md) | 정유민 | 2026-09 | Hub page: fully zero-shot setup; validation leaderboard 30 / 181 (KIMCHI-3, Overall +0.0876); STATE failed → retrieval from the Replogle genome-wide screen. |
| [SUMMARY · KIMCHI line](08a_summary.md) | 정유민 | 2026-09-06 | Write-up of the KIMCHI line: submissions table, emission fixes (rank 73 → 30), holdout→leaderboard transfer rates, oracle decomposition, rejected ideas, next steps. |
| [PROGRESS · day 1](08b_progress_day1.md) | 정유민 | 2026-08-24 | Day-1 log: the 272/300 genome-wide coverage discovery, cell-eval vs cell-eval2 mismatch, cross-cell-line transfer correlations, KIMCHI-2 configuration. |
| [DAY2 · day 2](08c_day2.md) | 정유민 | 2026-08-24 | Day-2 log: FID anchor mismatch, stochastic rounding, shared basal cells, panel centering, response dispersion; rejected shrinkage/rank transfer; uncovered targets. |
| [하윙 · Stack context transfer](09_stack_context_transfer.md) | 김서진 | 2026-09 | Ran Arc's Stack (T=1 vs T=5) on an RTX 3090, validated the submission pipeline (control baseline Overall −0.312), planned multi-source context transfer. |
| [CCLE & Chronos · retrieval + transfer](10_ccle_chronos_retrieval.md) | 김민석 | 2026-09 | Retrieval + transfer with CCLE context routing and DepMap-Chronos magnitude calibration; internal gains did not transfer to the leaderboard — lessons. |

<sub>*SUMMARY* and *PROGRESS* were sanitized: a teammate's institutional e-mail, server paths and the GPU purchasing/budget plan were removed.</sub>

---
<sub>[← Sessions](../sessions/README.md) · [Season 2](../README.md) · [Reviews →](../reviews/README.md)</sub>
