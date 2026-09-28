# [윤진] Evaluating the representational power of pre-trained DNA language models for regulatory genomics

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../../README.md) › [🧬 Genomics](../../../README.md) › [Season 1 · Functional Genomics](../../README.md) › [Journal club](../README.md) › [Paper proposals](README.md)</sub>

> ✍️ **조윤진 (teammate)** · 📅 week-1 proposal (Feb 2026) · 🗂️ Source: Notion — *Functional Genomics › 저널클럽 논문 제안*
>
> 🗳️ Proposal · 1주차 · ✅ read together · 읽고 싶어요: 윤진, 민선, 유민, 지헌, 수빈
>
> ➡️ Became my week-2 presentation: [02 · gLM evaluating](../02_week2_glm_evaluating.md).

---

링크 : [link.springer.com](https://link.springer.com/article/10.1186/s13059-025-03674-8)

<p align="center"><img src="assets/b4f97384_01.png" alt="figure" width="720"></p>

1. **선정 이유** : <ins>**Genome language Model의 objective 중 regulatory and functional genomics에 초점을 맞춤**</ins>. **Functional Genomics의 최신 지견에 대한 개괄적 이해가 GLM의 관점에서 가능한 논문.** 방대한 나열식 리뷰 논문이 아니라 중요한 것을 중요하게 강조하여, 우리의 background knowledge를 쌓기에 좋을듯. (2025 7월 논문인데 피인용수 47)
    - 이 분야에서 유명하신 저자 [https://link.springer.com/researchers/56018284SN](https://link.springer.com/researchers/56018284SN) (유민)
    - <b>AI </b>: 이 분야에서 Tokeninzation, self-supervised learning의 방법론에서 어떤 시도들이 있었는지, 한계가 무엇인지에 대한 백그라운드 설명이 잘 되어 있음.
    - **Genomics** : 앞으로 우리가 virtual cell challenge에 나간다면 알면 좋은, 주요 biological downstream task에 대한 설명이 잘 되어 있음.
    - Discussion/conclusion에서 논의하는 바가  방향 잡기에 좋음.<br>
1. <b>내용 : </b>
    주요 Genomic Language Model들에 대해서, cell type specific한 functional genomics prediction task의 수행능력을 실험함. Pre trained language model이, <ins><b>cell 특이적인 정보를 잘 포착하지 못한다(머신러닝과 다를 게 없다) </b></ins><ins>는</ins> 결론

    > Here, we evaluate the representational power of pre-trained gLMs to predict and interpret cell-type-specific functional genomics data that span DNA and RNA regulation for six major functional genomics prediction tasks. Our findings suggest that probing the representations of current pre-trained gLMs do not offer substantial advantages over conventional machine learning approaches that use one-hot encoded sequences. Nevertheless, highly tuned supervised models trained from scratch using one-hot encoded sequences can achieve performance competitive with or better than pre-trained models across the datasets explored in this study.
