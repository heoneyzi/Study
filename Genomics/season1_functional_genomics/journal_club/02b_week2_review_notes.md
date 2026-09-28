# 저널 2 리뷰 — week-2 companion notes

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [Journal club](README.md)</sub>

> ✍️ **강지헌 (me)** · 📅 2026-02 (week 2) · 🗂️ Source: Notion — *Genomics › Genomics (1) — personal notes folder*

---

평가 gLM 모델 :

- Nucleotide Transformer
- DNABERT2
- HyenaDNA
- 인간 참조 genome으로 학습시킨 커스텀 GPN 모델

(단 모델은 전혀 수정하지 않고, 모델이 생성한 결과만을 가지고 평가함)

<b>*gLM 임베딩을 어떻게 사용하나요?</b>*<br><br>→ 각 gLM의 마지막에서 두 번째 층(penultimate layer)에서 임베딩을 추출 → 표준적 관행<br>(왜냐하면 마지막 층은 너무 Task Specific적임)<br><br>1. 서열 전체 정보를 요약하기 위해 <b>*분류 토큰(CLS)</b>* 과 mean embedding을 사용<br><br>2. 추출된 임베딩을 받아 선형모델(Ridge)나 <b>*MLP</b>* 혹은 <b>CNN(</b>요약된 정보뿐만 아니라 임베딩 전체를 분석하기 위해서)까지 사용해 베이스라인 형성

VS

비교 모델:

- 전통적인 One-hot encoded CNN 방식
- 레이블이 있는 데이터로 학습된 지도학습 기반 파운데이션 모델 (Sei, Enformer 등)
- 해당 데이터셋에 맞춰 One-hot 서열로 처음부터(From Scratch) 학습시킨 지도학습 모델

<details>
<summary><b>코멘트</b></summary>

- gLM의 불확실성 + 연구의 불확실성
- S2F 모델에서도? <br>최신모델도 마찬가지일까?<br>Evo-2 랑 Alphagenome의 위치는? 물량공세의 승리?
- down stream (cell specific한) task에 대한 모델의 변화는 필수 → 효율적인 학습?  모델 단에서 효율적으로 건드릴 수 있을까?

</details>
