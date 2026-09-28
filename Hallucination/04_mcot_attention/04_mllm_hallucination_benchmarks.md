# MLLM Hallucination Benchmark

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › [04 · MCoT & attention](README.md)</sub>

> 🗓️ 날짜 미상 · Multimodal CoT · 어텐션 기법 조사 (2단계)

- **POPE (Polling-based Object Probing Evaluation)** – *객체 존재(Object Existence)*
    - **과제/지표:** VQA(Yes/No)로 “해당 객체가 ‘없다’고 판별”하는 정확도(객체 환각률 측정).
    - **구성:** MS-COCO 기반, 랜덤/인기/적대 3 split의 질문 설계. 공식 코드/데이터 제공.
    - **왜 유효한가:** 간단하지만 <b>객체 환각(Object Hallucination)</b>만을 정밀 타격. 많은 후속 연구의 기본판정 세트로 채택.
- **NOPE (Negative Object Presence Evaluation)** – *부존재 판별 고난도*
    - **과제/지표:** 부정대명사(NegP: none 등)를 정답으로 요구하는 **부존재 인식 정확도**.
    - **구성:** 2만9.5k 규모 합성 질문으로 스케일 크게 확장. ACL 버전 제공.
    - **왜 유효한가:** 표본 규모와 난도(어휘 다양성/범주 스코프)로 **언어 편향에 의한 환각**을 강하게 드러냄.
- **AMBER (LLM-free Multi-dimensional Benchmark)** – *객체/속성/관계, LLM-free 채점*
    - **과제/지표:** 판별형(객체·속성·관계) + 생성형(객체) 복합, **외부 LLM 판정 없이** 정답성 검증.
    - **왜 유효한가:** “LLM as a Judge” 편향을 제거해 **재현성·견고성**이 높음. 논문에서 “LLM-free”를 강조할 때 적합.
- **FaithScore** – *참조 없는(Reference-free) **세분 사실(Atomic Facts)** 검증*
    - **과제/지표:** 자유서술 답변을 문장→부분절→원자사실로 분해 후 **이미지 일치성**을 자동 검증(사실성 점수). Findings-EMNLP’24.
    - **왜 유효한가:** 캡션/오픈엔디드 답변에서 **세밀한 부분 환각**까지 잡아내 **감소폭을 정량화**하기 좋음.
- **THRONE** – *자유서술(Free-form) **Type-I 환각** 평가 특화*
    - **과제/지표:** 상세 설명 생성 시 환각 자동판정 프레임워크(공개 모델들의 투표 등)로 **Type-I(자유서술) vs Type-II(폐쇄형)** 분리 평가. CVPR’24.
    - **왜 유효한가:** 실제 논문 글쓰기/설명형 답변에서 문제되는 **자유서술 환각 감소**를 수치화 가능.
- **HallusionBench** – *시각 착시+언어 환각 진단*
    - **과제/지표:** 참/거짓·객관식·개방형 혼합으로 **시각적 착시**와 **언어 환각** 교착을 진단. Hugging Face 데이터/논문 페이지 제공.
    - **왜 유효한가:** **지각 착시 상황**에서의 환각을 가시화—“시각 근거 무시” 문제의 감소를 설득력 있게 제시.
- **Bingo (Bias & Interference Challenges)** – *편향/간섭 기반 환각*
    - **과제/지표:** GPT-4V 계열에서 관찰된 **지역/문자(OCR)/다중이미지 간섭** 등으로 유발되는 환각을 체계 진단. 코드 공개.
    - **왜 유효한가:** **문화/문자 편향**이나 **멀티이미지 간섭 환각**을 줄였다는 주장을 뒷받침.
- **HaELM (Hallucination Evaluation based on LLMs)** – *LLM-판정 자동 평가 프레임워크*
    - **과제/지표:** 저비용으로 사람판정 95% 수준에 근접하는 자동 평가. 프레임워크/데이터 공개.
    - **왜 유효한가:** 자체 어노테이션이 어려운 **대규모 자유응답** 실험에서 유용(단, LLM-as-judge 한계는 명시 필요).
- **LLaVA-Bench (In-the-Wild / Wilder)** – *일상 이미지 24장, 60문항(확장판 Wilder도 존재)*, GPT-기반 채점. 데이터셋/블로그/코드 공개.
    - **왜:** 실제 대화형 질의·설명에서 **환각/과잉추론**이 분명히 드러남. 많은 LMM이 기본으로 보고.
- **MM-Vet (v1/v2)** – *복합 능력 통합평가(인식/OCR/지식/공간/수학/언어 생성)*, 개방형 채점.
    - **왜:** 특정 능력 과최적화 없이 **종합 성능**에서 환각 경향을 상대 비교하기 좋음.
- **MMHal-Bench** – *할루시네이션 페널티 특화 96 QA(OpenImages 기반)*, RLHF-V가 제안·배포. HF/깃헙 제공.
    - **왜:** **“환각 억제”에 초점**을 맞춘 인더와일드 평가. RLHF·DPO류 방법의 효과 검증에 적합.

<br>• **MIHBench (Multi-Image Hallucinations)** – *다중 이미지에서의 객체 존재/카운트/동일성 일관성*. 2025 제안.  <br>

---
<sub>[← AttentionMap 후보](03_attention_map_candidates.md) · [📑 목차](../README.md) · [Video-Audio LLM Hallucination — AVCD 분석과 방향 전환 →](../05_audio_visual/01_video_audio_llm_hallucination.md)</sub>
