# 5/28 미팅 (할루시네이션)

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › [03 · Research log](README.md)</sub>

> 🗓️ 2025-05-28 · LVLM 객체 환각 스터디 (1단계, 팀 프로젝트)

목표 : cvpr

지헌 : ViT 어텐션을 문제 삼기. 어텐션<br>LLM에도 긍정적 영향을 끼칠 수 있다는 것. ViT에서도 어텐션이 예쁘게 걸리면 이후에도 좋은 영향이 갈 것.

희재 : LLM 어텐션,

두 쪽을 다 건드리긴 해야될 것.

우리가 할 증명실험을 찾는 거

Vit / LLM에서 각자 베이스 라인으로 (둘 다 어텐션 )

오브젝트를 보는 순간 순간 적절한 곳을 /  → object hallucination

CLIP자체가 문제 → object 유무는 잘한다. attribute, relation

object간 관계

attention 조절해줄 수 있는 모듈이

아이디어 :

segment 결과 따라서 해당하는 부분에만 어텐션 잘 끌어올 수 잇도록, 해당 키워드가 등장했을 <br>때,  → 이미지에 대한 어텐션 조작이 굳이 필요하지 않을 때에는 t

background feature를 어떻게 뽑아내는가 → 우리 연구에서는 어떻게 쓸 수 있을까?

희재 : 할루시네이션 + ViT 자체를 건드는 논문들

지헌 : 프로젝션 이후에서 어텐션 건드리는 논문들

크로스어텐션 모델 다루는 애들

llava 계열 → 지배적이면

---
<sub>[← ARGUS — Vision-Centric Reasoning with Grounded Chain-of-Thought](../02_paper_reviews/03_argus.md) · [📑 목차](../README.md) · [Background Feature 다루기 →](02_background_features.md)</sub>
