# [민선] Highly accurate protein structure prediction with AlphaFold (or AlphaFold 3)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **구민선 (teammate)** · 📅 week-3 proposal (Feb 2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 3주차 · — not selected · 읽고 싶어요: 민선

---

[https://www.nature.com/articles/s41586-021-03819-2](https://www.nature.com/articles/s41586-021-03819-2)<br>(또는 보다 최근 논문: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12342994/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12342994/))

**\[한 줄 요약\]**

MSA와 템플릿 정보를 통합하는 새로운 딥러닝 아키텍처(Evoformer + structure module)를 설계하여, 단일 아미노산 서열로부터 거의 실험 수준(평균 1Å대) 정확도의 3D 단백질 구조를 end-to-end로 예측하는 방법을 제시한 연구입니다.

**\[시사점 및 제안 이유\]**

앞에서 읽었던 gLM 논문들과 함께 보면

- gLM: 서열 → representation (주로 1D 상관/grammar 학습)
- AlphaFold: 서열 + MSA → 3D geometry 예측

이라는 대비를 통해, 서열로부터 구조 및 기능 정보를 서로 다른 수준에서 어떻게 추출하는지 비교해볼 수 있을 것 같습니다.

특히 3D level에서 구조를 직접 예측한다는 점에서, sequence-based 모델과 구조 기반 모델의 차이를 이해하는 데 도움이 될 것 같습니다.

또한 최근 개인적으로 읽은 면역 관련 논문에서 ligand–receptor interaction의 bonding strength와 구조적 안정성을 분석할 때 AlphaFold를 활용한 사례를 보았는데, 실제 연구 응용 측면에서도 의미가 있을 것 같아 제안드립니다.
