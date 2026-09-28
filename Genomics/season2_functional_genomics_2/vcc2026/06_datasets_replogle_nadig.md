# Replogle Nadig Preprint

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **김서진 (teammate)** · 📅 2026-08 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

\[Replogle-Nadig-Preprint\]

[arcinstitute/Replogle-Nadig-Preprint at main](https://huggingface.co/datasets/arcinstitute/Replogle-Nadig-Preprint/tree/main)

대회 주최하는 ARC Institue에서 만든? 데이터셋

\[원본 데이터셋\]

1. Reploge 2022 - K562 essential + RPE1 essential
    [plus.figshare.com](https://plus.figshare.com/articles/dataset/_Mapping_information-rich_genotype-phenotype_landscapes_with_genome-scale_Perturb-seq_Replogle_et_al_2022_processed_Perturb-seq_datasets/20029387)

    [www.biorxiv.org](https://www.biorxiv.org/content/10.1101/2021.12.16.473013v3.full) → 해당 논문에서 나온 대규모 Perturb-seq 데이터

    ⇒ CRISPRi와 single-cell RNA-seq를 이용해 **250만 개 이상의 human cells**을 프로파일링

    human chronic myelogenous leukemia + retinal pigment epithelial 계열의 human cell line
2. Nadig - HepG2 + RPE1
    [NCBI - WWW Error Blocked Diagnostic](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE264667)

    HepG2와 Jurkat이라는 서로 다른 cell line에 genetic perturbation을 수행<br>

| 구분 | **K562** | **RPE1** | **HepG2** | **Jurkat** |
|---|---|---|---|---|
| 출처 | Replogle et al. | Replogle et al. | Nadig et al. | Nadig et al. |
| 세포 종류 | 백혈병 세포 | 망막 상피 계열 | 간암 세포 | T-cell 백혈병 |
| Species | Human | Human | Human | Human |
| Perturbation | **CRISPRi** | **CRISPRi** | Genetic perturbation | Genetic perturbation |
| 측정 방식 | scRNA-seq / Perturb-seq | scRNA-seq / Perturb-seq | scRNA-seq | scRNA-seq |
| Control | NTC | NTC | Control | Control |
| 핵심 정보 | Gene KD → expression 변화 | Gene KD → expression 변화 | Gene perturbation → expression 변화 | Gene perturbation → expression 변화 |
| 2026 활용 | Training | Training / LOCO validation | Training / LOCO validation | Training / LOCO validation |

\[scPerturb\]

아래는 못쓸 건 아닌데 위에가 더 좋아보여서 밑에거 쓰고 싶으신 분 복붙해가세용

[GitHub - sanderlab/scPerturb: scPerturb: A resource and a python/R tool for single-cell perturbation data](https://github.com/sanderlab/scPerturb)

[scPerturb Single-Cell Perturbation Data: RNA and protein h5ad files](https://zenodo.org/records/7041849)\\

|  |
||
