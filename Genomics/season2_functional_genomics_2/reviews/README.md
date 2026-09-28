<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › **Reviews**</sub>

# Reviews — what makes a representation good for Perturbation prediction?

My FG2 review of Jiang et al., *What Makes a Representation Good for Single-Cell Perturbation Prediction?* (ICML 2026, arXiv [2605.19343](https://arxiv.org/abs/2605.19343)), used as a lens to re-read the models the team met and our VCC 2026 results. Next in the series: GeoFlow (planned).

<details>
<summary><b>🇰🇷 한국어 요약</b></summary>

Perturbation 데이터에서 유전자 발현 변동의 대부분은 세포의 배경(세포 종류, 세포주기 등)이 만들고, Perturbation이 만드는 신호는 소수 유전자에 몰린 작은 신호입니다. 논문은 배경과 신호를 나누지 않는 표현이 신호를 눌러 버리거나(억제) 배경과 섞어 버린다(얽힘)고 주장하고, 이를 나누는 PerturbedVAE를 제안합니다. 저는 이 논문을 깊게 읽은 뒤, 그 관점으로 FG2에서 다룬 모델들과 우리 VCC 2026 실험(효과를 옮기는 것이 점수를 만들고 임베딩의 몫은 작았다는 결과)을 다시 해석했습니다. 시끄러운 식당에서 친구의 목소리만 골라 듣는 것처럼, 좋은 표현은 배경 소음과 Perturbation 신호를 분리해 담아야 한다는 것이 핵심입니다. 통합본이 최신판이고, 발표 구성안과 이전 판(임베딩 중심)도 함께 두었습니다.

</details>

<table><tr>
<td align="center" width="50%"><img src="review_assets/charts/chart_jiang24_method_ladder.png" alt="Overall score by method on Jiang24" width="100%"><br><sub>My local proxy runs (Jiang24, BxPC3 held out): only one weighted transfer beats the mean-effect baseline. Not a leaderboard score.</sub></td>
<td align="center" width="50%"><img src="review_assets/charts/chart_kimchi_oracle.png" alt="KIMCHI oracle decomposition" width="100%"><br><sub>Oracle decomposition of the team's KIMCHI line (정유민's SUMMARY §1.6): most of the gap is which response to transfer, not how to generate cells.</sub></td>
</tr></table>

## 📄 Notes

| Note | Author | Date | What it is |
|---|---|---|---|
| [What makes a representation good? (review)](01_what_makes_a_representation_good.md) | 강지헌 (me) | 2026-09-27 | My main FG2 review of *What Makes a Representation Good for Single-Cell Perturbation Prediction?* (ICML 2026), then re-reading FG2 models and VCC through its "shared effect + background-dependent modulation" lens. |
| [Talk plan (slide by slide)](02_talk_plan.md) | 강지헌 (me) | 2026-09 | Slide-by-slide plan for presenting the review: flow, figures and charts, speaker notes. |
| [Embedding-centric edition (09-26)](03_embedding_centric_review_2026-09-26.md) | 강지헌 (me) | 2026-09-26 | Earlier embedding-centric edition of the review (superseded by 01; kept for its model-comparison tables). |

<sub>`review_assets/` holds figures cropped from the paper (credited in the text) and charts I drew for the talk (`review_assets/charts/`).</sub>

---
<sub>[← VCC 2026](../vcc2026/README.md) · [Season 2](../README.md) · [🧬 Genomics](../../README.md)</sub>
