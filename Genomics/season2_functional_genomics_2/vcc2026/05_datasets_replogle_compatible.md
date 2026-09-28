# Replogle-호환 Dataset

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **김민석 (teammate)** · 📅 2026-08 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

- 기본적으로 서진님의 Replogle/Nadig dataset을 baseline으로 잡고 가는 것이 좋아보임

#### KOLF2.1J Perturbation Cell Atlas (Nourreddine, Nat Biotech)

[https://y-doctor.github.io/KOLF2.1J_Perturbation_Cell_Atlas/#home](https://y-doctor.github.io/KOLF2.1J_Perturbation_Cell_Atlas/#home)

- hiPSC cell line에서 진행된 perturb-seq data
- KRAB-ZIM3-dCas9 + 10x guide calling
- **25 cell 미만·knockdown 30% 미만 perturbation을 제거하는 QC 파이프라인(PASTA)이 Replogle과 동일**

#### Dataset with additional context - DepMap

- DepMap은 CRISPR-Cas9 KO시 cell line 별 세포 생존율을 정리한 데이터
- 해당 데이터를 바탕으로 sgRNA 별 cell survival dependency를 스칼라로 정리한 모델이 Chronos
    → gene의 ‘중요도’에 대해서 supplementary하게 활용해 볼 수 있지 않을까?
