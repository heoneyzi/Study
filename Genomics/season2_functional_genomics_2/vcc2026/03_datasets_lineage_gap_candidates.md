# [동현] 계통 공백을 채울 데이터셋 후보 — lineage-gap datasets

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **이동현 (teammate)** · 📅 2026-08 · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026 (untitled page)*

---

## TeloHAEC CAD Perturb-seq

- 링크: [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE210681](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE210681)
- 논문: [https://pmc.ncbi.nlm.nih.gov/articles/PMC10921916/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10921916/)
- 규모: 214,449개 세포, 2,285개 유전자 perturbation
- Context: TeloHAEC human aortic endothelial cell
- Modality: CRISPRi, 10x 3′ scRNA-seq
- 역할 1: 현재 공백표에서 가장 부족한 **내피세포(endothelial) 계통**을 직접 채워주는 데이터
- 역할 2: CAD 관련 유전자를 포함하고 있어 암세포주 중심 데이터와 다른 생물학적 프로그램 학습 가능
- 역할 3: 2천 개 이상의 유전자를 동일한 내피세포 context에서 perturb하여 gene effect와 cell context를 함께 학습하기 좋음
- 주의 1: immortalized endothelial cell이므로 primary endothelial cell과 완전히 동일하지는 않음
- 주의 2: 별도의 pilot 데이터인 GSE212396보다 comprehensive screen인 **GSE210681을 사용**
- **우선순위: P0 — 바로 추가 권장**

---

## Tian et al. iPSC-derived Neuron CROP-seq

- 링크: [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152988](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE152988)
- 규모: iPSC-derived glutamatergic neuron에서 184개 CRISPRi target + 100개 CRISPRa target
- Context: human iPSC-derived neuron
- Modality: CROP-seq, CRISPRi / CRISPRa
- 역할 1: 현재 데이터셋에서 가장 부족한 **신경세포 계통**을 직접 보완
- 역할 2: cancer cell line이 아닌 분화된 post-mitotic neuron에서 perturbation response를 학습할 수 있음
- 역할 3: Pisces의 multi-lineage iPSC가 공개되기 전까지 neuron context를 확보할 수 있는 현실적인 대안
- 주의 1: CRISPRi와 CRISPRa가 함께 있으므로 반드시 modality를 분리해서 사용
- 주의 2: 처음에는 CRISPRi subset만 기존 Replogle/Nadig baseline에 추가하는 것이 안전
- 주의 3: neuron은 cell cycle과 증식 관련 perturbation 효과가 일반 세포주와 크게 다를 수 있음
- **우선순위: P1**

---

## Leng et al. iPSC-derived Astrocyte Perturb-seq

- 링크: [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182308](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE182308)
- 규모: 30개 유전자 perturbation
- Context: human iPSC-derived astrocyte
- 조건: vehicle / IL-1α + TNF + C1q inflammatory stimulation
- Modality: CRISPRi CROP-seq
- 역할 1: neuron뿐만 아니라 **glial lineage**까지 신경계 context를 확장
- 역할 2: 같은 astrocyte에서 resting-like 상태와 cytokine-induced reactive 상태 비교 가능
- 역할 3: 같은 gene perturbation이 inflammatory cell state에 따라 어떻게 변하는지 학습 가능
- 주의 1: target gene 수가 30개로 작기 때문에 gene vocabulary 확장보다는 **context/state transfer 학습용**
- 주의 2: vehicle과 cytokine 조건을 별도 context로 취급해야 함
- **우선순위: P1**

---

## iAssembloid Perturb-seq

- 링크: [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE272093](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE272093)
- 규모: 68개 유전자 perturbation
- Context: 2D neuron monoculture / 3D neuron–astrocyte–microglia assembloid
- 역할 1: 동일한 perturbation을 2D 단일세포 배양과 3D multicellular context에서 비교 가능
- 역할 2: neuron, astrocyte, microglia가 함께 존재할 때 나타나는 non-cell-autonomous effect를 학습할 수 있음
- 역할 3: VCC unseen context에서 단순 cell identity뿐 아니라 주변 세포 조성까지 달라질 가능성에 대비
- 주의 1: 3D assembloid는 일반적인 cell-line Perturb-seq보다 batch 및 composition variation이 큼
- 주의 2: 처음부터 baseline 데이터와 완전히 통합하기보다는 context encoder pretraining 또는 auxiliary dataset으로 사용하는 것이 적절
- 주의 3: cell type별 pseudobulk를 만든 뒤 2D/3D 조건을 분리하는 것이 권장됨
- **우선순위: P1**

---

## Human Cortical Neurogenesis Perturb-seq

- 링크: [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284197](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE284197)
- 규모: 44개 transcription factor perturbation
- Context: primary human cortical radial glia, perturbation 후 D0 / D7
- Modality: CRISPRi
- 역할 1: iPSC-derived neuron과 달리 **primary human neurodevelopment context** 제공
- 역할 2: radial glia에서 분화가 진행되면서 같은 perturbation 효과가 어떻게 변하는지 비교 가능
- 역할 3: Pisces의 multi-lineage differentiation 및 VCC의 stem-cell-derived unseen context와 직접 연결 가능
- 주의 1: target이 transcription factor 중심이고 규모가 작아 genome-wide gene 학습용은 아님
- 주의 2: timepoint를 별도 context로 취급해야 함
- 주의 3: 초기에는 human single-gene knockdown subset만 사용하는 것이 안전
- **우선순위: P1**

---

## Compressed Perturb-seq / THP-1 LPS Screen

- 링크: [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE221321](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE221321)
- 규모: 598개 유전자 perturbation
- Context: THP-1 monocyte, LPS 3시간 자극
- 구조: conventional Perturb-seq / compressed Perturb-seq, CRISPRi / CRISPR KO 비교
- 역할 1: immune context에서 perturbation과 LPS stimulation의 상호작용을 학습 가능
- 역할 2: Marson CD4 T cell 및 Jurkat과 다른 **myeloid lineage**를 추가
- 역할 3: resting vs activated Jurkat, Frangieh IFN-γ 조건과 함께 immune-state transfer 축을 만들 수 있음
- 주의 1: compressed condition은 한 세포에 여러 perturbation이 포함될 수 있어 바로 합치기 어려움
- 주의 2: 우선 conventional CRISPRi single-perturbation subset만 사용 권장
- 주의 3: CRISPR KO와 CRISPRi를 동일 label로 합치면 안 됨
- **우선순위: P1**

---

## IGVF WTC11 Cardiomyocyte Perturb-seq

- 링크: [https://doi.org/10.65695/IGVFDS8493OWMF](https://doi.org/10.65695/IGVFDS8493OWMF)
- Context: WTC11 iPSC-derived cardiomyocyte
- 규모: 약 2,000개 transcription factor를 대상으로 한 production-scale 프로젝트
- Modality: CRISPRi
- 역할 1: 현재 공백표의 **근육/심근 계통**을 채울 수 있는 대규모 후보
- 역할 2: iPSC에서 완전히 분화된 cardiomyocyte context를 제공하여 pluripotent → differentiated context transfer에 유용
- 역할 3: Feng/KOLF2.1J/Pisces iPSC 데이터와 연결하여 분화 전후의 perturbation 효과를 비교할 수 있음
- 주의 1: IGVF production dataset이라 GEO 기반 데이터보다 파일 구조와 metadata 확인 작업이 더 필요할 수 있음
- 주의 2: 실제 사용 전 guide assignment, control 구성, 공개 파일 완결성을 확인해야 함
- 주의 3: 데이터 성숙도가 확인되기 전까지는 핵심 baseline보다 보조 데이터로 취급
- **우선순위: P1 — 다운로드 및 metadata 검증 후 확정**
