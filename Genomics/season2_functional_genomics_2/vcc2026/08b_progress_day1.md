# PROGRESS — VCC 2026 진행 기록 (day 1)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **정유민 (teammate)** · 📅 2026-08-24 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026 › 1st week*
>
> Sanitized: machine/account line and server paths removed.

---

## Virtual Cell Challenge 2026 — 진행 기록

작성: 2026-08-24 · 팀 DipMind

---

### 1. 현재 성적

| 제출 | 방식 | Rank | Overall |
|---|---|---|---|
| control-copy | 모델 없음, control 셀 복제 | — | (기록 없음) |
| KIMCHI-1 | STATE 학습 모델 | — | control-copy보다 낮음 |
| **KIMCHI-2** | 공개 스크린 실측 반응 조회 | **73** | **+0.0113** |

KIMCHI-2 지표 (스케일: 0 = 컨텍스트 평균, 1 = 실제 replicate):

| pds | mse | nmae | fid | reach | jac |
|---|---|---|---|---|---|
| +0.300 | 0 | +0.040 | **−0.326** | +0.075 | −0.021 |

KIMCHI-1 원시값 (참고): PDS 0.5(무작위) / MSE 192 / NMAE 2.643 / JAC 0.029 / FID 0.493 / REACH 0.080

---

### 2. 과제 정의

- **완전 zero-shot**. 챌린지 학습 세트 없음. 익명 세포주 A/B/C의 **비섭동 control 셀만** 주어짐
- 예측 대상: **300개 CRISPRi 타겟 × 400셀 × 3컨텍스트 = 360,000행 × 18,533 유전자**, raw 정수 카운트
- 채점: `cell-eval2` `vcc2026` 프리셋, 6개 지표의 참조 스케일 평균
- 최종 순위는 test set(10/22 공개, 컨텍스트 D/E/F, 다른 300개 패널)으로만 결정

---

### 3. 결정적 발견

#### 3.1 300개 타겟의 91%가 이미 공개 데이터에 측정되어 있다

처음에 essential 패널 4개 파일(Replogle-Nadig hepg2/jurkat/k562/rpe1, 2,396 섭동)만 확인하고<br><b>"300/300이 공개 스크린에 없다 → 일반화가 필수"</b>라고 결론지었다. <b>이것이 틀렸다.</b>

| 소스 | 섭동 유전자 | 300 타겟 커버 |
|---|---|---|
| K562 **genome-wide** (Replogle 2022 GWPS) | 9,867 | **272 (91%)** |
| K562 essential | 2,058 | 0 |
| RPE1 (essential만; genome-wide 없음) | 2,394 | 0 |
| HepG2 / Jurkat (Nadig) | 2,394 | 0 |

주최측은 **essential 패널**과 겹치지 않게 골랐을 뿐, genome-wide에는 대부분 있다.<br>이 발견 전까지 세운 ESM2 일반화 설계 전체가 불필요했다.

`data/gwps/K562_gwps_normalized_bulk_01.h5ad` (357 MB, figshare 20029387).<br>단세포 버전(65.8 GB)은 불필요 — pseudobulk면 충분하다.

#### 3.2 로컬 평가 도구가 실제 채점과 달랐다

`cell-eval` v1(`vcc` 프로파일, 3개 원시 지표)로 평가하다가, 실제 채점이<br>`cell-eval2`(`vcc2026`, 6개 참조 스케일 지표)임을 뒤늦게 확인했다.

**v1에는 log-FC 크기를 벌하는 지표가 없어** 모델의 최대 약점을 못 봤다.<br>같은 예측을 두 도구로 채점하면 결론이 뒤집혔다:

|   | v1 판정 | vcc2026 판정 |
|---|---|---|
| STATE vs control-copy | STATE 승 (DE 겹침 2.5배, discrimination +0.055) | **STATE 패** (−0.338 vs −0.045) |

`cell-eval2`는 GPU DE 백엔드 `gpudge`를 요구하며 CPU 폴백을 명시적으로 거부한다<br>(DE 수치가 조용히 바뀌기 때문).

#### 3.3 다른 세포주로의 전이 가능성 (실측)

같은 유전자 knockdown의 반응 상관:

| 비교 | 상관 |
|---|---|
| 같은 세포주, 반쪽씩 나눈 재현 (상한) | \~+0.65 |
| 같은 세포주(K562), 다른 스크린 (GWPS ↔ essential) | +0.29 |
| **다른 세포주, 같은 유전자** | **+0.13 \~ +0.27** |
| hepg2 ↔ rpe1 (둘 다 부착성 상피) | +0.27 |
| 혈액 계통 포함 쌍 | +0.13 |
| STATE 학습 모델 (zero-shot) | +0.056 |

