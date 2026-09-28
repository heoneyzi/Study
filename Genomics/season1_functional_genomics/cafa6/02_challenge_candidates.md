# Challenge — 후보 대회 비교 (CAGI7 · CAFA 6 · VCC · DREAM)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [CAFA 6](README.md)</sub>

> ✍️ **조윤진 (teammate)** · 📅 ≈ 2026-01 (kick-off) · 🗂️ Source: Notion — *Functional Genomics › 개인 아카이브 › 프로젝트 방향성*

---

### 1. CAGI7 RGP-CRAM Challenge (불가, 기관승인 필요)

[https://genomeinterpretation.org/cagi7-rgp-cram.html](https://genomeinterpretation.org/cagi7-rgp-cram.html)

| 항목 | 내용 |
|---|---|
| **챌린지명** | CAGI7 Rare Genomes Project - CRAM |
| **주최기관** | Critical Assessment of Genome Interpretation (CAGI), Broad Institute, Rare Genomes Project |
| **개최 시기** | • 챌린지 오픈: 2025년 12월 27일• 제출 마감: 2026년 3월 31일 |
| **주요 태스크** | • 희귀질환 환자의 CRAM 파일(short-read 게놈 시퀀싱 데이터)에서 원인 변이 식별<br>• 예제 세트: 4명의 solved 환자<br>• 테스트 세트: 20명의 solved/unsolved 환자 혼합<br>• SNV, INDEL, 구조변이, 미토콘드리아 변이, 탠덤반복 확장 등 다양한 변이 유형 포함<br>• HPO(Human Phenotype Ontology) 기반 표현형 데이터 제공<br>• 최대 100개의 후보 변이 제출 가능<br>• EPCR(Estimated Probability of Causal Relationship) 값 포함 필요 |
| **데이터 규모** | • 총 24명의 proband (예제 4명 + 테스트 20명)<br>• 30x depth Illumina 시퀀싱<br>• GRCh38 참조 게놈<br>• CRAM 파일 형식 (압축된 alignment 데이터) |
| **참여 방법** | 1. CAGI 웹사이트 등록 (genomeinterpretation.org)<br>2. Synapse 플랫폼 계정 생성<br>3. **중요**: 기관 서명이 필요한 Data Use Agreement 제출<br>4. Terra 플랫폼에서 암호화된 데이터 다운로드<br>5. 승인 후 복호화 비밀번호 수령 (PGP, Signal 등 암호화 통신)<br>6. Synapse에 예측 결과 제출• 팀당 최대 6개 모델 제출 가능 |
| **경쟁 규모** | • 글로벌 챌린지 (전세계 참여 가능)<br>• CAGI6 RGP 챌린지는 수십개 팀 참여 (정확한 CAGI7 참여팀 수는 진행 중이라 미공개)<br>• 개인 및 연구기관 모두 참여 가능 |
| **평가 기준** | • True positive 변이의 순위 기반 가중 점수<br>• EPCR 값을 활용한 sensitivity, specificity, PPV 평가<br>• 상위 팀의 unsolved 케이스 재검토 (EPCR ≥0.1)<br>• 독립 평가자에 의한 블라인드 평가 |
| **상금/혜택** | • 상금 정보 미공개<br>• 우수 팀은 RGP 팀과 공동으로 논문 출판 기회<br>• Unsolved 케이스에서 새로운 진단 발견 가능 (CAGI6에서 2건 성공)<br>• 환자에게 결과 환원 가능성 |
| **특이사항** | • 제한된 접근: 미국 수출통제법 적용, 특정 국가 제외<br>• 각 데이터 접근자마다 별도 기관 서명 필요<br>• 승인 과정 수일\~수주 소요• 윤리적 고려: 2차 소견 제출 금지, 챌린지 종료 후 데이터 삭제 필수<br>• RGP-VCF 챌린지와 동일 승인으로 참여 가능 |
| **권장 도구** | • Variant calling: GATK HaplotypeCaller, DeepVariant, DRAGEN<br>• 미토콘드리아: Mutect2• 구조변이: Manta, DELLY, Lumpy, GATK-SV<br>• 탠덤반복: GangSTR, ExpansionHunter |

---

### 2. CAFA 6 Protein Function Prediction

[https://www.kaggle.com/competitions/cafa-6-protein-function-prediction/data](https://www.kaggle.com/competitions/cafa-6-protein-function-prediction/data)

| 항목 | 내용 |
|---|---|
| **챌린지명** | CAFA 6 (Critical Assessment of protein Function Annotation algorithms) |
| **주최기관** | Iowa State University, Northeastern University, UniProt, ISCB |
| **개최 시기** | • 등록 시작: 2025년 10월 16일<br>• 등록 마감: 2026년 1월 26일<br>• 최종 제출 마감: 2026년 2월 2일<br>• 결과 평가: 2026년 이후 (실험 데이터 축적 기간 필요) |
| **주요 태스크** | • 단백질 아미노산 서열로부터 생물학적 기능 예측<br>• Gene Ontology(GO) 용어로 기능 주석  - Molecular Function (MFO): 분자 수준 활동  - Cellular Component (CCO): 세포 내 위치  - Biological Process (BPO): 생물학적 프로세스<br>• Human Phenotype Ontology (HPO) 예측 포함<br>• Time-delayed evaluation: 제출 후 실험 데이터가 축적되면 평가 |
| **데이터 규모** | • 대규모 단백질 서열 데이터셋<br>• GO 데이터베이스 (약 40,000개 용어)<br>• 다양한 종(species)의 단백질 포함<br>• 학습 데이터: train_sequences.fasta, train_terms.tsv |
| **참여 방법** | 1. Kaggle 플랫폼 가입<br>2. 대회 페이지에서 규칙 확인 및 데이터 다운로드<br>3. 모델 개발 및 학습<br>4. Kaggle에 예측 결과 제출<br>• 개인 또는 팀(최대 인원 제한 있음) 참여 가능 |
| **경쟁 규모** | • **대규모 글로벌 챌린지**• CAFA5 Kaggle 대회: 수천 팀 참여<br>• CAFA6도 유사한 규모 예상• 학계, 산업계, 개인 연구자 모두 참여 |
| **평가 기준** | • Modified F1-metric (CAFA-metric)<br>• Information Accretion (IA) 가중치 적용<br>• 각 ontology별 개별 평가 후 평균<br>• Precision, Recall, Fmax 종합 평가<br>• 희귀하고 어려운 GO 용어에 더 높은 가중치 |
| **상금/혜택** | • **총 상금: \$50,000<br>**• 우수 팀은 Nature 등 저명 학술지 공동 논문 게재<br>• ISMB/CAFA 워크샵 발표 기회<br>• 단백질 기능 예측 분야 벤치마크 확립 |
| **특이사항** | • Kaggle 플랫폼 사용으로 접근성 높음<br>• 시계열 챌린지: 예측 후 실제 실험 결과로 평가<br>• 평가 기간이 길어질 수 있음 (2024년까지 소요 가능)• 2-3년 주기로 개최되는 정기 챌린지<br>• CAFA 역사: CAFA1(2010), CAFA2, CAFA3(2016-2017), CAFA4, CAFA5(2023), CAFA6(2025-2026) |
| **권장 접근법** | • Protein Language Models: ESM-2, ProtT5, ProtBert, Ankh<br>• Ensemble 방법론• 서열, 구조, 발현 프로파일, 상호작용 데이터 통합<br>• BLAST-KNN, InterPro 등 전통적 방법과 딥러닝 결합 |

---

### 3. Virtual Cell Challenge 2025 (2026 중반에 열릴 것 예상)

[https://virtualcellchallenge.org/#timeline](https://virtualcellchallenge.org/#timeline)

| 항목 | 내용 |
|---|---|
| **챌린지명** | Virtual Cell Challenge (Inaugural 2025) |
| **주최기관** | Arc Institute |
| **개최 시기** | • **이미 종료됨** (2025년)<br>• 리더보드 제출: 2025년 10월 27일까지<br>• 최종 제출: 2025년 11월 3일• 우승자 발표: 2025년 (완료)<br>**2026년 챌린지 예상**:• Arc는 매년 반복 개최 2026년도 유사 일정 예상 (6-7월 시작) |
| **주요 태스크** | • H1 hESC(인간배아줄기세포)에서 유전자 교란(CRISPRi) 효과 예측<br>• 300개 유전자 perturbation의 전사체 반응 예측<br>• Few-shot learning 챌린지: 새로운 세포 컨텍스트에 대한 일반화<br>• 리더보드: 50개 perturbation<br>• 최종 평가: 100개 perturbation |
| **데이터 규모** | • **300,000개** 단일세포 RNA-seq 프로파일<br>• H1 hESC 세포주• 300개 CRISPRi genetic perturbations<br>• 10x Genomics Flex 플랫폼 사용<br>• 학습/검증/테스트 세그먼트로 분할 제공 |
| **참여 방법** | 1. virtualcellchallenge.org 웹사이트 등록<br>2. 팀 구성 (1-8명)<br>3. 데이터 다운로드 및 모델 개발<br>4. 리더보드 제출 (선택, 1일 1회 제한)5. 최종 제출 (필수, 1일 1회 제한)<br>• 개인 또는 기업 소속으로 참여 가능<br>• 한 기업의 직원만으로 팀 구성 가능 |
| **경쟁 규모** | • **초대형 글로벌 챌린지** (2025년 기준)<br>• **5,000명 이상** 등록<br>• **1,200개 팀** 제출<br>• **300개 팀** 최종 제출<br>• **114개국** 참여<br>• 학생부터 대형 연구기관까지 다양 |
| **평가 기준** | • **PDS (Perturbation Discrimination Score)**: 예측된 교란이 서로 구별 가능한지 (L1 norm)<br>• **DES (Differential Expression Score)**: 상향/하향 조절 유전자 세트 정확도<br>• **MAE (Mean Absolute Error)**: 전사체 전체의 유전자 수준 예측 정확도• 3개 메트릭 종합 평가 |
| **상금/혜택** | • **총 상금: \$100,000<br>**• Grand Prize 포함<br>• Cell 저널 논문 게재<br>• 우수 모델은 약물 발견 분야 적용 가능성 |
| **특이사항** | • **Machine Learning Predictions Only**: 실험실 결과나 문헌 사용 금지• 미국 수출통제 대상국 참가 제한 (북한, 이란, 러시아 등)<br>• Arc 직원 및 2025년 2월 이후 자문받은 학생 참가 불가<br>• 2025년 1차 대회 완료, 결과 발표됨<br>• **매년 반복 예정**: 새로운 세포 타입, 더 복잡한 도전과제 |
| **권장 접근법** | • Deep learning + classical statistical features 조합이 효과적<br>• 순수 end-to-end 학습은 아직 한계<br>• Distributional shift 고려 필요 (H1 hESC는 학습 데이터와 다름)<br>• scRNA-seq 데이터 전처리 중요 |
| **스폰서** | NVIDIA, 10x Genomics, Ultima Genomics |

---

### 4. DREAM Challenges - Target 35 Drug Discovery (2026년에 DREAM Challenge 새로운 것 열릴 것 같은데, 아직 안열림)

[https://dreamchallenges.org/open-challenges/](https://dreamchallenges.org/open-challenges/)

| 항목 | 내용 |
|---|---|
| **챌린지명** | Target 35 Drug Discovery Challenge |
| **주최기관** | DREAM Challenges, Target 2035 Initiative, Sage Bionetworks |
| **개최 시기** | • 발표: 2025년 4월 7일• **구체적 타임라인 미공개추정**:<br>• Target 2035는 2021년 시작된 글로벌 이니셔티브<br>• 2025년 중후반\~2026년 진행 예상 |
| **주요 태스크** | • Inaugural (첫 번째) Target 2035 챌린지<br>• 특정 단백질 타겟에 대한 약물 발견<br>• 계산 방법론으로 신약 후보 물질 예측<br>• 상세 과제는 출시 후 공개 예상 |
| **데이터 규모** | • Target 2035는 미연구 단백질의 구조와 기능 규명 목표<br>• 구조 생물학, 약물-타겟 상호작용 데이터 예상 |
| **참여 방법** | 1. dreamchallenges.org 등록<br>2. Synapse 플랫폼 접속<br>3. 챌린지별 규칙 및 데이터 다운로드<br>4. 약물 후보 예측 모델 개발5. Synapse 제출 |
| **경쟁 규모** | • DREAM 챌린지 표준 규모<br>• 약물 발견, 구조 생물학, AI/ML 연구자<br>• 제약 산업 관심 예상 |
| **평가 기준** | • 예측된 약물 후보의 결합 친화도• 선택성• 약물성(druglikeness)<br>• 실험 검증 가능성 |
| **상금/혜택** | • 상금 정보 미공개<br>• Target 2035 글로벌 이니셔티브 참여<br>• 신약 개발 파이프라인 기여 |
| **특이사항** | • **Target 2035와 첫 협력<br>**• 미연구 단백질 표적화 목표<br>• 글로벌 과학 커뮤니티 협력 강조• 오픈 사이언스 원칙 |

---

### 종합 비교 및 권장사항

#### 난이도 및 진입장벽

| 챌린지 | 난이도 | 진입장벽 | 권장 팀 |
|---|---|---|---|
| **CAGI7 RGP-CRAM** | ★★★★★ | 높음 (기관 서명, 승인 절차) | 임상유전학 경험팀, 변이 해석 전문가 |
| **CAFA 6** | ★★★★☆ | 낮음 (Kaggle, 공개) | 단백질 기능 예측 연구자, 딥러닝 전문가 |
| **Virtual Cell 2025** | ★★★★★ | 중간 (종료됨, 2026 대기) | 단일세포 분석, perturbation 모델링 전문가 |
| **Target 35** | ★★★★☆ | 중간 (예상) | 구조생물학, 약물설계 전문가 |

#### 상금 및 임팩트

| 챌린지 | 상금 | 논문 기회 | 산업 임팩트 |
|---|---|---|---|
| **CAGI7 RGP-CRAM** | 미공개 | ⭐⭐⭐⭐⭐ (공동 출판) | 희귀질환 진단 |
| **CAFA 6** | **\$50,000** | ⭐⭐⭐⭐⭐ (Nature급) | 단백질 DB 주석 |
| **Virtual Cell 2025** | **\$100,000** | ⭐⭐⭐⭐⭐ (Cell 게재) | 약물 발견 |
| **DREAM(Target 35_** | 미공개 | ⭐⭐⭐⭐☆ | 신약 개발 |
