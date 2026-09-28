# 2026 VCC Datasets + New

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **김서연 (teammate)** · 📅 2026-08 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

Background (개인 공부용)

- scRNA-seq: 세포 x 유전자 행렬
- Perturbation: 특정 유전자 일부러 knock down
- CRISPRi: 유전자 자르지 않고 발현만 억제하는 방법 (mRNA)
- Guide RNA: 어떤 유전자를 끌지 지정해주는 안내 서열
- non-targeting control (NTC): 아무 유전자도 타겟하지 않는 가짜 guide, 대조군
- UMI: 세포 하나에서 mRNA 분자 수
- Cell context / cell line: 같은 유전자 꺼도 세포 종류에 따라 반응이 다름!!

대회 과제<br>: 아무것도 안 건드린 세포 데이터와 끌 유전자 목록만 주고 세포들의 발현 예측<br>- 세포주에 따른 학습 + Pre-training! 이 중요할 듯

\*데이터를 요약할 때, 어떤 것을 집중해서 볼지 정하면 좋을 것 같습니다.

[Virtual Cell Challenge](https://virtualcellchallenge.org/app/datasets#virtual-cell-atlas)

Challenge Datasets

- Validation set
    - Cell context A, B, C
    - Each context: non-targeting guide 46 x 400 cels
    - UMI 중앙값 2만
    - 예측할 300개 유전자 목록
    - 총 제출 세포 수 = 300(유전자) x 400(cells) x 3(context)
    - 각 세포당 유전자 18,533 → 360000 x 18533 행렬
- Final test set
    - New cell context D,E,F
- Target Gene Selection: on-target knockdown \> 80%
    - 작년에는 반응 거의 없는 유전자도 섞었다는 점에서 차이가 있음

Arc Virtual Cell Atlas

: Observational(정상, for pretraining?) + Perturbational = 6억

1. scBaseCount - Observational
    - SRA의 단일세포 데이터를 AI가 찾아내서 동일한 파이프라인으로 처리
    - 5억 200만 세포, 27개 생물종, 75개 조직
        - 전체 생물종으로 학습하고 인간으로 fine-tuning?
    - 처리 방식을 통일화함!
2. Tahoe-100M - Chemical Perturbational
    - 1억 세포. 6만 약물실험. 암세포 모델 50종 x 약물 1,100종 반응 지도
    - 유전자 아니고 약물 변형 데이터 - 세포가 외부 자극에 반응하는 일반 패턴을 학습
        - Flow matching 학습에 유리?
        - 세포주마다 어떤 유전자가 켜져 있는지 학습 가능
            - 약물의 반응 경로를 알 때
3. 2025 VCC Dataset
    - H1 hESC (인간, 배아줄기세포)
    - Perturb당 1000세포, 세포당 UMI 5만 이상, high on-target knockdown
    - 10x Flex(고정형) - 올해와 동일 but 다른 데이터셋과 합칠 때 정규화 유의해야 함

Public Perturbation Datasets

1. Gene Perturbations
    - [NCBI - WWW Error Blocked Diagnostic](https://pubmed.ncbi.nlm.nih.gov/35688146/)
        - K562(백혈병 세포주) Genome-wide (61.3GB), K562 필수 유전자만(9.9GB), RPE1(망막 상피 세포주) (8.1GB)
        - K562 genome-wide: 2025 VCC의 train/validation과 많이 겹침 → 한 유전자를 K562에서 껐을 때랑 다른 세포주에서는 어떨지 추론할 수 있음
    - [Transcriptome-wide analysis of differential expression in perturbation atlases](https://www.nature.com/articles/s41588-025-02169-3)
        - DepMap Common Essential Genes → 단일세포 CRISPR screening. 세포주 다양성
2. Chemical Perturbations
    - [Systematic reconstruction of molecular pathway signatures using scalable single-cell perturbation screens](https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41556-025-01622-z)
        - A549(폐), MCF7(유방), HT29(대장), HAP1, K562(골수), BxPC3(췌장)에서 같은 perturb이 세포 종류에 따라 어떻게 달라지는지
    - [Massively multiplex chemical transcriptomics at single-cell resolution](https://www.science.org/doi/10.1126/science.aax6234)
        - Nuclear hashing으로 여러 조건을 한번에 단일세포 해상도로 측종
        - 암세포주 3종 x 화합물 188종
    - [Multiplex single-cell chemical genomics reveals the kinase dependence of the response to targeted therapy](https://cell.com/cell-genomics/retrieve/pii/S2666979X23003397?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2666979X23003397%3Fshowall%3Dtrue)
        - 교모세포종 세포주
        - 유전적 + 화학적 perturb

Thoughts

- 전체적으로 세포 종류를 커버하는 Pre-training이 중요하다는 점을 감안했을 때, 현재 알아본 데이터셋으로 커버되는 부분과 커버되지 않은 부분을 정리하면 다음과 같음. (지헌, 서진, 민석님 데이터 토대로, 계통 분류는 클로드의 기준을 따라서 맞는지는 몰라유..)
    | 계통 | 보유 | 상태 |
    |---|---|---|
    | 혈액/림프 | K562, HAP1, 1차 CD4+T, Jurkat | O |
    | 줄기세포 | H1 (hESC), KOLF2.1J (hiPSC) | O |
    | 상피/부착 | RPE1, HepG2, A549, MCF7, HT29, HCT116, HEK293T, BxPC3 | O(과잉) |
    | 신경/교세포 |  | X |
    | 근육/심근 |  | X |
    | 내피/섬유아 |  | X |
    | 골수계 | K562, HAP1 | O(백혈병 한정) |
- 신경: [www.sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0896627319306403), [Genome-wide CRISPRi/a screens in human neurons link lysosomal failure to ferroptosis](https://www.nature.com/articles/s41593-021-00862-0)
    - iPSC를 Ngn2로 분화한 뒤 genome-wide로 함. 신경퇴행 관련 유전자에 대한 CROP-seq 전사체(2021 Nature)
    - 주의점: CROP-seq는 guide에 대한 방식이 다름..! CRISPRi & CRISPRa를 섞어 사용해서 데이터 사용할 거면 분리해서 사용해야 함.
- 미세아교세포: [https://www.nature.com/articles/s41593-022-01131-4](https://www.nature.com/articles/s41593-022-01131-4)
    - 주의점: 마찬가지로 CRISPRi/a 섞어 ㅅ용함
    - 성숙 골수계
- 심근: [www.sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S2213671125003170)
- 대형 DB 먼저 훑는게 나을수도
    - PerturbDB: [PerturbDB for unraveling gene functions and regulatory networks](https://academic.oup.com/nar/article/53/D1/D1120/7755478)
    - PerturbBase: [PerturBase: a comprehensive database for single-cell perturbation data analysis and visualization](https://academic.oup.com/nar/article/53/D1/D1099/7815638)
- 대조군에서 세포의 종류를 읽어내는 과정이 필요함
    - scBaseCount
    - DepMep에서
        - CCLE → 대조군의 세포주 추정
        - Chronos → 각 세포에서 유전자의 중요도를 수칳ㅘ
        - CCLE 좌표에 매핑한 후 그 좌표의 Chronos 가져와서 perturb 효과 크기를 추정
- 모르는 유전자가 나왔을 때 유전자간 연결에 대한 정보가 있으면 좋을듯??
- 세포주에 따른 차이 vs 그냥 유전적 배경에 따른 노이즈 분리. 즉, 도너 다양성 → context 차이에 따른 발현의 차이의 범위를 줄일 수 있을 수도?
    - [A genome-scale single-cell CRISPRi map of trans gene regulation across human pluripotent stem cell lines](https://www.cell.com/cell-genomics/fulltext/S2666-979X(25)00332-5)

결론..

- 평가 방식에 대한 안내도 나와있던데, 이것을 우선 정리한 후 어떤 데이터셋이 필요할지 기준을 세운 후 거기에 맞게 정리하면 좋을 것 같습니다. → 평가 기준표 정리해 놓을게용
- Data 생성 방식에 대해 좀 공부가 필요할 것 같아서 논문 더 읽어보려 합니다
- scPerturb([https://github.com/sanderlab/scPerturb](https://github.com/sanderlab/scPerturb))이랑 PerturbDB, DepMap 좀 큰 애들 위주로 기준에 따라 정리를 다시 해봐야할 것 같습니다.