**계통이 같으면 전이가 2배 잘 된다.** 그리고 아무 학습 없이 다른 세포주 값을 복사하는 것만으로<br>학습 모델의 2\~5배다.

#### 3.4 컨텍스트 fingerprint 매칭

control 프로파일(log CP10k) 상관:

|   | hepg2 | jurkat | k562 | rpe1 |
|---|---|---|---|---|
| 컨텍스트 A | 0.362 | **0.647** | 0.478 | 0.376 |
| 컨텍스트 B | 0.384 | 0.341 | 0.351 | **0.458** |
| 컨텍스트 C | 0.425 | 0.351 | 0.365 | **0.443** |

A는 혈액 계통, B·C는 상피 계통으로 보인다. 챌린지가 "여섯 세포주가 서로 다른 조직 유래"라고<br>밝힌 것과 부합.

**단, 현재 이 매칭은 무용지물이다** — 300개 타겟이 GWPS(K562)에만 있어 가중 평균할 대상이 없다.<br>가중치 0.554를 받은 jurkat이 실제 기여는 0이다.

#### 3.5 노이즈 바닥 (정답 없이 크기 보정하는 법)

컨텍스트 A의 46개 non-targeting 가이드(각 400셀)의 서로 간 변이:

```
가이드-평균 |delta| L1 중앙값 = 162.4     ← 순수 기술/생물 노이즈
KIMCHI-1 예측                = 1,024.2   ← 노이즈의 6.3배 (과대)
KIMCHI-2 예측                =   290.9   ← 1.8배 (적정)
```

정답이 없어도 예측 크기를 검증할 수 있는 기준. **진작 썼어야 했다.**

---

### 4. KIMCHI-2 구성 (현재 최선)

```
소스        K562 GWPS pseudobulk (z-score) — 실질적 단일 소스
값 변환     z-score 그대로 × 0.567
            (var['std']를 곱하면 상관 +0.29 → +0.09로 악화. 곱하지 말 것)
amplitude   1.0  (스윕 실측; 1.3은 nmae가 +0.014 → −0.229로 급락)
미커버 28개 generic response = 커버된 272개 반응의 평균
            (실제 반응과 상관 +0.141, "변화 없음"의 0보다 나음)
셀 생성     control 셀 400개를 각각 다르게 뽑아 같은 delta를 log 공간에서 적용
            → 셀-셀 상관 0.537 (실제 0.510)로 분포 재현
유전자      7,683개 예측 / 나머지 10,850개는 control 값 유지
```

#### amplitude 스윕 (K562 GWPS → Jurkat, 300 섭동)

|   | 0.5 | 0.75 | **1.0** | 1.3 |
|---|---|---|---|---|
| nmae | −0.007 | +0.017 | +0.014 | **−0.229** |
| fid | +0.192 | +0.324 | +0.425 | +0.513 |
| reach | +0.073 | +0.137 | +0.200 | +0.258 |
| jac | +0.041 | +0.048 | +0.040 | +0.026 |
| pds | +0.399 | +0.509 | +0.573 | +0.616 |
| **avg** | +0.116 | +0.173 | **+0.209** | +0.197 |

크기를 키우면 방향 지표(fid/reach/pds)는 계속 좋아지지만 nmae가 무너진다. 1.0이 균형점.

---

### 5. 홀드아웃이 실제보다 낙관적이었다

|   | 홀드아웃 예측 | 실제 |
|---|---|---|
| avg_score | +0.209 | **+0.011** |
| pds | +0.573 | +0.300 |
| fid | +0.425 | **−0.326** |

**fid가 부호까지 뒤집혔다.** 원인 후보:

1. **커버리지** — 홀드아웃 300/300, 실제 272/300
2. **플랫폼 차이** — 홀드아웃은 Jurkat control이라 소스와 동일 전처리(fingerprint r=0.86).<br>실제는 10x Flex vs Replogle 10x 3′ (r=0.35\~0.48)
3. **anchor 차이** — 실제 채점은 `vcc2026-valA/B/C-r4` 앵커를 쓰고, 우리 홀드아웃은<br>자체 생성한 앵커다. 스케일 자체가 다르다

이전에 저지른 같은 종류의 실수도 있었다: 2,000 유전자 공간에서 홀드아웃을 만들어<br>300개 타겟 중 65개만 target-gene 제외가 작동했고, 그래서 `pds_cosine`이 부풀려졌다.<br>(`cell-eval2`가 경고를 출력했는데 영향 크기를 과소평가했다.)

---

### 6. 버린 접근 — STATE 학습 모델

#### 구성

