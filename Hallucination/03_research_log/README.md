<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › **03 · Research log**</sub>

# 🗒️ 03 · Research log — the LVLM team project (May–June 2025)

Meeting notes and ideation from the phase-1 project with Heejae Yang; the 5/28 kick-off set CVPR as the target. The thread runs from splitting the literature into ViT-side and LLM-side attention, to Jiheon's "look like a human" proposal, to a concrete to-do list. The notes are in Korean.

| # | Note | What it covers | Date |
|---|---|---|---|
| 9 | [5/28 meeting](01_meeting_0528.md) | Kick-off: CVPR target; ViT-side (Jiheon) vs LLM-side (Heejae) attention; what the proof experiments should show | 2025-05-28 |
| 10 | [Background features](02_background_features.md) | How to use the region outside the segmented objects (DE-ViT, context encoders) | 2025-05 |
| 11 | [6/5 feedback: "look like a human"](03_feedback_0605.md) | **His idea:** n objects + 1 background, per-token selection of what to attend to; open problems (what to contrast against, training vs inference-only) | 2025-06-05 |
| 12 | [6/12 meeting](04_meeting_0612.md) | CoT for re-looking, a consistent story, an LLM-only comparison, decoding choices, AGLA as the priority read | 2025-06-12 |
| 13 | [Ideation (6/21)](05_ideation_0621.md) | **His plan:** goal, method and two open problems; prompt-aware segment selection; two triggers for re-injecting segments | 2025-06-21 |
| 14 | [To-do](06_todo.md) | Segmentation model, benchmark inference, box and class conditioning | — |
| 15 | [Attention-map visualisation](07_attention_map_visualization.md) | First attempt with VLM-Visualizer | — |

---
<sub>[← 02 · Paper reviews](../02_paper_reviews/README.md) · [📑 Hallucination index](../README.md) · [04 · MCoT & attention →](../04_mcot_attention/README.md)</sub>
