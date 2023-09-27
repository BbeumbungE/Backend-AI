# 아이캔버스 [Backend-AI]

💡 아이들이 스케치를 그리면 생성형 AI가 이를 그림으로 변환해 주는 서비스입니다. 게임적인 요소를 더해 아이들이 스스로 자신만의 콘텐츠를 생성하면서 자신감과 창의력을 증진하고, 재미와 성취감을 경험할 수 있도록 합니다.

- 참고 문헌 : [Pix2Pix 프로젝트 페이지](https://phillipi.github.io/pix2pix/) | [Github](https://github.com/phillipi/pix2pix) | [Paper](https://arxiv.org/abs/1611.07004) | [HED paper](https://arxiv.org/abs/1504.06375)

<br>

## 서비스 예시 화면

- 작성중



- 모델의 결과를 보고 싶으신 분은 [사용한 데이터 Section](#사용한-데이터)을 참고해주세요.

<br>

## AI 파트의 목표

🚩 궁극적인 목표 : 서비스의 핵심 기능 중 하나인 그린 스케치를 해당 그림으로 변환해주는 generator 학습 <br>

- 이를 달성하기 위해서 해야할 일
  - 데이터 수집
  - 데이터 전처리
  - 모델 학습
  - 모델 비교 & checkpoint 결정
  - FastAPI 서버에 모델 띄우기

<br>

## 데이터 전처리

- 많은 경우에 이미지 데이터와 해당하는 edge가 함께 제공되지 않습니다.
- 이미지 수가 많기에 이를 직접 그리는 것은 현실적으로 어려우니, pix2pix 저자들의 implementation을 참고, [HED(Holistically-Nested Edge Detection)](https://github.com/s9xie/hed)로 edge를 추출한 뒤, post-processing 작업을 거쳤습니다.
  - [pix2pix github](https://github.com/phillipi/pix2pix)의 Extracting Edges Section을 참고해주세요

<br>

- 결론적으로 저렇게 이어붙여서 학습 시에 불러오게 됩니다
- 예시 이미지 : [DVM Car Dataset](https://deepvisualmarketing.github.io/), bmw series 5
![combined bmw](./docs%20images/combined_bmw.jpg)

<br>

※ <b>Distribution Mismatch</b>

- 학습을 시키는 데이터는 HED에 의해 자동으로 추출된 edge인데, 실제 사용자가 이를 따라 그리기는 현실적으로 어렵습니다.
- 그래서 학습시키는 데이터와 궁극적으로 적용하고자 하는 데이터에 <b>distribution mismatch</b>가 발생하는데, 일반적으로 이는 실제 적용 시에서의 성능 저하를 초래할 수 있다는 점을 짚고 넘어가야 합니다.

<br>

- 그렇다 하더라도 저희가 궁극적으로 원하는 것은 유저가 그린 edge를 잘 변환해주는 generator이기 때문에 저희는 직접 edge를 그려서 유저가 잠재적으로 그릴 만한, 그릴 수 있는 수준의 edge를 기준으로 결과를 비교해서 모델을 선정했습니다.

| HED에 의해 자동으로 추출된 edge | 직접 그려본 edge |
| :---: | :---: |
|![edge_hed](./docs%20images/bmw_edge_hed.jpeg)|![edge_drawn](./docs%20images/bmw_edge_drawn.jpg)|

- 저자들도 마찬가지로 이를 유념하여, paper 부록에 학습 데이터에 대한 결과 뿐만 아니라, 사람이 그린 데이터에 대한 결과도 함께 첨부했습니다.

<br>

## 모델 소개

<br>

## 사용한 데이터

### Cartoon set
- 출처 : [구글의 cartoon set](https://google.github.io/cartoonset/)
- 데이터 수 : 9996 (원본 10만 개 중에서 일부를 추출하여 수행)
- batch 사이즈 : 4
- 학습시킨 epoch 수 : 28
- 특이사항
  - 성능 개선을 위해서 color 정보를 condition으로 추가해 보기도 하고, 데이터의 수를 늘려보기도 하였으나(10만 개, 원본 데이터 전부), 사용자가 그린 edge에 대한 변환 성능에 이렇다 할 개선점이 보이지 않음 (학습 데이터는 굉장히 잘 변환)
- 예시 결과
![cartoon set 예시 결과 이미지](./docs%20images/cartoon_set.png)

<br>

### Panda
- 출처 : [Kaggle, Panda or Bear Image Classification](https://www.kaggle.com/datasets/mattop/panda-or-bear-image-classification)
- 데이터 수 : 300 (곰 데이터는 제외하고, 판다 데이터만 사용)
- batch 사이즈 : 1
- 학습 시킨 epoch 수 : 180
- 예시 결과
![panda 예시 결과 이미지](./docs%20images/panda.png)

### Car
- 출처 : [DVM car dataset](https://deepvisualmarketing.github.io/)
- 데이터 수 : 11476 (DVM car dataset에서 세단 형의 bmw series 5 & 7만 추출)
- batch 사이즈 : 4
- 학습 시킨 epoch 수 : 19
- 예시 결과
![car 예시 결과 이미지](./docs%20images/bmw.png)

### Handbags
- 출처 : [저자들이 사용했던 데이터셋](http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/)
- 데이터 수 : 138567
- batch 사이즈 : 4
- 학습 시킨 epoch 수 : 5
- 예시 결과
![handbag 예시 결과 이미지](./docs%20images/handbag.png)

### Shoes
- 출처 : [저자들이 사용했던 데이터셋](http://efrosgans.eecs.berkeley.edu/pix2pix/datasets/)
- 데이터 수 : 49825
- batch 사이즈 : 4
- 학습 시킨 epoch 수 : 25
- 예시 결과
![show 예시 결과 이미지](./docs%20images/shoe.png)

### Maplestory Characters
- 출처 : [Kaggle, maplestory_characters_hd](https://www.kaggle.com/datasets/irotem98/maplestory-characters-hd)
- 데이터 수 : 69372
- batch 사이즈 : 4
- 학습 시킨 epoch 수 : 14
- 예시 결과
![maplestory character 예시 결과 이미지](./docs%20images/maple_character.png)

### Gemstone
- 출처 : [Kaggle, Gemstones Images](https://www.kaggle.com/datasets/lsind18/gemstones-images)
- 데이터 수 : 3219
- batch 사이즈 : 4
- 학습 시킨 epoch 수 : 대략 36
- 예시 결과
![gemstone 예시 결과 이미지](./docs%20images/gemstone%20result.jpg)

### Space
- 출처 : [Kaggle, Cosmos Images](https://www.kaggle.com/datasets/kimbosoek/cosmos-images)
- 데이터 수 : 4649
- batch 사이즈 : 4
- 학습 시킨 epoch 수 : 40
- 예시 결과
![space 예시 결과 이미지](./docs%20images/space%20result.jpg)