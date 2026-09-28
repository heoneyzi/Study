# 중간보고서 — midterm report (2026-02-03)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [Meetings](README.md)</sub>

> 👥 **FG season-1 team** · 📅 2026-02-03 · 🗂️ Source: Notion — *Functional Genomics › Meeting Notes*
>
> 🔁 Duplicate in Notion, not reproduced: *Genomics (1) › 중간보고서* (earlier draft with to-do comments to teammates).

---

#### 1. 프로젝트 개요

본 프로젝트는 염기서열에서부터 생명 현상으로 이어지는 Functional Genomics을 딥러닝과 접목하기 위하여 단계적으로 연구를 수행합니다. Central Dogma에 대한 이론적인 지식을 바탕으로 연구 초기 단계에서는 단백질 기능 예측 챌린지인 CAFA 6에 참여해보며, 모달리티의 특수성과 관련 모델의 파이프라인으로 이루어지는 플로우를 따라가면서 실전 감각을 익힙니다. 프로젝트의 중반 단계에서는 Functional Genomics에 대한 전반적인 연구의 흐름을 파악하고, 다양한 리서치를 알아보고 서로 설명하는 시간을 가지며 이론적 바탕과 풍부한 관점을 가질 수 있도록 합니다. 프로젝트의 최종 목표는 Virtual Cell Challenge와 같이 단백질을 넘어 유전자 수준의 변이와 발현을 예측하는 유전자 관점의 챌린지로 영역을 확장하고자 합니다.

저희는 다양한 챌린지 경험과 리서치를 통합하여 Functional Genomics 분야에서 독창적이고 고도화된 분석 방법론을 구축하는 것을 최종 목표로 합니다.

---

#### 2. 프로젝트 배경 (Introduction)

생명체의 설계도인 DNA가 RNA로 전사되고 단백질로 번역되어 실제 기능을 수행하기까지의 과정인 Central Dogma는 현대 생명과학의 핵심으로 볼 수 있습니다. 최근 AI 기술의 발전으로 AlphaFold와 ESM 등 다양한 모델이 등장하고 생명 현상에 대한 예측에서 발전을 일으켰으나, 여전히 복잡한 세포 환경 내에서의 단백질 기능과 유전자 간의 상호작용을 완벽히 해석하는 것에는 한계가 존재합니다.

특히 최근에 대두되는 Single Cell 데이터와 같이 노이즈가 많고 복잡한 데이터를 다루기 위해서는 단순한 모델 적용을 넘어서, 또다른 견고한 파이프라인이 필수적입니다. 저희 팀은 단백질부터 시작해 유전자까지 연구의 시각을 넓힘으로써, 생명 정보의 흐름을 통합적으로 이해하고 이를 예측할 수 있는 기술적 기반을 마련하고자 합니다.

---

#### 3. 프로젝트 계획

프로젝트는 크게 네 단계로 구성되며, 실전 경험과 이론적 깊이를 동시에 확보하기 위한 방향성으로 구성했습니다.

| 계획 | 기간 |
|---|---|
| **Central Dogma 이해 및 방향성 수립** | 1주차 |
| **CAFA 6 챌린지 수행** | 2주차 - 4주차 |
| **저널 클럽 및 관련 연구 리서치** | 5주차 - 7주차 |
| **새로운 챌린지 도전 및 파이프라인 구성** | 8주차 이후 (다음 분기까지 연장 예정) |

1. **Central Dogma 이해 및 방향성 수립:** 챌린지 수행에 앞서서 프로젝트의 방향성을 수립하고, 함께 Central Dogma에 대한 공부를 하며 챌린지에 참여할 수 있는 최소한의 준비를 합니다.
2. <b>CAFA 6 챌린지 수행:</b> 프로젝트의 시작과 동시에 2월 초 종료되는 <b>CAFA 6 </b>챌린지에 참여합니다. 이는 바이오 데이터셋의 모달리티를 빠르게 파악하고, 전체 프로세스를 단기간에 경험하여 연구의 감을 잡는 것을 목적으로 합니다. <br>단백질 기능 주석(Annotation) 예측을 위해 다양한 모델을 벤치마킹하고, 사용해보여 우리 팀만의 앙상블 기법이나 최적화 전략을 적용하기 위해 노력합니다.
3. **저널 클럽 및 관련 연구 리서치:** 챌린지 수행과 병행하여 최신 Functional Genomics 논문들을 함께 읽고 공유하며 전반적인 이해도를 올립니다. 또한 모델의 아키텍처뿐만 아니라 전체적인 연구의 흐름을 비판적으로 검토하며, 현재 기술의 한계점과 개선 가능성을 모색합니다.
4. **새로운 챌린지 도전 및 파이프라인 구성:** 앞서 습득한 관점을 통해서 유전자 수준의 변이 데이터셋(예: 벌크셀/싱글셀 발현량 예측 등)에 적용합니다. 이를 통해 단백질과 유전자를 아우르는 통합적인 시각을 확보하고, 저희 팀만의 연구 방법론을 설계하여 최종적인 연구 성과를 도출합니다.

---

#### 4. 활용 데이터 및 출처

현재 CAFA 6에서 사용한 데이터셋은 단백질 서열 데이터 및 Gene Ontology(GO) 레이블입니다.

출처: [CAFA 6 Protein Function Prediction](https://www.kaggle.com/competitions/cafa-6-protein-function-prediction/data)

---

#### 5. 진행상황 : 0, 1

#### Trials

[[윤진] 코드 1차 시도](../cafa6/05_yoonjin_code_attempt1.md)

[[수빈] CAFA6 시도](../cafa6/07_subin_cafa6_jepa.md)

---

> 📎 첨부였던 *CAFA 6 데이터셋* 페이지는 강지헌의 [데이터셋 정리](https://github.com/heoneyzi/Medical/blob/main/CAFA6/notes/01_dataset.md) 노트와 같은 내용입니다 (identical copy, not duplicated).
