# [민선] DNA-Diffusion: Leveraging Generative Models for Controlling Chromatin Accessibility and Gene Expression via Synthetic Regulatory Elements

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **구민선 (teammate)** · 📅 extra proposal (2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 기타 · — not selected · 읽고 싶어요: 민선

---

[www.biorxiv.org](https://www.biorxiv.org/content/10.1101/2024.02.01.578352v1)

한 줄 요약:

세포 타입 별 ATAC‑seq 데이터로 학습한 Diffusion model을 이용해, 특정 세포 타입에서만 강하게 활성화되는 200bp cis-regulatory elements를 생성하고, 이 서열들이 실제 크로마틴 접근성과 유전자 발현을 세포 특이적으로 높일 수 있음을 보인 논문.

방법 요약:

- **모델 구조**: U-Net 아키텍처 기반의 Denoising Diffusion Probabilistic Model (DDPM)을 사용하며, cell type label과 timestep을 embedding하여 입력받음.
- **데이터셋**: GM12878(면역), K562(혈액암), HepG2(간암) 세포의 DHS(DNase I Hypersensitive Sites) 인덱스 데이터를 활용.
- **학습 및 생성**: DNA 서열을 \[-1, 1\] 범위의 one-hot encoded matrix로 변환 후 노이즈를 추가(Forward process)하고, 이를 다시 제거하는 역과정(Reverse process)을 통해 서열을 생성함 (50 steps).
- **평가 프레임워크**: 생성된 서열이 기존 서열을 단순 memorization했는지 확인하고, ChromBPNet, Enformer, MPRA predictor 등 최신 딥러닝 모델을 사용하여 기능을 검증함.

시사점 & 읽어야하는 이유:

- **Why it fits Evo 2**: Evo 2가 genome-scale의 generative modeling을 수행한다면, DNA-Diffusion은 cell type specific cis-regulatory sequence 설계에 최적화된 로컬 모델. 따라서 local enhancer design vs. whole-genome design 관점에서 대조하며 읽기 좋음.
- Hands-on: 논문의 framework는 특정 세포 타입에 대한 합성 조절 서열을 샘플링한 뒤 Basenji/Enformer 같은 기존 예측 모델로 바로 스코어링할 수 있는 실질적인 workflow를 제공함.
- application: precision gene therapy 설계에 연결이 가능함.
- **확장 가능성**: 세포 타입 라벨만으로 학습하는 구조라, 향후 더 많은 조직 데이터를 통합하여 DNA sequence design용 foundation model로 확장할 수 있을 것 같음
- **접근성**: 코드와 모델이 공개되어 있어(Evo 2와 마찬가지로), 비교적 저렴한 GPU 환경에서도 200bp 조절 서열 생성 해볼 수 있을 것 같음 (사실 이 부분은 잘 모르겠긴 해요…)
