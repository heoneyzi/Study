# Perturb 필수 데이터셋 — my dataset map

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › [VCC 2026](README.md)</sub>

> ✍️ **강지헌 (me)** · 📅 2026-08 (before the 08-22 meeting) · 🗂️ Source: Notion — *Functional Genomics 2 › Virtual Cell Challenge 2026*

---

## 데이터셋 개요

Cell Specific하지 않고, 새로운 Gene에 대한 perturbation에서 어떻게 작동할지 알아야함.

> - Gene을 잘 알아야함
> - Cell Context를 잘 알아야함
> - 같은 Gene Perturbation이 Cell마다 어떻게 바뀌는지
> - 처음 본 Cell에서도 가능해야함

### Perturbation Modality

| Modality | 방향 | 매커니즘 |
|---|---|---|
| **CRISPRi** | ↓ 억제 | dCas9-KRAB로 전사 억제 |
| **CRISPR KO** | ✕ 소실 | Cas9 절단·frameshift |
| **CRISPRa** | ↑ 활성 | dCas9-활성인자로 과발현 |
| **shRNA** | ↓ 억제 | RNAi 분해 |
| **소분자/약물** | 다양 | 화학적 저해/활성 |
| **cytokine 자극** | 다양 | 신호전달 활성화 |

- 현재 찾은 데이터셋은 ***CRISPRi***에 집중했음

## 데이터 종류

### GSE281048 (Jiang24 / Mixscale)

> ***같은 Gene Perturbation이 Cell마다 어떻게 바뀔까?***

링크: <br>[NCBI - WWW Error Blocked Diagnostic](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE281048)

```javascript
K562
 ├─ Gene A knockdown
 ├─ Gene B knockdown
 ├─ Gene C knockdown
 ...
```

```javascript
K562
 ├─ Gene A knockdown
 ├─ Gene B knockdown
 ├─ Gene C knockdown
 
 A549
 ├─ Gene A knockdown
 ├─ Gene B knockdown
 ├─ Gene C knockdown
 ...
```

- 기본적인 perturb-seq 데이터는 하나의 Cell에 대해서 많은 녹다운 데이터를 가지고 있음<br>이 데이터셋은 다양한 Cell에 대한 데이터를 가지고 있음
- 어찌보면 zero shot perturbation에서 가장 취지에 적합한 데이터셋
- <b> </b>PerturBench의 “Jiang24” 벤치마크

---

### Replogle 2022

> ***Gene Perturbation의 기본 문법을 알려주자***

```javascript
K562
 ├─ Gene A knockdown
 ├─ Gene B knockdown
 ├─ Gene C knockdown
 ...
 ├─ Gene Z knockdown
```

- 이 데이터셋은 K562 세포를 중심으로 수많은 Gene을 녹다운 시켜봤음
- Gene Perturb에 대한 기본적인 개념을 학습시켜줄 수 있음
- 새로운 Gene?에 대해서 들어왔을 때 강점을 가질 것임
- Cell Context가 K562와 RPE1 정도 뿐임

---

### Marson 1차 CD4+ T세포 genome-scale CRISPRi

> ***모델이 Cell Line이 아닌 진짜 세포에서도 작용할까?***

```javascript
Cell Line
 ├─ K562
 ├─ A549
 ├─ MCF7
 ├─ HepG2
 ├─ Jurkat
 ...
```

```javascript
Primary Cell
 ├─ primary CD4+ T cell
 
```

- 실험에서만 사용하는 Cell Line을 과도하게 외워서 푸는 것인지 아닌지 확인 가능
- 실제 사람 세포에서도 되는지 확인 가능
- 대규모 + CRISPRi + primary cell + donor diversity

---

### scBaseCount / CELLxGENE Census

> ***처음 보는 세포에 대해서 이해를 제대로 시키자***

```javascript
T cells
B cells
epithelial cells
fibroblasts
neurons
hepatocytes
endothelial cells
cancer cells
stem cells
...
```

```javascript
tissues
donors
diseases
states
...
```

- Cell X non-targeting control expression이 들어오게 될텐데, 이에 대해서 cell이 어떤 특징을 가지는지 알아야지 성능이 오를 것임

$$
X_{control} = [X_1, X_2, ... X_{10000}]
$$

```javascript
new control
↓
context encoder
↓
"이 세포는 기존의 A와 B 사이쯤에 있구나"
```

---

### VCC 2025 H1 hESC

> ***잘하고 있는지 작년 데이터로 평가해보자***

링크: [https://github.com/ArcInstitute/arc-virtual-cell-atlas/blob/main/virtual-cell-challenge/tutorial-R.ipynb](https://github.com/ArcInstitute/arc-virtual-cell-atlas/blob/main/virtual-cell-challenge/tutorial-R.ipynb)

```javascript
K562
RPE1
A549
MCF7
...
-> 암세포주
```

```javascript
H1
-> human embryonic stem cell
```

- 아무래도 작년 데이터이다 보니까 학습보다도 Zeroshot 시험지로 이를 사용할 수 있지 않을까?

---

### X-Atlas/Orion

> ***다양한 Gene CRISPRi 데이터로 Gene에 대해서 알려주자***

링크: [Xaira-Therapeutics/X-Atlas-Orion at main](https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Orion/tree/main)

- Protein Coding Genes가 19000여개 존재함
- Replogle 2022처럼 Gene에 대한 이해도를 높여주는 역할
- Cell Context가 HCT116와 HEK293T가 대부분임

---

### GSE264667

> ***Replogle 2022가 아닌*** ***추가적인 Context에 대한 적용***

링크: [NCBI - WWW Error Blocked Diagnostic](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE264667)

```javascript
Jurkat → T-cell 계열
HepG2  → liver 계열
```

```javascript
Train:
K562
RPE1
Jurkat

Test:
HepG2
```

- Cell Holdout 실험으로 늘릴 수 있지 않을까?

---