- SE-600M 동결 → `X_state` 2,058차원 basal 표현
- ST(State Transition) 116M 파라미터를 Replogle 3개 세포주 701,428셀로 학습
- 섭동 표현: ESM2 → 중심화·PCA 256 + control 채널 = 257차원 (300/300 조회 가능)
- 출력: 반응성 상위 2,000 유전자

#### 진단 결과 (`scripts/diagnose_deltas.py`)

|   | hepg2 (본 데이터) | jurkat (미지 세포주) |
|---|---|---|
| corr(실제, 예측) | +0.239 | +0.056 |
| 과대예측 | 2.26배 | 6.43배 |
| 모든 섭동에 공유되는 변화 | 58.1% | 68.0% (실제 9.3%) |

- <b>본 적 있는 데이터에서도 상한(+0.79) 대비 30%</b>에 그쳤다. zero-shot 이전에 학습·손실 설계가 문제.<br>분포 손실(energy)이 섭동 신호를 압도하는 것으로 보인다 — 실제 섭동 효과는 유전자당 0.04 수준인데<br>세포 간 변이가 훨씬 크다.

#### 시도한 개선과 결과

- 출력 유전자 8,783 → 2,000 반응성: 재현 가능 신호 +0.444 → +0.648 (**효과 있음**)
- `cell_set_len` 128 → 256, `decoder_weight` 1.0 → 3.0: hepg2 상관 +0.125 → +0.239
- 후처리 α 축소: v1 기준 역효과, vcc2026 기준 −0.338 → −0.034 (**도구에 따라 결론이 갈림**)

#### PRiMeFlow 검토 결과 — 전환하지 않음

- 섭동을 **compositional one-hot**으로 인코딩 (`Enc(c) = [∑ OneHot(p) || OneHot(cov)]`)
- 논문이 **미지 섭동·미지 세포타입 zero-shot을 주장하지 않음**. 평가도 2025년 과제(H1 한 세포주 안 few-shot)
- 핵심 차별점("사전학습 잠재공간 없이 유전자 공간 직접 모델링")이 우리 병목과 무관 —<br>측정 결과 SE 임베딩이 유전자 공간보다 **섭동 정체성을 더 잘 보존**한다<br>(자기일관성 corr 0.423 vs 0.267, top-1 검색 33.2% vs 32.2%)

---

### 7. 상위 팀 설명 해독 (10위권)

> "Eight-source full-axis STEER same-perturbation response consensus weighted by official<br>target-control fingerprints, amplitude 1.3, with frozen P1-v0 control draws, independent<br>count transport, and audit-only calibration. Selected by paired fast screening and exact<br>CUDA/gpudge confirmation across physically source-excluded CZI, K562-essential, and RPE1 contexts."

| 구절 | 해석 | 우리 상태 |
|---|---|---|
| same-perturbation response consensus | 같은 유전자의 실측 반응을 조회 | ✅ 구현 |
| eight-source | 8개 소스 합의 | ❌ 실질 1개 (K562 GWPS) |
| target-control fingerprints 가중 | control 프로파일 유사도로 가중 | ⚠️ 구현했으나 소스가 1개라 무용 |
| amplitude 1.3 | 효과 크기 전역 스케일 | ✅ 우리는 1.0이 최적 |
| frozen control draws | control 셀 추출 고정 | ✅ seed 고정 |
| independent count transport | 셀별 독립 카운트 변환 | ✅ |
| source-excluded 검증 | 소스 단위 통째 제외 | ⚠️ 세포주 단위로만 |

**가장 큰 격차는 소스 수다.** 8개 소스로 합의를 내면 fingerprint 가중이 실제로 작동하고<br>amplitude를 크게(1.3) 써도 안정적이다.

---

### 8. 다음에 시도할 것 (우선순위)

#### A. 소스 확대 — 가장 큰 격차

- 28개 미커버 타겟을 담은 소스 탐색 (scPerturb 18개 스크린 확인했으나 **0개 발견**)
- CZI CELLxGENE 섭동 데이터셋 (상위 팀이 "CZI" 언급)
- VCC 2025 H1 hESC 데이터 (챌린지 `vcc datasets`에는 controls만 제공됨)
- **같은 300개 타겟을 다른 세포주에서 측정한 소스**가 있으면 fingerprint 가중이 살아난다

#### B. fid가 −0.326인 원인 규명

홀드아웃에서 +0.425였는데 실제로 부호가 뒤집혔다. 6개 지표 중 유일하게 크게 음수라<br>여기만 고쳐도 Overall이 크게 오른다. `de_wilcoxon_direction_fidelity_yield_raw`의 정의를<br>`cell_eval2/catalog.py`에서 확인하고, 실제 컨텍스트에서 무엇이 다른지 진단할 것.

#### C. 홀드아웃을 실제 채점과 정렬

