# 🪅 1st week — VCC 2026 (DipMind)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **정유민 (teammate)** · 📅 2026-08 → 09-06 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

## Virtual Cell Challenge 2026 — DipMind

익명 세포주 A/B/C의 비섭동 control 셀만으로 300개 CRISPRi 타겟의 반응을 예측한다.<br>완전 zero-shot — 챌린지 학습 세트는 없다.

**현재: validation 리더보드 30위 / 181팀 (KIMCHI-3, Overall +0.0876)**

### 문서

- 📄 [SUMMARY](08a_summary.md)

- 📄 [PROGRESS](08b_progress_day1.md)

- 📄 [DAY2](08c_day2.md)

### 한 문단 요약

대형 모델 학습(STATE)은 실패했다 — 학습 데이터가 0인 과제였다.<br>전환점은 **300개 타겟 중 272개가 Replogle K562 genome-wide 스크린에 이미 측정되어 있다**는 발견이었고,<br>이후는 그 값을 컨텍스트로 옮겨 적는 조회(retrieval) 방식이다.<br>오라클 분해 결과 점수의 **0.50은 소스/평균 반응, 0.21만이 방출 품질**이므로,<br>다음 한 수는 생성 모델이 아니라 **소스 확대**다.

