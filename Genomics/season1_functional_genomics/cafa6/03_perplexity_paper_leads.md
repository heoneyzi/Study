# perplexity가 알려준 논문 — paper leads

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [CAFA 6](README.md)</sub>

> ✍️ **조윤진 (teammate)** · 📅 ≈ 2026-01 · 🗂️ Source: Notion — *Functional Genomics › 개인 아카이브*

> [!NOTE]
> 🤖 **AI-generated answer (Perplexity) pasted for reference** — a list of leads, not verified claims.

---

### 1. 싱글셀 파운데이션 모델(scFMs) 계열

- 수천만\~1억 셀 규모의 scRNA-seq을 self-supervised로 학습한 **Single-cell foundation models** 리뷰/포지션 페이퍼가 2025년에 나와서, 앞으로 싱글셀 해석 파이프라인의 기본 단위가 될 거라는 그림을 제시합니다.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586647/)\]
- 대표 모델들:
    - Geneformer, scGPT, scFoundation, GeneCompass, CellFM 등으로, 3,000만\~1억 셀 수준 규모에서 학습된 거대 모델입니다.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12380448/)\]
    - downstream에서 세포 타입 annotation, perturbation 예측, trajectory 인퍼런스 등 거의 모든 태스크를 하나의 latent space에서 해결하는 방향으로 가고 있습니다.\[[pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12586647/)\]

연구 아이디어 관점에서는 “자기 실험 데이터는 그냥 파운데이션 모델에 `fine-tune`/`prompt`하는 시대”를 전제로 설계하는 게 파격 포인트로 보입니다.

### 2. 공간+싱글셀 통합 파운데이션 모델: Nicheformer

- 2025년 Nature Methods에 실린 **Nicheformer: a foundation model for single-cell and spatial omics**는 인간/마우스에서 유래한 거대 SpatialCorpus-110M(해리형+공간 전사체)으로 학습한 트랜스포머 계열 파운데이션 모델입니다.\[[nature](https://www.nature.com/articles/s41592-025-02814-z)\]
- modality, organism, assay 토큰을 넣어서, single-cell과 spatial 데이터를 하나의 joint representation 안에서 학습하고, 기존 Geneformer, scGPT, scVI, PCA 기반 접근보다 다양한 downstream 작업에서 우수한 성능을 보입니다.\[[nature](https://www.nature.com/articles/s41592-025-02814-z)\]

이건 “공간 니치까지 포함한 세포 생태계 레벨의 foundation model”이라, tissue microenvironment, 종양-면역 니치 등과 연계한 functional genomics 설계에 영감을 줄 수 있습니다.

### 3. 그래프 신경망 기반 GRN 인퍼런스 (설명가능성까지 밀어붙인 쪽)

- 2024년 이후, **GNN을 이용한 gene regulatory network(GRN) 인퍼런스**가 causal 정보까지 넣으면서 꽤 공격적으로 나옵니다.\[[nature](https://www.nature.com/articles/s41598-024-71864-8)\]
    - 예: causal 정보를 이용해 neighbor aggregation 시 정보 손실과 잘못된 인과 추론을 줄이는 GCN 기반 GRN 인퍼런스 프레임워크.\[[nature](https://www.nature.com/articles/s41598-024-71864-8)\]
- 2024년 말 bioRxiv의 **GRNIX**는:
    - 실제 자가면역 질환 데이터에서 GNN 기반으로 GRN을 추정하면서, 정확도와 함께 “어떤 edge/노드가 예측에 기여했는지”를 노출하는 explainable GRN 프레임워크를 제시합니다.\[[biorxiv](https://www.biorxiv.org/content/10.1101/2024.11.24.625043v1.full-text)\]
    - 전통적 네트워크 확산, 행렬 분해 계열보다 정확도와 해석가능성을 동시에 잡는다는 점을 강하게 주장합니다.\[[biorxiv](https://www.biorxiv.org/content/10.1101/2024.11.24.625043v1.full-text)\]

실험 디자인 측면에서는 CRISPRi/a perturbation과 GRNIX 같은 모델을 붙여 “모듈/경로 단위 causal 구조”를 보는 쪽까지 확장 가능해 보입니다.

### 4. 식물·비인간 시스템까지 확장된 functional genomics FM

- 2025년 Plant single-cell genomics 리뷰에서는, 위에서 언급한 single-cell FM들을 식물 시스템에까지 확장하는 방향을 정리하면서, virtual cell construction, cross-scale genome modeling(Evo2) 같은 개념을 소개합니다.\[[academic.oup](https://academic.oup.com/gpb/article/23/3/qzaf059/8173801)\]
- transcriptomics, epigenomics, cellular image를 모두 결합하는 멀티모달 single-cell 분석이 앞으로의 표준이 될 것으로 전망하고 있습니다.\[[academic.oup](https://academic.oup.com/gpb/article/23/3/qzaf059/8173801)\]

“식물/비모델 생물–foundation model–멀티오믹스” 조합은, non-model parasite나 host–parasite system으로 옮겨 가도 상당히 임팩트 있는 프레임 짜기 좋습니다.

### 5. Genos: 장거리 컨텍스트를 여는 유전체 파운데이션 모델

- 2025년 중국 BGI-Research와 Zhejiang Lab이 **Genos**라는 100억 파라미터급 genomic foundation model을 공개했다고 보고되는데, 한 번에 최대 100만 bp를 단일 염기 해상도로 분석하는 걸 목표로 합니다.\[[coherentmarketinsights](https://www.coherentmarketinsights.com/industry-reports/functional-genomics-market)\]
- 단순 변이 annotation을 넘어, 장거리 상호작용과 복잡한 조절 패턴 해석까지 염두에 둔 모델로 포지셔닝되어 있어, 3D genome/레귤레이토리 landscape 수준 functional genomics와 잘 맞습니다.\[[coherentmarketinsights](https://www.coherentmarketinsights.com/industry-reports/functional-genomics-market)\]

Hi-C/HiChIP/단일세포 3D 구조와 붙여서 “장거리 enhancer–promoter 기능 예측”까지 가면 꽤 파격적인 연구 설계가 가능해 보입니다.

---
