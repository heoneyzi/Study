# video-SALMONN 2+ 1차 결과 분석

<sub>[🏠 Portfolio](https://github.com/heoneyzi) › [📚 Study](../../README.md) › [🌀 Hallucination](../README.md) › [05 · Audio-visual](README.md)</sub>

> 🗓️ 2026-03 · Audio-Visual LLM 환각 (3단계)

> [!NOTE]
> **큐레이션 메모** — AVHBench 문항(영상 12개 = 원본/불일치 대조 6쌍, 질문 33개)에 대해 video-SALMONN 2+ 7B의 모달리티별(비디오·오디오·텍스트) 어텐션을 기록한 원본 노트입니다. 원본 Notion의 글자색 판정을 기호로 옮겼습니다: 🟦 파랑 = 정답과 일치 · 🟥 빨강 = 정답과 불일치(환각) · 🟧 주황 = 캡션이 정답 설명과 부분적으로만 일치. 문항별 그림 순서: ① 레이어별 평균 어텐션 ② 마지막 레이어(27)의 생성 토큰별 어텐션 ③ 어텐션 상위 오디오 구간 ④ 어텐션 상위 비디오 패치. 코드와 집계 요약은 [E1 실험 폴더](../experiments/E1_avhbench_attention/README.md)에 있습니다.

<p align="center"><img src="assets/f68cf1d8_01.png" alt="figure" width="720"></p>

현재 추출한 것. 12개(대조군집합 6개)으로 실험을 돌려봄

Video SALMONN2+ 7B 모델로

모든 것은 같게 하며 전체 맥스 프레임만 768에서 128로 줄임. 10초밖에 안되는 데이터셋이라 ㄱㅊ할 것 같았음

레이어 28개

레이어마다 각 토큰시 나오는 오디오 비디오 텍스트의 어텐션 값을 다 받음. 물론 합한 것만…

어차피 제대로 알려면 모델 단에서 다 부수고 들어가야해서 그건 이후에 어떻게 볼지 정하고 해도 될듯

### 104

#### 1

🟦 "question": "Is the woman making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "Yes, the woman is speaking into the microphone at the podium."

<p align="center"><img src="assets/f68cf1d8_02.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_03.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_04.png" alt="figure" width="720"></p>

<table><tr>
<td align="center" width="33%"><img src="assets/f68cf1d8_05.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_06.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_07.png" alt="figure" width="100%"></td>
</tr></table>

#### 2

🟥 "question": "Is the microphone making sound in the audio?",<br>"label": "No",<br>"generated_result": "Yes, the microphone is clearly visible and being used by the woman to amplify her voice during her speech."<br>

<p align="center"><img src="assets/f68cf1d8_08.jpg" alt="figure" width="720"></p>

#### 3

🟦 "question": "Is the podium making sound in the audio?",<br>"label": "No",<br>"generated_result": "No, the podium itself does not make any sound. It is a static object used for speeches."

<p align="center"><img src="assets/f68cf1d8_09.jpg" alt="figure" width="720"></p>

#### 4

🟦 "question": "Are the contexts of audio and visual content matching?",<br>"label": "Yes",<br>"generated_result": "Yes, they match well. The while the woman is speaking at the podium, she gestures with her right hand, and there's a backdrop of blue and red flags behind her."

<p align="center"><img src="assets/f68cf1d8_10.jpg" alt="figure" width="720"></p>

#### 5

🟧 "question": "Describe what you see and hear in a single sentence.",<br>"label": "In the video, a woman delivers a speech at an event, standing at a podium with a microphone in front of a flag.",<br>"generated_result": "A woman stands at a podium, speaking into an audience against a backdrop of large, colorful flags, while she shares her personal story about living in the hills of East Tennessee."

<p align="center"><img src="assets/f68cf1d8_11.jpg" alt="figure" width="720"></p>

<table><tr>
<td align="center" width="33%"><img src="assets/f68cf1d8_12.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_13.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_14.png" alt="figure" width="100%"></td>
</tr></table>

<p align="center"><img src="assets/f68cf1d8_15.png" alt="figure" width="720"></p>

### 105

#### 1

🟥 "question": "Are the contexts of audio and visual content matching?",<br>"label": "No",<br>"generated_result": "Yes."

<p align="center"><img src="assets/f68cf1d8_16.jpg" alt="figure" width="720"></p>

---

### 182

#### 1

🟦 "question": "Is the water making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "Yes."

<p align="center"><img src="assets/f68cf1d8_17.jpg" alt="figure" width="720"></p>

#### 2

🟦 "question": "Is the woman making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "Yes."

<p align="center"><img src="assets/f68cf1d8_18.jpg" alt="figure" width="720"></p>

#### 3

🟦 "question": "Is the water visible in the video?",<br>"label": "Yes",<br>"generated_result": "Yes, the water is visible as the woman swims and then she emerges from the water."

<p align="center"><img src="assets/f68cf1d8_19.jpg" alt="figure" width="720"></p>

<table><tr>
<td align="center" width="33%"><img src="assets/f68cf1d8_20.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_21.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_22.png" alt="figure" width="100%"></td>
</tr></table>

<p align="center"><img src="assets/f68cf1d8_23.png" alt="figure" width="720"></p>

#### 4

🟦 "question": "Is the woman visible in the video?",<br>"label": "Yes",<br>"generated_result": "Yes, the woman is swimming in a clear blue pool."

<p align="center"><img src="assets/f68cf1d8_24.jpg" alt="figure" width="720"></p>

#### 5

🟦 "question": "Describe what you see and hear in a single sentence.",<br>"label": "A young woman in a black bikini stands in a blue pool, splashing water as people speak in the distance and a faint whistle is heard.",<br>"generated_result": "A woman is swimming in a pool, smiling and adjusting her hair while the sound of water splashing can be heard."

<p align="center"><img src="assets/f68cf1d8_25.jpg" alt="figure" width="720"></p>

<table><tr>
<td align="center" width="33%"><img src="assets/f68cf1d8_26.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_27.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_28.png" alt="figure" width="100%"></td>
</tr></table>

<p align="center"><img src="assets/f68cf1d8_29.png" alt="figure" width="720"></p>

### 183

#### 1

🟥 "question": "Are the contexts of audio and visual content matching?",<br>"label": "No",<br>"generated_result": "Yes."

<p align="center"><img src="assets/f68cf1d8_30.jpg" alt="figure" width="720"></p>

---

### 249

#### 1

🟦 "question": "Is the emergency vehicle making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "Yes, the police motorcycle is making sound in the audio."

<p align="center"><img src="assets/f68cf1d8_31.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_32.png" alt="figure" width="720"></p>

#### 2

🟧 "question": "Describe what you see and hear in a single sentence.",<br>"label": "A cop in yellow riding a motorcycle down a city street with cars on the side of the road, as an emergency siren in the background.",<br>"generated_result": "A busy street scene unfolds with people walking, a police van, and a red double-decker bus."

<p align="center"><img src="assets/f68cf1d8_33.jpg" alt="figure" width="720"></p>

<table><tr>
<td align="center" width="33%"><img src="assets/f68cf1d8_34.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_35.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_36.png" alt="figure" width="100%"></td>
</tr></table>

<p align="center"><img src="assets/f68cf1d8_37.png" alt="figure" width="720"></p>

### 250

#### 1

🟦 "question": "Are the contexts of audio and visual content matching?",<br>"label": "No",<br>"generated_result": "No, they do not match. The audio features a man speaking, followed by music, a a loud bang, and then another loud bang, while the video shows a a busy street scene with police officers and a red double-decker bus."<br>

<p align="center"><img src="assets/f68cf1d8_38.png" alt="figure" width="720"></p>

---

### 297

#### 1

🟦 "question": "Is the water making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "Yes, the water is flowing and splashing, creating a soothing sound."

<p align="center"><img src="assets/f68cf1d8_39.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_40.png" alt="figure" width="720"></p>

#### 2

🟦 "question": "Is the fish tank making sound in the audio?",<br>"label": "No",<br>"generated_result": "No, the fish tank is not making any sound. The sound heard is the water being poured into fill the aquarium."

<p align="center"><img src="assets/f68cf1d8_41.jpg" alt="figure" width="720"></p>

#### 3

🟦 "question": "Are the contexts of audio and visual content matching?",<br>"label": "Yes",<br>"generated_result": "Yes."

<p align="center"><img src="assets/f68cf1d8_42.jpg" alt="figure" width="720"></p>

#### 4

🟧 "question": "Describe what you see and hear in a single sentence.",<br>"label": "The soothing sound of water trickling and dripping accompanies a bustling crowd's chatter, as a man captures a mesmerizing image of fish swimming in a large aquarium.",<br>"generated_result": "The video shows a close-up of a fish tank with water droplets on the glass, followed by a man speaking."

<p align="center"><img src="assets/f68cf1d8_43.jpg" alt="figure" width="720"></p>

### 298

#### 1

🟥 "question": "Are the contexts of audio and visual content matching?",<br>"label": "No",<br>"generated_result": "Yes, they do match each other well. The video shows a fish tank with water droplets on the glass, while the man's speaks about checking buttons and preview buttons."

<p align="center"><img src="assets/f68cf1d8_44.jpg" alt="figure" width="720"></p>

---

### 342

#### 1

🟥 "question": "Is the truck making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "No, there is no truck making sound in the audio."<br>

<p align="center"><img src="assets/f68cf1d8_45.jpg" alt="figure" width="720"></p>

#### 2

🟦 "question": "Is the street light making sound in the audio?",<br>"label": "No",<br>"generated_result": "No, the street light is not making any sound. It is just a bright light illuminating the road."<br>

<p align="center"><img src="assets/f68cf1d8_46.jpg" alt="figure" width="720"></p>

#### 3

🟦 "question": "Is the street making sound in the audio?",<br>"label": "No",<br>"generated_result": "No, there is no specific mention of the street making sound in the audio description."<br>

<p align="center"><img src="assets/f68cf1d8_47.jpg" alt="figure" width="720"></p>

#### 4

🟦 "question": "Is the truck visible in the video?",<br>"label": "Yes",<br>"generated_result": "Yes, the truck is visible on the left side of the frame."<br>

<p align="center"><img src="assets/f68cf1d8_48.jpg" alt="figure" width="720"></p>

#### 5

🟦 "question": "Is the emergency vehicle visible in the video?",<br>"label": "Yes",<br>"generated_result": "Yes, the emergency vehicle is visible with its its lights flashing."<br>

<p align="center"><img src="assets/f68cf1d8_49.jpg" alt="figure" width="720"></p>

#### 6

🟦 "question": "Are the contexts of audio and visual content matching?",<br>"label": "Yes",<br>"generated_result": "Yes."<br>

<p align="center"><img src="assets/f68cf1d8_50.jpg" alt="figure" width="720"></p>

#### 7

🟦 "question": "Describe what you see and hear in a single sentence.",<br>"label": "The chaotic night scene is filled with the deafening wail of an emergency siren and the roaring engine of a large truck as vehicles speed down the street.",<br>"generated_result": "A car drives down the road, its\\n\\tDescription: A\\n\\tA truck with flashing lights is parked on the side of the road, emitting a loud s\\n\\tDescription:"<br>

<p align="center"><img src="assets/f68cf1d8_51.jpg" alt="figure" width="720"></p>

### 343

#### 1

🟦 "question": "Are the contexts of audio and visual content matching?",<br>"label": "No",<br>"generated_result": "No, they do not match. The video shows a nighttime street scene with cars and traffic lights, while the audio features music playing."<br>

<p align="center"><img src="assets/f68cf1d8_52.png" alt="figure" width="720"></p>

---

### 401

#### 1

🟦 "question": "Is the toilet making sound in the audio?",<br>"label": "Yes",<br>"generated_result": "Yes, the toilet is flushing."

<p align="center"><img src="assets/f68cf1d8_53.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_54.png" alt="figure" width="720"></p>

#### 2

🟦 "question": "Is the toilet visible in the video?",<br>"label": "Yes",<br>"generated_result": "Yes, the video shows a close-up of a toilet with water flowing into create bubbles."

<p align="center"><img src="assets/f68cf1d8_55.jpg" alt="figure" width="720"></p>

<table><tr>
<td align="center" width="33%"><img src="assets/f68cf1d8_56.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_57.png" alt="figure" width="100%"></td>
<td align="center" width="33%"><img src="assets/f68cf1d8_58.png" alt="figure" width="100%"></td>
</tr></table>

<p align="center"><img src="assets/f68cf1d8_59.png" alt="figure" width="720"></p>

#### 3

🟥 "question": "Are the contexts of audio and visual content matching?",<br>"label": "Yes",<br>"generated_result": "No."

<p align="center"><img src="assets/f68cf1d8_60.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_61.png" alt="figure" width="720"></p>

#### 4

🟧 "question": "Describe what you see and hear in a single sentence.",<br>"label": "The loud buzzing and rustling sounds were accompanied by a toilet flushing, as water ran from a faucet into a glass in a bathroom with a white toilet and a red light.",<br>"generated_result": "A hand reaches out to touch the toilet handle, initiating the flushing process."

<p align="center"><img src="assets/f68cf1d8_62.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_63.png" alt="figure" width="720"></p>

### 402

#### 1

🟥 "question": "Are the contexts of audio and visual content matching?",<br>"label": "No",<br>"generated_result": "Yes, they do match each other well. The man describes the toilet flushing while water is running in the background."

<p align="center"><img src="assets/f68cf1d8_64.jpg" alt="figure" width="720"></p>

<p align="center"><img src="assets/f68cf1d8_65.png" alt="figure" width="720"></p>

---
<sub>[← video-SALMONN 2+ 환경 세팅](02_video_salmonn2plus_setup.md) · [📑 목차](../README.md) · [Video · Audio Hallucination 논문 서베이 →](04_video_audio_hallucination_survey.md)</sub>
