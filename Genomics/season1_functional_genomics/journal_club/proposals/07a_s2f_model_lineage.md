# cf) S2F model 계보 — sequence-to-function reading roadmap

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **sub-page of 조윤진 (teammate)'s proposal** · 📅 Feb 2026 · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안 › [윤진] Personalized gene expression…*

---

### Sequence-to-Function 모델 핵심 논문 로드맵

#### 🏛️ 1세대: CNN 기반 분류 모델 (2015–2016)

**DeepSEA** ⭐ — *필독*<br>Zhou & Troyanskaya<br>*Nature Methods* 12, 931–934 (2015)<br>[https://doi.org/10.1038/nmeth.3547](https://doi.org/10.1038/nmeth.3547)

이 분야의 시조 논문. 1kb DNA 서열 → 919개 chromatin feature (TF binding, DNase, histone) 이진 분류. ENCODE/Roadmap 데이터를 학습한 최초의 대규모 다중작업 CNN. In silico 단일염기 치환으로 noncoding variant 효과 예측이라는 패러다임을 제시. 이후 모든 모델의 출발점.

---

**Basset** — *구조 이해에 필수*<br>Kelley, Snoek & Rinn<br>*Genome Research* 26, 990–999 (2016)<br>[https://doi.org/10.1101/gr.200535.115](https://doi.org/10.1101/gr.200535.115)

DeepSEA를 이어받아 오픈소스(Torch) 패키지로 공개. DNase-seq peak 분류에 집중. ISM(in silico mutagenesis)으로 모델 해석 방법론을 체계화. Basset → Basenji → Enformer로 이어지는 Kelley lab 계보의 시작점.

---

#### 🐕 2세대: Dilated CNN + 정량적 예측 (2018–2020)

**Basenji** ⭐ — *필독*<br>Kelley et al.<br>*Genome Research* 28, 739–750 (2018)<br>[https://doi.org/10.1101/gr.227819.117](https://doi.org/10.1101/gr.227819.117)

이진 분류(peak/no peak)에서 **정량적 genomic track 예측**으로의 전환점. Dilated CNN으로 receptive field를 131kb까지 확장 (DeepSEA의 1kb 대비 100배). CAGE, DNase, ChIP-seq coverage를 128bp 해상도로 예측. eQTL sign 예측 등 variant effect 해석의 새 기준 제시.

---

**Basenji2 (cross-species)** — *진화적 신호 활용의 출발*<br>Kelley<br>*PLOS Computational Biology* 16, e1008050 (2020)<br>[https://doi.org/10.1371/journal.pcbi.1008050](https://doi.org/10.1371/journal.pcbi.1008050)

인간+마우스 **공동 학습**으로 cross-species regulatory grammar 이전을 최초 실증. eQTL 예측 성능 유의미하게 향상. 이후 Enformer, Borzoi, AlphaGenome으로 이어지는 multispecies training 전통의 기반.

---

**ExPecto** — *expression 예측의 선구자*<br>Zhou et al.<br>*Nature Genetics* 51, 1160–1169 (2019)<br>[https://doi.org/10.1038/s41588-019-0434-0](https://doi.org/10.1038/s41588-019-0434-0)

Beluga(DeepSEA 업그레이드) → 조직별 유전자 발현 예측의 2단계 프레임워크. TSS 주변 chromatin feature → 조직특이적 mRNA 양 예측. GWAS causal variant 우선순위화에 직접 적용 가능한 첫 실용적 발현 예측 모델.

---

#### 🧠 3세대: Transformer + 장거리 상호작용 (2021–2022)

**BPNet** ⭐ — *해석가능성의 이정표*<br>Avsec, Weilert, Shrikumar et al. (Kundaje & Zeitlinger labs)<br>*Nature Genetics* 53, 354–366 (2021)<br>[https://doi.org/10.1038/s41588-021-00782-6](https://doi.org/10.1038/s41588-021-00782-6)

단일 TF에 집중하여 **베이스 해상도** (1bp) ChIP-nexus profile 예측. DeepLIFT/TF-MoDISco로 모티프 문법(syntax) 발견 — Nanog의 helical periodicity(10.5bp), TF간 directional cooperativity를 CRISPR로 실험 검증. Contribution score 기반 해석 방법론의 교과서.

---

**Enformer** ⭐⭐ — *가장 중요한 전환점*<br>Avsec, Agarwal et al. (DeepMind + Calico)<br>*Nature Methods* 18, 1196–1203 (2021)<br>[https://doi.org/10.1038/s41592-021-01252-x](https://doi.org/10.1038/s41592-021-01252-x)

이 계보의 **정점**이자 현대 모델들의 직접적 출발점. 200kb 입력 → CNN stem + **Transformer** → 5,313개 genomic track (인간+마우스). Receptive field: Basenji2의 20kb → **100kb** (5배 확장). Attention이 enhancer-promoter interaction을 자연스럽게 학습. CAGI5 saturation mutagenesis 챌린지에서 최고 성능. 이 논문 이후 "transformer가 regulatory genomics를 이해한다"는 공감대 형성.

---

**Sei** — *genome-wide regulatory vocabulary*<br>Chen, Wong, Troyanskaya & Zhou<br>*Nature Genetics* 54, 940–949 (2022)<br>[https://doi.org/10.1038/s41588-022-01102-2](https://doi.org/10.1038/s41588-022-01102-2)

21,907개 chromatin profile을 예측하는 가장 포괄적인 CNN 모델. 예측을 클러스터링해 **40개 sequence class** (promoter, tissue-specific enhancer, CTCF 등) vocabulary 도출 — "regulatory alphabet" 개념. GWAS heritability를 sequence class별로 분해해 복잡 형질의 조절 구조를 해부하는 새 방법론 제시.

---

#### 🦅 4세대: 초장거리 + 멀티모달 + RNA (2023–2025)

**Borzoi** ⭐ — *RNA까지 통합한 unifying model*<br>Linder, Srivastava, Yuan, Agarwal & Kelley (Calico)<br>*Nature Genetics* 57, 949–961 (2025)<br>[https://doi.org/10.1038/s41588-024-02053-6](https://doi.org/10.1038/s41588-024-02053-6)

Enformer를 **RNA-seq coverage 예측**으로 확장한 현재 state-of-the-art. 524kb 입력 → 전사, 스플라이싱, 폴리아데닐화를 **단일 모델**에서 동시 예측. sQTL/paQTL 예측에서 특화 모델과 동등하거나 우월. RNA-seq 데이터의 풍부함으로 훈련 데이터 확장성 획기적 향상. "DNA 서열 하나로 RNA 처리의 모든 레이어를 예측한다"는 비전 실현.

---

**AlphaGenome** ⭐⭐ — *현재 최고 성능*<br>Cheng et al. (Google DeepMind)<br>*Nature* (2025)<br>[https://doi.org/10.1038/s41586-025-09165-5](https://doi.org/10.1038/s41586-025-09165-5)

현존 sequence-to-function 모델의 **최고봉**. 1Mb 입력 서열 → 11가지 출력 유형 (gene expression, chromatin accessibility, TF binding, 3D genome contact, splicing 등)을 **동시** 예측. U-Net + sequence parallelism으로 1Mb 처리. 25개 variant effect 평가 중 25개에서 이전 모델 대비 동등하거나 우월. Gosai et al.의 MPRA 데이터로 validation. 멀티스케일 U-Net 아키텍처가 local + global 정보를 동시 통합.

---

#### 📚 보너스: 필수 리뷰 논문

**"Predicting gene expression from DNA sequence using deep learning models"**<br>Barbadilla-Martínez et al.<br>*Nature Reviews Genetics* (2025)<br>[https://doi.org/10.1038/s41576-025-00841-2](https://doi.org/10.1038/s41576-025-00841-2)

위 모델 계보 전체를 체계적으로 리뷰하는 2025년 최신 종설. DeepSEA부터 Borzoi까지의 아키텍처 진화, 훈련 데이터 전략, 해석 방법, 한계를 한 논문에서 조망.
