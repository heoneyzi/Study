# [유민] Rapid directed evolution guided by protein language models and epistatic interactions

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **정유민 (teammate)** · 📅 extra proposal (2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 기타 · — not selected · 읽고 싶어요: 유민

---

[https://www.science.org/doi/10.1126/science.aea1820](https://www.science.org/doi/10.1126/science.aea1820)

Patrick Hsu팀의 EvolutionaryScale출신 연구자들이 science에 3일전에 발표한 논문입니다.

#### **한 줄 요약**

소수의 double mutant 데이터만으로 고차 조합 변이의 epistasis를 학습해 단백질 기능을 향상시킨 combinatorial ML 설계 전략 (PLM 기반 후보 선별을 활용한다는 점에서 EVOLVEpro와 유사하나, double mutant screening을 통해 상호작용을 직접 모델링한다는 점이 차별점).

#### **방법 요약**

Protein language model로 유망한 single mutation 후보(n ≈ 15)를 선별한 뒤, 해당 후보들의 double mutant를 실험해 비선형 상호작용(epistasis)을 학습합니다. 이후 one-hot 기반 회귀 모델을 사용해 3개 이상 고차 조합 변이의 기능을 예측하고 최적 조합을 선택하였습니다.

#### **결과**

- APEX 효소에서 최대 256배 기능 향상, 항체에서는 발현과 결합력을 동시에 개선하는 데 성공
- 수백 개 수준의 데이터로 고차 epistasis를 외삽할 수 있음을 보임
    - 논문 曰: 8\~12 mutant까지 extrapolate 가능함
- Epistasis 모델링에는 언어모델 임베딩보다 one-hot 형식의 단순한 입력이 더 효과적임
- 코드 및 webapp 제공

#### 시사점 & 읽어야 할 이유

- 효과 있는 mutation discovery 목적으로 PLM likelihood 활용하는 것이 매우 효과적이다
- Protein engineering 논문이지만, 생물학적 실험 oracle과 ML을 결합한 시도라는 점에서 functional genomics와 연결되고 흥미로움
    - ClinVar multimutant 변이 해석에 비슷한 방법 적용해볼 수 있을 것 같음
- 최종 combinatorial ML 설계 과정에서 One-hot encoding이 ESM embedding을 활용하는 것보다 더 효과적이었음 → low N setting에서는 간단한 모델이 더 유리함을 보여주는 또다른 예시
- gLM에서도 거의 비슷한 방법을 적용할 수 있을 것 같은데 이에 대해 고민해보는 것도 좋을 것 같음.
- YAICON에서 활용한다면, 특정 단백질 하나 정하고, ESM을 이용해서 candidate뽑아서 실제 실험해보는 것은 어떨까 함(우리 연구실에서)

아래는 Patrick Hsu 인용

> The process of scientific research is fundamentally a search problem, and we basically do guess and check. We've trained predictive models of biology, like our Evo series of DNA language models, to learn the evolutionary constraints on biological sequences. Such models learn a fitness landscape of what evolution has explored. But the fitness landscape is not the same as the function you actually care about: whether an enzyme catalyzes faster, whether an antibody binds tighter, whether a CRISPR tool edits better. The core question is how do you connect the knowledge of these models to the functional search that has to happen in the physical lab?
