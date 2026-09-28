# [유민] Accelerating protein engineering with fitness landscape modelling and reinforcement learning

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **정유민 (teammate)** · 📅 week-1 proposal (Feb 2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 1주차 · — not selected · 읽고 싶어요: 유민

---

**\[1주차 저널클럽 후보\]<br>Accelerating protein engineering with fitness landscape modelling and reinforcement learning<br>Nature Machine Intelligence, Sep 2025**

[https://www.nature.com/articles/s42256-025-01103-w](https://www.nature.com/articles/s42256-025-01103-w)

μProtein 프레임워크: 단백질의 mutational effect를 예측하는 딥러닝 모델 μFormer + 이를 oracle로 활용해 서열 공간을 탐색하는 RL알고리즘 μSearch를 결합함.

\[특징\]

1. RL기반 서열 공간 탐색(μSearch): PPO + Dirichlet noise 탐색 전략으로 mutation-site policy network와 mutation-type policy network를 분리 설계 → 다른 방법이 도달하지 못하는 높은 fitness 서열을 다수 발견
2. Pairwise Masked Language Model(PMLM) pretrain을 통해 residue 간 공동 진화 정보를 학습 → additive model(다중 변이 효과 = 단일변이 효과의 합으로 근사)로는 잡아내지 못하는 비선형 상호작용을 모델링함
3. Multi-point mutation 일반화: (2)의 Epistasis 모델링을 통해 단일변이 데이터만으로 학습하고도 다중변이 fitness를 정확하게 예측, ProteinGym 벤치에서 기존 방법들을 상회함
4. Wet-lab 검증: lactamase(항생제 내성 유전자) 변이체 생성하여 랜덤 생성 대비 2배의 성공률을 보임

\[읽어볼 이유\]

- PMLM 사전 학습: 토큰 독립성 가정하는 기존 MLM 대비 토큰 쌍의 결합확률을 직접 모델링함 → 단백질 서열 residue간 의존성이 중요한 도메인 지식 반영
- RL formulation: 단백질 최적화를 MDP로 정의하고 PPO로 풀되, dual policy network 분리 + Dirichlet exploration noise 설계
- 머신러닝 모델의 성능 평가를 실험(oracle)로 수행하는 작업 흐름에 대해 이해
