# [수빈, 민선] Advancing regulatory variant effect prediction with AlphaGenome

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **박수빈 · 구민선 (teammates)** · 📅 week-1 proposal (Feb 2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 1주차 · — not selected · 읽고 싶어요: 수빈, 민선, 지헌, 윤진
>
> ➡️ AlphaGenome was covered later in [week 5](../05_week5_alphagenome.md).

---

[https://www.nature.com/articles/s41586-025-10014-0](https://www.nature.com/articles/s41586-025-10014-0)

#### 민선 작성

논문 후보2 (Advancing regulatory variant effect prediction with AlphaGenome) 내용:

- 유전자 발현, RNA splicing 패턴, transcription factor binding 등 다양한 functional genomic feature를 하나의 딥러닝 모델에서 동시에 예측하는 모델 + 실제 적용 사례 (질병 발생 메커니즘 예측)를 설명하는 논문입니다.
- (특히 regulatory variant effect prediction (non coding 유전체 변이가 유전자 발현 조절에 미치는 영향 예측) 성능이 좋음 -\> 질병 연관 변이의 대부분이 non-coding 영역에 존재한다는 점에서 중요한 의의를 가짐)

선정 이유:

- CAFA 6에서 다루는 단백질 기능 예측 문제를 세포 유형&조절 맥락과 연결해 생각할 수 있어 CAFA 6 프로젝트와 이어지는 논문이라고 생각하여 가져왔습니다.

#### 수빈 작성

\[저널클럽 1주차\] 후보 2 - DeepMind long context GLM AlphaGenome

- 논문 제목 : Advancing regulatory variant effect prediction with AlphaGenome
- DeepMind가 제안한 통합 DNA sequence 모델로, 1Mb DNA 컨텍스트를 입력으로 받아 발현/접근성/히스톤마크/TF 결합/3D contact/splicing 등 다양한 functional genomics modality를 단일 모델로 예측하는 방향을 제안함
- 현재 동향을 이해하기 위해서는 significant 한 SOTA 모델이 어떻게 구현되었는지에 대한 이해가 도움이 될 것 같았습니다.
