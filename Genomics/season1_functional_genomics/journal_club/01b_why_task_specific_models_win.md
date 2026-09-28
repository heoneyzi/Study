# 뭔 말이냐면 — why task-specific models still win

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [Journal club](README.md)</sub>

> ✍️ **sub-page of 조윤진 (teammate)'s week-1 notes** · 📅 2026-02 · 🗂️ Source: Notion — *Functional Genomics › 개인 아카이브 › [저널클럽 1주차] GLM survey*

> [!NOTE]
> 🤖 **AI-generated answer (ChatGPT) pasted for reference** — kept because it is part of the team notes; it is not the team's own writing.

---

네 문장 묶음이 말하는 요지는 이거야:

> <b>“DNA foundation model(gLM)</b>은 보통 *일반 목적*으로 pretrain(MLM/AR)돼서 광범위한 task에 ‘그럭저럭’ 강하지만,
> - <b>가장 빡센 정량 예측(트랙 회귀)·정밀 변이효과(variant effect)</b>에서는 <b>처음부터 그 목적에 맞게 설계된 task-specific(전용) 모델</b>(Enformer/DeepSEA/ChromBPNet, 그리고 점수화 스코어러인 CADD)이 여전히 더 강한 경우가 많다.”

아래에서 용어부터 모델별로 “뭘 하는지/왜 강한지”를 풀어줄게.

---

### 1) “Sequence-to-signal regression”이 뭔데?

- <b>DNA 서열(Sequence)</b>을 입력으로 받아서, 실험에서 관측되는 <b>연속 신호(signal track)</b>를 예측하는 <b>회귀(regression)</b> 문제야.
- 예: 1kb\~200kb DNA를 넣으면
    - DNase/ATAC 접근성 트랙
    - ChIP-seq(히스톤 마크/TF 결합) 트랙
    - RNA expression 트랙
        같은 “게놈 좌표별 신호”를 예측

이런 걸 잘 하면, 같은 모델로 **variant effect**도 계산 가능해:

- ref 서열로 예측한 트랙 vs alt(변이) 서열로 예측한 트랙의 차이 = 변이 효과

---

### 2) “Variant scoring”이 뭔데?

한 변이(SNP/indel)가 **병원성/유해성/기능 변화**를 일으킬 가능성을 **점수로 매기는 것**이야.

두 갈래가 있어:

1. **트랙 기반(기능 예측 기반)**: “이 변이가 ATAC/ChIP/expression을 얼마나 바꾸나?”
2. **통합 주석 기반(스코어러)**: 여러 annotation(보존성, 유전자 구조, epigenome 등)을 합쳐 “유해할 확률”을 점수화

---

### 3) 모델들이 각각 “무엇을 잘 하길래” 강한가?

#### A. Enformer (전형적인 sequence-to-signal 최강 계열)

- DeepMind가 제안한 **sequence→functional tracks(특히 발현/조절 신호)** 예측 모델.
- 긴 범위(장거리 조절)를 반영하도록 설계되어 gene expression/variant effect 예측이 강하다고 소개됨. ([Nature](https://www.nature.com/articles/s41592-021-01252-x))

**왜 강하냐(핵심):**

- 목표 자체가 “실험 신호를 맞추는 회귀”라서, gLM처럼 “언어모델 목표(다음 토큰/마스크 복원)”에서 억지로 변환하는 것보다 **목표-평가가 일치**함.

#### B. DeepSEA (강력한 baseline: 1kb 주변의 규제 신호/변이효과)

- “서열 변화가 chromatin features(DNase, TF binding, histone mark 등)를 어떻게 바꾸는지”를 **single-nucleotide sensitivity**로 예측한다고 명시. ([deepsea.princeton.edu](https://deepsea.princeton.edu/))
- 전통적으로 “ref/alt 서열을 둘 다 넣고 예측 차이를 보는” 방식으로 variant effect를 계산하는 대표격. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4768299/))

#### C. ChromBPNet (초정밀 ATAC/DNase profile + bias correction)

- ATAC 같은 데이터는 <b>실험적 bias(Tn5 절단 선호 등)</b>가 크고, 진짜 생물학 신호와 섞임.
- ChromBPNet은 이걸 분리(deconvolve)하도록 **bias-factorized** 구조/학습을 강조하고, base-resolution 프로파일과 footprint까지 잘 뽑는 방향. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/39829783/))

