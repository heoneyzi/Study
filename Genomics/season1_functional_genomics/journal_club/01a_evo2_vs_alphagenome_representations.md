# 둘이 뭐가 다른데? — Evo 2 vs AlphaGenome representations

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [Journal club](README.md)</sub>

> ✍️ **sub-page of 조윤진 (teammate)'s week-1 notes** · 📅 2026-02 · 🗂️ Source: Notion — *Functional Genomics › 개인 아카이브 › [저널클럽 1주차] GLM survey*

> [!NOTE]
> 🤖 **AI-generated answer (ChatGPT) pasted for reference** — kept because it is part of the team notes; it is not the team's own writing.

---

아주 좋은 질문이야.

핵심은 이거야:

> Evo2는 **P(sequence)** 를 학습하는 모델인데,
> 그 내부 hidden representation은 도대체 “무엇을 의미하느냐?”

이걸 수학적·생물학적·표현학습 관점에서 나눠서 설명해볼게.

---

## 🧬 1️⃣ Evo2는 무엇을 학습했는가?

Evo2는 autoregressive objective로 학습됨:

$$
\log P(x_t \mid x_{<t})
$$

즉 모델은:

- “이 문맥에서 다음 염기가 무엇이 자연스러운가?”
- “어떤 패턴이 자주 공존하는가?”

를 배움.

그럼 representation은 무엇을 담을까?

---

## 🧠 2️⃣ Representation의 수학적 의미

AR 모델의 hidden state (h_t)는:

$$
h_t \approx \text{minimal sufficient statistic of } x_{<t}
$$

즉,

> 과거 서열의 정보를 “다음 염기 예측에 충분한 형태”로 압축한 것

중요한 점은:

- **완전한 과거 복제본이 아님**
- 예측에 불필요한 정보는 버림
- 통계적으로 의미 있는 구조만 남김

---

## 🧬 3️⃣ 생물학적으로 무엇이 남을까?

다음 염기 예측에 중요한 것들:

#### ① Codon 구조

- 3bp periodicity
- reading frame
- synonymous/non-synonymous constraint

#### ② TF motif 패턴

- 특정 motif 뒤에 오는 염기 분포
- motif cluster 구조

#### ③ CpG 통계

- methylation 관련
- CpG depletion 패턴

#### ④ Long-range correlation

- enhancer-promoter 통계적 공존
- GC content domain
- isochores

#### ⑤ Evolutionary constraint

- 보존된 영역에서 낮은 entropy
- 변이 허용 영역에서 높은 entropy

즉 Evo2 representation은:

> “게놈이 진화적으로 만들어낸 통계 구조”

를 담고 있어.

---

## 🔬 4️⃣ AlphaGenome representation과의 차이

|   | Evo2 | AlphaGenome |
|---|---|---|
| representation 의미 | sequence distribution 압축 | functional signal 압축 |
| 학습 목표 | 다음 염기 | ATAC/ChIP 등 |
| 포함 정보 | 진화 통계 | 실험적 기능 |
| cell-type specificity | 암묵적 | 명시적 |

Evo2는:

- “이 서열이 자연스러운가?”
- “이 패턴이 자주 등장하는가?”

AlphaGenome은:

- “이 서열이 열려 있는가?”
- “이 TF가 붙는가?”

---

## 📊 5️⃣ Information-theoretic 관점

Evo2 representation은 대략:

$$
h_t \approx I(x_{<t}; x_t)
$$

즉,

다음 염기를 예측하는 데 필요한 mutual information을 보존하는 표현.

그 결과:

- 높은 보존 영역 → 낮은 entropy
- 변이 허용 영역 → 높은 entropy

---

## 🧬 6️⃣ 그럼 Variant effect에서 representation은 무엇을 의미하나?

SNP 하나가 바뀌면:

- 그 위치의 local hidden state 변화
- 이후 위치들에 cascading effect

representation 변화는:

> “이 변이가 게놈의 통계적 구조를 얼마나 깨는가”

를 반영한다.

---

## 🧠 7️⃣ 직관적 비유

Evo2는:

- 게놈을 “언어”처럼 읽고
- 문법과 통계 구조를 학습한 모델

representation은:

> 문장의 “문법적 구조 요약”

AlphaGenome은:

> 문장이 실제로 “무슨 기능을 하는지” 요약

---

## 🔥 중요한 통찰

Evo2 representation은:

✔ 진화적 constraint

✔ motif 통계

✔ coding 압력

✔ long-range GC 구조

를 담지만,

❌ 특정 세포에서 enhancer가 켜지는지 직접 담지는 않음.

---

## 🧬 8️⃣ 한 줄 정의

> Evo2의 representation은 “게놈 언어의 통계적·진화적 구조를 예측에 충분한 형태로 압축한 잠재 상태”다.

---

원하면 다음을 더 깊게 파줄 수 있어:

- 왜 AR representation은 coding region에서 특히 강한가
- 왜 regulatory element에서는 한계가 생기는가
- Evo2 representation을 downstream task에 어떻게 fine-tuning하는가
- multi-species 학습이 representation을 어떻게 더 진화적으로 만드는가

어디까지 들어가볼까?