- 실제 anchor(`vcc2026-valA/B/C-r4`)와 우리 자체 anchor의 스케일 차이 확인
- 플랫폼 차이(10x Flex vs 10x 3′)를 모사할 방법

#### D. 컨텍스트별 amplitude

K562 유사도가 A=0.478, B=0.351, C=0.365로 다르다. 현재는 전 컨텍스트 1.0 고정.<br>근거 있는 외삽 방법을 찾으면 이득 가능.

#### E. 셀 수준 이질성

현재 400개 셀에 **동일한 delta**를 적용한다. 실제로는 섭동 효과 자체가 셀마다 다르다.<br>flow matching 계열(Altos Labs 2025 우승작)이 노리는 지점. 다만 현재 병목은 평균 반응의<br>정확도이므로 후순위.

---

### 9. 자산 목록

#### 데이터 (작업 서버)

```
controls/                 챌린지 validation 번들 (A/B/C + gene_names + pert_counts)
data/gwps/                Replogle pseudobulk 4개 (880 MB) ★ KIMCHI-2의 핵심
data/replogle_full/       Replogle-Nadig 원본 단세포 4개 세포주 (34 GB)
data/prepared/            8,783 유전자로 정렬한 4개 세포주 (raw counts)
data/se/                  위에 SE-600M X_state 부착 (42 GB)
data/se2k/                2,000 반응성 유전자로 축소
data/scperturb/           scPerturb CRISPR 스크린 18개 (300 타겟 커버 0)
data/retrieval_cache/     소스별 섭동 응답 캐시 (재실행 시 5분 → 즉시)
models/SE-600M/           SE 체크포인트 (12 GB)
runs/st_v1, st_v2/        STATE 학습 결과
submissions/kimchi2/      제출한 .vcc (3.3 GB)
eval/hold8k, eval/amp/    홀드아웃 + amplitude 스윕
```

#### 스크립트 (`scripts/`)

| 파일 | 역할 |
|---|---|
| `retrieval_predict.py` | **KIMCHI-2 본체.** 조회-합의 예측기 |
| `score_vcc2026.sh` | `cell-eval2` `vcc2026` 채점 (0/1 기준점 자동 생성) |
| `diagnose_deltas.py` | 섭동 특이 신호 vs 일반 이동 진단 |
| `make_submission.py` | 360,000행 스트리밍 조립 + 제약 검증 |
| `to_counts.py` | log1p 예측 → raw counts (18,533 공간 scatter) |
| `pad_contexts.py` | 컨텍스트를 400셀/섭동으로 패딩 |
| `align_context.py`, `subset_genes.py`, `prep_replogle.py` | 유전자 공간 정렬 |
| `build_pert_features.py` | ESM2 → PCA 섭동 특징 (STATE용) |
| `train.sh`, `run_inference.sh` | STATE 학습/추론 파이프라인 |
| `attach_controls.py` | 채점용 control 블록 부착 (제출본에는 넣지 말 것) |
| `baseline_predict.py` | control-copy 베이스라인 |

#### 재현 명령

```bash
source scripts/env.sh

# KIMCHI-2 재생성 (캐시 있으면 컨텍스트당 3~4분)
python scripts/retrieval_predict.py \
  --gwps data/gwps/K562_gwps_normalized_bulk_01.h5ad \
  --gwps-fingerprint data/prepared/k562.h5ad --gwps-scale 0.567 \
  --context controls/context_A.h5ad --context-name A \
  --perts controls/pert_counts.csv --genes controls/gene_names.csv \
  --n-cells 400 --amplitude 1.0 --uncovered generic \
  --output preds/retrieval_g/counts_A.h5ad

# 홀드아웃 채점
bash scripts/score_vcc2026.sh eval/hold8k <pred.h5ad> <tag>
```

---

### 10. 반복하지 말아야 할 실수

1. **공개 데이터 커버리지를 부분만 확인하고 결론짓기** — essential 패널 4개만 보고<br>"0/300"이라 단정, genome-wide를 놓쳐 전체 설계를 잘못된 전제 위에 세웠다
2. **채점 도구를 확인하지 않고 최적화** — `cell-eval` v1으로 며칠 최적화했는데 실제는 `cell-eval2`
3. **홀드아웃 유전자 공간을 채점 공간과 다르게 구성** — target-gene 제외가 65/300만 작동해<br>`pds_cosine`이 부풀려졌고, 그 상태로 제출을 권고했다
4. **도구 경고를 읽고도 영향 크기를 과소평가** — `cell-eval2`가 명시적으로 경고했다
5. **실행 중인 셸 스크립트 수정** — bash가 파일을 다시 읽어 파이프라인이 중단됐다
6. **리더보드 설명에 방법을 상세히 기재** — 공개된다는 점을 고려하지 않았다