**왜 강하냐(핵심):**

- “실험이 만드는 잡음/편향”까지 모델링해서, **미세한 footprint/변이 영향** 같은 ‘정량·세밀’ 과제에서 유리함.

#### D. CADD (스코어러: “sequence-to-signal”이라기보다 통합 점수)

- CADD는 **여러 annotation을 하나의 deleteriousness score로 통합**하는 프레임워크로 설명됨. ([cadd.gs.washington.edu](https://cadd.gs.washington.edu/))
- 아이디어: 자연선택을 거친(관측된) 변이 vs 시뮬레이션 변이를 대비해 학습해 “유해함”을 점수화. ([cadd.gs.washington.edu](https://cadd.gs.washington.edu/))

**ClinVar/OMIM 같은 임상 데이터에서 왜 자주 언급되냐?**

- ClinVar는 임상적 의미가 달린 변이 해석을 모아둔 공용 아카이브(병원성/양성 등). ([ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/clinvar/))
- OMIM은 인간 유전자–질환(멘델 질환) 관계를 curated한 지식베이스. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/25428349/))
    이런 “병원성/질환” 라벨에 대해 CADD 같은 스코어가 baseline으로 자주 쓰여.

---

### 4) “LRB에서 Enformer/CADD가 리드”는 무슨 뜻?

LRB는 “장거리(long-range) 게놈 과제들을 모아 평가하는 벤치마크”로 소개돼. ([OpenReview](https://openreview.net/forum?id=8O9HLDrmtq))

여기에 보통:

- eQTL 같은 변이-표현형(발현) 연계
- 병원성 변이(ClinVar 등)
- 발현 예측(bulk RNA)
    같은 “현실적으로 어려운(variant-centric, quantitative)” 과제가 들어가고,

이런 과제는

- **표현학습된 gLM 임베딩을 얹는 방식**보다
- <b>처음부터 신호/표현형 예측에 맞춘 모델(Enformer류)</b>이나
- <b>임상 주석을 통합한 스코어러(CADD류)</b>가
    여전히 강하게 나오는 경우가 많다는 맥락이야. ([Google DeepMind](https://deepmind.google/blog/predicting-gene-expression-with-ai/))

---

### 5) 왜 “현재 gLM은 fine-grained variant effect에서 전용모델에 뒤질” 수 있나?

요지는 “목표함수와 출력해상도가 다르기 때문”이야.

- gLM(MLM/AR)은 기본적으로 **서열 자체의 확률/복원**을 학습
    → 기능 신호(ATAC/ChIP/expression)를 “직접” 맞추도록 훈련되지 않음
- 반면 Enformer/DeepSEA/ChromBPNet은 **처음부터 기능 신호 회귀 + 변이효과**를 목표로 설계
    → 특히 **베이스 수준(profile), footprint, 실험 bias 보정** 같은 “정밀 정량”에서 강점 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/39829783/))

그래서 문장에 나온 것처럼:

- gLM도 naive baseline(단순 k-mer, shallow model, 로지스틱 등)보다는 대체로 좋아지지만,
- “진짜 정밀한 변이효과(어느 위치의 어떤 motif가 어떤 cell type에서 신호를 얼마나 바꾸는지)”로 가면 전용모델이 아직 우세한 구간이 남아 있는 거야.

---

원하면, 너가 적어둔 문장을 그대로 기준으로:

- “eQTL 예측”이 정확히 어떤 입력/출력이고,
- Enformer vs (gLM 임베딩+linear head) vs CADD가 각각 어떤 경로로 점수를 내는지
    한 과제를 예시로 들어서 **완전 구체적인 파이프라인**으로 그려줄게.
