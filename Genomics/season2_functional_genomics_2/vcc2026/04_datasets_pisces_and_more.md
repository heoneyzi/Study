# [유민] X-Atlas/Pisces · Feng 2026 · sci-Plex-GxE 외 후보

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **정유민 (teammate)** · 📅 2026-08 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026 (untitled page)*

---

## X-Atlas/Pisces

- 링크: [https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Pisces](https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Pisces)
- 논문: [https://www.biorxiv.org/content/10.64898/2026.03.18.712807v1](https://www.biorxiv.org/content/10.64898/2026.03.18.712807v1) (2026.03)
- 규모: 25.6M perturbed single cell, genome-wide CRISPRi 7개 스크린, 총 16개 context
- Context: HCT116, HEK293T, HepG2, iPSC, resting Jurkat, CD3/CD28 activated Jurkat, multi-lineage 분화 중 iPSC
- 역할 1: Orion의 상위호환. 동일 플랫폼(FiCS)이라 배치 통일성 유리
- 역할 2: 분화 중 iPSC context 보유. VCC의 H1 hESC 및 unseen context 과제와 직결
- 역할 3: resting vs activated Jurkat 쌍으로 세포주 동일, 상태만 다른 비교 가능
- 주의 1: 현재 전체가 아닌 subset 공개. HepG2/iPSC 스크린 일부는 Coming Soon 표기
- 주의 2: 라이선스 CC BY-NC-SA 계열. 대회 규정과 대조 필요
- **참고: 동반 모델 X-Cell (4.9B diffusion LM, **[**github.com/xaira-therapeutics/x-cell**](http://github.com/xaira-therapeutics/x-cell)**)**

## Feng et al. 2026

- 링크: [https://www.cell.com/cell-genomics/fulltext/S2666-979X(25)00332-5](https://www.cell.com/cell-genomics/fulltext/S2666-979X(25)00332-5)
- Preprint: [https://www.biorxiv.org/content/10.1101/2024.11.28.625833v1](https://www.biorxiv.org/content/10.1101/2024.11.28.625833v1)
- 규모: 7,226 유전자, 34개 iPSC 세포주, 26명 도너
- 세포 수: targeting guide 배정 219,206 세포 + NTC/무guide 대조군 499,998 세포
- 라이브러리: Dolcetto, gene당 3 gRNA + NTC 40개
- 역할: cell line / genomic background / target gene의 분산 분해가 논문에 직접 제시됨. 세포주 차이 vs 유전적 배경 노이즈 분리 문제를 데이터로 다룰 수 있는 유일한 소스
- 주의: gRNA당 중앙값 8세포, gene당 25세포로 매우 얕음. pretraining 가중치를 낮게 잡거나 pseudobulk 활용 권장
- 비고: PRiMeFlow B.2에 포함된 항목

## McFaline-Figueroa et al. 2024 (sci-Plex-GxE)

- 링크: [https://www.cell.com/cell-genomics/fulltext/S2666-979X(23)00339-7](https://www.cell.com/cell-genomics/fulltext/S2666-979X(23)00339-7)
- 규모: 약 100만 perturbed cell
- 구조: 522개 human kinase 유전적 perturbation x GBM 세포주 3종 x RTK 경로 저해제 4종
- 역할 1: 신경/교세포 계통 공백을 부분적으로 메움
- 역할 2: 유전적 + 화학적 perturbation 조합(GxE)을 동시에 제공하는 유일한 카드
- 주의: sci-RNA-seq 기반. 10x Flex와 chemistry가 완전히 달라 정규화 설계 필수
- 비고: PRiMeFlow B.2에 포함된 항목

## Replogle et al. 2020 (direct-capture Perturb-seq)

- 링크: [https://www.nature.com/articles/s41587-020-0470-y](https://www.nature.com/articles/s41587-020-0470-y)
- 규모: 소규모, K562 단일 context
- 구조: sgRNA를 전사체와 함께 직접 시퀀싱. dual-guide 벡터 기반 조합 perturbation 포함
- 역할: Replogle 2022와 다른 라이브러리/배치이므로 배치 로버스트니스에 기여
- 주의: genetic interaction 실험이 섞여 있음. single-gene knockdown subset만 추출해서 사용
- 우선순위: 낮음
- 비고: PRiMeFlow B.2에 포함된 항목

## Perturb-CITE-seq (Frangieh et al. 2021)

- 규모: 218,331개 흑색종 세포, 248개 유전자 타겟
- 조건: control / co-culture / IFN-gamma 자극 3개 조건 분리
- 역할: 멜라닌세포 계통 + 사이토카인 자극 context를 동시에 제공
- 비고: 규모가 작아 부담 없음. 조건별로 별도 데이터셋 취급 권장

## PerturbAI 마우스 뇌 in vivo CRISPR Atlas

- 링크: [https://www.perturb.ai/8-million-crispr-atlas](https://www.perturb.ai/8-million-crispr-atlas)
- 규모: 800만 세포, 약 2,000개 질환 연관 유전자
- Context: 마우스 전뇌, in vivo, single-nucleus RNA-seq
- 역할: 팀 공백표의 신경 계통 X 칸을 메울 수 있는 유일한 대규모 소스
- 주의: 마우스 + in vivo + snRNA-seq. human in vitro 10x 데이터와 통합 비용이 큼
- 우선순위: 여유 있을 때만. 없으면 스킵

## 접근 불가 항목

- Illumina Billion Cell Atlas: 200개 이상 질환 관련 세포주, 10억 세포 목표. AstraZeneca, Merck, Eli Lilly, Formation Bio 등 얼라이언스 파트너 한정. 참고만
- PRiMeFlow 내부 독점 데이터: H1 hESC 및 iPSC와 생물학적으로 구별되는 완전 분화 non-pluripotent 세포주. 획득 불가하나, 이 문장 자체가 우리 공백표의 신경/근육/내피 칸이 핵심이라는 것을 시사 메모

---

### 메모

우선순위: X-Atlas/Pisces \> Feng 2026 \> sci-Plex-GxE \> Replogle 2020

- Replogle/Nadig baseline은 그대로 유지
- 신경/근육/내피 공백은 현재 공개 데이터 기준 Pisces의 multi-lineage 분화 iPSC + sci-Plex-GxE의 GBM 조합이 최선
- chemistry가 10x Flex, 10x 3' v3, sci-RNA-seq, PIP-seq로 제각각. 데이터셋 추가 시마다 정규화 전략을 함께 결정할 것
- CROP-seq 계열(신경, 미세아교세포)은 CRISPRi/CRISPRa 혼합이므로 반드시 분리 후 사용
