# [수빈] Ctrl-DNA: Controllable Cell-Type-Specific Regulatory DNA Design via Constrained RL

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **박수빈 (teammate)** · 📅 week-3 proposal (Feb 2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 3주차 · ✅ read together · 읽고 싶어요: 수빈, 유민, 민선, 지헌, 윤진
>
> ➡️ Became the [week-3 session](../03_week3_ctrl_dna.md).

---

#### **한줄 요약**

Constraint RL Setting을 활용해, 세포 유형별로 표적 세포에 대해서는 발현율을 높이고, 비표적 세포에 대해서는 발현율을 임계값 이하가 되도록 하는 CRE Sequence 설계하는 방법론을 만든 논문

#### 방법

1. Batch-wise Advantage 구성
    <p align="center"><img src="assets/6dc97384_01.png" alt="figure" width="720"></p>

    GRPO(DeepSeekMath에서 제안된 방법) 스타일로 별도의 Value Function Learning 없이 Batch-wise Normalization을 활용해 Advantage를 구성하는 방법으로 PPO 스타일을 구현
2. Clipping Objective + KL Regularization
    PPO에서 제시된 것과 같이 Clipping을 활용하고, 여기에 추가로 KL term을 더해 Distribution Shift를 막음
3. Lagrangian Multiplier
    Multi-Objective Setting을, Objective Vector에 대해 Constraint를 준 형태로 표현하고, Constraint를 Lagrangian Multiplier (Constraint안에 있으면 그냥 Scalar 값, Constraint 밖에 있으면 양의 무한 값을 가지는 하나의 Scalar Objective로 구성되도록 식을 재구성)을 적용하고 Primal-Dual로 최종 Objective를 구성.
4. Reward Model & TFBS
    현재 접근 방법은 Online Learning을 전제로 하고 있기 때문에, 실제 환경과의 지속적인 interaction을 필요로 함. 하지만 개별 Action (정확히는 CRE Sequence)을 매번 실험실 환경에서 실험할 수는 없기 때문에 데이터를 통해 학습된 Reward Model을 대신 적용하여 학습을 구성. 하지만 Multi-stage learning의 특성 상 Reward model의 결함을 이용하는 Reward Hacking에 취약해질 수 있음. 본 연구에서는 Reward Hacking을 완화하기 위해 Transcription Factor Binding Site (TFBS) 값을 Regularization Term으로 추가해 생물학적으로 말이 되지 않는 Action에 대해 추가적인 페널티를 줌.

#### **시사점 및 제안 이유**

- 강화학습(RL)으로 gLM(뿐만 아니라 LLM, VLM 등)과 같은 Foundation Model을 학습시키는 것이 주목을 받고 있습니다. 유의미한 형태로 Scalable한 접근을 한 것을 살펴보면서, 앞으로의 Task를 해결해나갈 때 RL의 철학을 바탕으로 이해하기에 좋은 논문이라고 생각했습니다.
- 생물학적 특성 상 Multi-Objective (목적이 여럿인 상황, 예: 표적 세포와 비표적 세포에서의 발현율 차이) Setting이 중요한 과정이 많을 것인데, 이를 Constraint RL에서 Regularization을 적용해 Linear Scalarization과 Lagrangian multiplier를 통해 푸는 정석적이면서 깔끔한 접근이 흥미로웠습니다.
- 별도의 Reward Model을 함께 구현해, 실제 실험실 상호작용 없이도 Proxy를 통해 학습하는 등 Practical한 접근방법을 확인할 수 있어 Baseline을 구성할 때도 참고할 수 있을 것 같습니다.
