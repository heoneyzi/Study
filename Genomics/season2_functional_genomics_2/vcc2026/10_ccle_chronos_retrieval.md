# CCLE & Chronos — retrieval + transfer

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **김민석 (teammate)** · 📅 2026-09 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

## VCC2026 — Retrieval + Transfer 접근 요약

Perturb-seq 소스는 Replogle 2종(K562, RPE1)만 사용 (팀 내 다른 모델과 DB 규모를 맞추기 위한 의도적 제약).

### 핵심 아이디어

- 300개 타깃 대부분이 이미 다른 세포주에서 CRISPRi로 측정돼 있다는 전제로, "예측"이 아니라 "조회 후 이식"으로 모델 구성.
- 학습 파라미터는 수십 개 수준으로 최소화하고, **무거운 지식은고정 DB 조회로 조달.**

**핵심 arm 4개:**

1. **Delta transfer** — K562/RPE1의 (perturbed − control) 패턴을 공유 저차원 방향으로 뽑아서,<br>타깃 세포주의 control에 그 방향만 이식 (절대 발현값은 절대 안 씀).
2. **CCLE 기반 context 라우팅** — 타깃의 control profile을 CCLE 전체(\~1,400 라인)와 상관시켜,<br>Perturb-seq가 아예 측정 안 한 라인에도 "이 라인이 K562/RPE1 중 어디에 더 가까운가"를 추정. Perturb-seq DB와 완전히 직교하는 정보원이라는 게 포인트.
    - training dataset에 없는 zero-shot cell line에서도 known seq data matching을 하려고 도입해보았음
3. **DepMap Chronos 기반 크기 보정** — 이식할 방향은 정해졌는데 "얼마나 세게"는 별도 문제라, 유전자 essentiality(Chronos)로 크기를 회귀 보정.
4. **Self-knockdown 하한선** — 위 세 개가 다 실패해도, 타깃 유전자 자기 자신의 잔여 발현 하향만은 항상 적용. 가장 싸고 확실한 신호.

### 내부 검증에서 본 것

- 자기 자신 knockdown만 넣는 것(arm 4) 대비, 방향 이식(arm 1+2)을 더하면 판별력 계열 지표가 큰 폭으로 개선 (수십\~수백 배).
- 대신 발현 오차(MSE)는 같이 나빠짐 — **방향은 맞는데 유전자 단위 정밀도는 떨어진다**는 패턴이 일관되게 재현됨.
- 크기 보정(arm 3)을 얼마나 강하게 반영할지(전역 배율 α)를 스윕해보면, 판별력 이득과 MSE 손해가 트레이드오프 관계 — α를 낮출수록 손해 없이 이득만 취하는 구간이 있음.
- 이 트레이드오프는 내부 검증 세포 수(통계 검정력)를 4배 늘려도 거의 그대로 — 샘플링 문제가 아니라 진짜 구조적 패턴으로 보임.

### ⚠️ 가장 중요한 발견 — 내부 검증이 실제 채점을 예측 못 했음

- 내부적으로 가장 좋아 보였던 설정으로 실제 제출했더니 **리더보드에서 정반대로 나쁨** (판별력 지표가 내부 예측과 부호까지 반대). 원인을 여섯 가지 각도(부호 오류, self-knockdown 크기, 유전자 순서, perturbation 간 예측 다양성, 통계 검정력, 타깃-소스 유사도)로 다 확인했는데 **전부 정상 — 명확한 버그를 못 찾음.**
- 특히 "타깃이 소스와 안 닮아서 실패했다"는 가설도 기각됨: 실제 채점 라인들이 우리가 내부 검증에 쓴 held-out 라인보다 CCLE 기준으로 딱히 더 낯설지 않았음. 즉 **단일 held-out 라인 검증이 좋아 보여도 실제 미지 라인 일반화를 보장하지 못한다**는 게 이번 스프린트의 제일 큰<br>교훈. 원인은 아직 미궁 — 조합형이 아닌 완전히 다른 계열의 두 번째 held-out 라인(iPSC 유래 데이터 확보해둠)으로 재현되는지가 다음 확인 대상.

### 다른 모델에 붙여볼 만한 것

- **CCLE 라우팅**: 어떤 아키텍처든 거의 공짜로 붙일 수 있는 직교 정보원. 우선순위 1.
- **Self-knockdown 하한선**: 없다면 가장 저비용 고효율.
- **크기를 고정 상수로 두지 말 것**: 우리도 이번에 실패로 배운 것 — 타깃별 신뢰도에 따라<br>이식 강도를 조절하는 구조가 필요한데, "CCLE 유사도"가 그 신뢰도 신호로 충분하진 않았음<br>(검증됨). 더 나은 신호가 뭔지는 열린 문제.
- **위 미해결 이슈 때문에, 우리 내부 숫자를 그대로 신뢰하지 말고 자체 held-out으로 재검증 후 채택 권장.**

### 개인 감상평?

- 분명 Null → Known-seq delta shift → adjust magnitude of the shift 순으로 하면 될 것 같은데.. Replogle 내 ablation study에서는 known을 판단하는 CCLE, magnitude 판단하는 Chronos 모두 유용했는데 실제로는 그렇지 않았음. 이게 CCLE, Chronos 외의 baseline 모델의 성능이 낮아서인지는 이전 좋았던 KIMCHI model line에 붙여보면 알 수 있지 않을까 함..

---

> 🗂️ Meeting notes that were nested under this page: [VCC 2025 review](../sessions/04_vcc2025_review_2026-08-15.md) · [VCC 2026 kick-off](../sessions/05_vcc2026_meeting1_2026-08-22.md) · [mid-challenge review](../sessions/06_vcc2026_direction_meeting_2026-09-06.md).
