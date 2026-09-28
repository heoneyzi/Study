# Method — 윤진 CAFA 6 variants

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 1 · Functional Genomics](../README.md) › [CAFA 6](README.md)</sub>

> ✍️ **조윤진 (teammate)** · 📅 2026-01 · 🗂️ Source: Notion — *Functional Genomics › 개인 아카이브 › [윤진] 코드 1차 시도*

---

| 결과 | 구조 요약 | 역할 |
|---|---|---|
| 결과 1 | mean ⊕ max + GCN | **best guess 예상** |
| 결과 2 | mean + GCN | 안정적 baseline |
| 결과 3 | CLS + GCN | 표현력 실험 |
| 결과 4 | CLS + MLP | GCN ablation |

#### 공통 전제 (CAFA6 베이스라인)

- **Protein embedding**: ESM-C (EvolutionaryScale)
- **GO ontology**: CAFA6 기준 `go-basic.obo`
- **GCN 구조**: CAFA5 `protnn` 스타일
    <details>
    <summary><b>GCN</b></summary>

    #### 입력

    1. **Node feature**
        ```
        X ∈ R^{N_protein × N_GO}
        
        ```

        - N_GO ≈ 수천
        - 각 GO term 노드의 feature = NN/Boost 예측 점수
    2. **Graph structure (GO DAG)**
        ```
        A ∈ {0,1}^{N_GO × N_GO}
        
        ```

        - A\[i,j\] = 1 → i is_a j (child → parent)
            $$
            x^{(0)} = \text{NN\_pred} \in \mathbb{R}^{N_{GO}}
            $$
    3. **Training with constraint : Topological order (단백질마다 독립적으로 GO Index 사용)**
        - 자식 node의 특징을 가지면 당연히 부모 node의 특징을 가지므로, directional graph에서 P부모\>P자식이 되도록 설계
            - ex.
                > 만약 단백질이
                > `GO:protein_kinase_activity` 를 가진다면
                >
                > 반드시 `GO:kinase_activity` 도 가져야 한다

        **Forward Training**

        ```
        Input: x_0  (NN 예측 점수)
        for l = 1..L:
            x_l = σ( W_l · (A_norm · x_{l-1}) )
        Output: x_L
        
        ```

    $$
    [
    x_{\text{parent}}^{(l+1)}
    = f\Big(
    x_{\text{parent}}^{(l)},
    \sum_{\text{child} \in Children(parent)} x_{\text{child}}^{(l)}
    \Big)
    ]
    $$

    $$
    [
    x^{(l+1)} = \sigma\Big(
    W_l \cdot \big(
    x^{(l)} + A^\top x^{(l)}
    \big)
    \Big)
    ]
    $$

    **⇒ 기능 간 논리적 제약, mean pooling으로 손실된 annotation bias 보정**

    ---

    </details>

    - node = GO term
    - node feature = model 예측 score
    - message passing = child → parent
- **Loss / metric**: CAFA F-max

#### 1. **ESM-C + (mean ⊕ max pooling) → Linear → GCN**

```shell
Residue embeddings  [L, D]
   ├─ mean pooling  → [D]
   ├─ max pooling   → [D]
   └─ concat        → [2D]
           ↓
        Linear
           ↓
      GO score
           ↓
          GCN

```

- **mean pooling**
    - 전역적 기능 신호 (CAFA에 매우 잘 맞음)
- **max pooling**
    - 특정 domain / motif의 강한 신호 보존
- concat으로:
    - “전체 기능” + “국소 강한 evidence” 동시 제공

#### 2. ESM-C + mean pooling → Linear → GCN

```shell
Residue embeddings [L, D]
      ↓ mean
   Protein emb [D]
      ↓ Linear
   GO score
      ↓ GCN
```

#### 3. **ESM-C + CLS token → Linear → GCN**

```shell
CLS embedding [D]
     ↓ Linear
  GO score
     ↓ GCN
```

#### 4. **ESM-C + CLS token → MLP (no GCN)<br>**

```shell
CLS embedding [D]
      ↓ MLP
   GO score

```
