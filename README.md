# 아이캔버스 [Backend-AI]

💡 아이들이 스케치를 그리면 생성형 AI가 이를 그림으로 변환해 주는 서비스입니다. 게임적인 요소를 더해 아이들이 스스로 자신만의 콘텐츠를 생성하면서 자신감과 창의력을 증진하고, 재미와 성취감을 경험할 수 있도록 합니다.

- 참고 문헌 : [Pix2Pix 프로젝트 페이지](https://phillipi.github.io/pix2pix/) | [Github](https://github.com/phillipi/pix2pix) | [Paper](https://arxiv.org/abs/1611.07004) | [HED paper](https://arxiv.org/abs/1504.06375)

<br>

## 서비스 예시 화면

- 작성중



- 모델의 결과를 보고 싶으신 분은 [사용한 데이터 Section](#사용한-데이터)을 참고해주세요.

<br>

## 데이터 전처리


※ <b>Distribution Mismatch</b>

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

