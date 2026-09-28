# 하윙 — Stack context-transfer test

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **김서진 (teammate)** · 📅 2026-09 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

Stack: 다른 세포 context에서 관찰된 perturbation 결과를 prompt로 주고, 새로운 세포 context의 control cell에 그 perturbation 효과를 transfer하는 모델

공식 pretrained checkpoint를 받아서 RTX 3090에서 inference를 돌렸고, T=1이랑 T=5 iterative generation 둘 다 정상적으로 동작하는 걸 확인 → 공식 Belinostat 예제로 평가해보니 T=5가 전반적으로 perturbation delta를 더 잘 맞추는 편이었는데, 실제보다 DE gene을 많이 예측하는 경향도 확인

VCC validation 데이터도 받아서 제출 형식까지 맞췄고, 아무 perturbation 효과를 주지 않는 control baseline을 공식 서버에 제출해서 전체 파이프라인이 정상적으로 동작하는 것도 확인

⇒ baseline의 Overall score는 -0.312

이후에 Stack 하나만이 아닌 public CRISPRi 데이터를 이용해볼려고 함

→ 같은 target gene의 perturbation effect가 여러 cell context에 있으면, VCC의 context와 가장 비슷한 source context를 찾아서 그 effect를 transfer하도록 할 예정

- Stack의 context transfer
- 여러 public context의 perturbation delta
- low-rank나 linear model
- unseen target을 위한 gene embedding

Stack이 DE gene을 너무 많이 예측하는 문제 → 마지막에는 effect size와 DE gene 수를 calibration하는 과정도 추가할 예정
