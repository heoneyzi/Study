<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../../README.md) › [🧬 Genomics](../../README.md) › [Season 2 · Functional Genomics 2](../README.md) › **Reviews**</sub>

# Reviews — what makes a representation good for Perturbation prediction?

My FG2 review of Jiang et al., *What Makes a Representation Good for Single-Cell Perturbation Prediction?* (ICML 2026, arXiv [2605.19343](https://arxiv.org/abs/2605.19343)), used as a lens to re-read the models the team met and our VCC 2026 results. Next in the series: GeoFlow (planned).

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
