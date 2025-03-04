##▣ 예제9. 산점도(Scatter Plot)

## 1. 산점도(Scatter Plot)
산점도(Scatter Plot)는 두 변수 간의 관계를 시각적으로 표현하는 그래프입니다. 주로 상관관계 분석 및 데이터 패턴을 파악하는 데 사용됩니다.

## 1.1 산점도의 특징
- 두 개의 연속형 변수 간 관계를 표현
- 상관관계(양의 상관, 음의 상관, 무상관) 파악 가능
- 데이터의 분포와 이상치 탐지에 유용함

## 1.2 기본적인 산점도 그리기
Matplotlib을 사용하여 간단한 산점도를 만들 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 랜덤 데이터 생성
np.random.seed(0)
x = np.random.rand(100) * 10  # X 값 (0~10 사이)
y = x * 2 + np.random.randn(100) * 2  # Y 값 (X와 상관이 있는 데이터)

# 산점도 그리기
plt.scatter(x, y, color='blue', alpha=0.5)
plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.title("기본 산점도")
plt.show()
```

## 1.3 색상 및 마커 스타일 변경
산점도에서 색상과 마커 스타일을 조정할 수 있습니다.
```python
plt.scatter(x, y, c='red', marker='^', alpha=0.7)
plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.title("색상 및 마커 스타일 변경")
plt.show()
```

## 1.4 산점도에 크기(size) 추가
데이터의 중요도나 추가적인 정보를 반영하기 위해 점의 크기를 조절할 수 있습니다.
```python
size = np.random.rand(100) * 300  # 랜덤 크기 설정
plt.scatter(x, y, s=size, c='green', alpha=0.5)
plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.title("크기가 추가된 산점도")
plt.show()
```

## 1.5 여러 개의 그룹을 가진 산점도
데이터를 그룹별로 구분하여 시각화할 수 있습니다.
```python
categories = np.random.choice([0, 1, 2], size=100)  # 세 개의 그룹 생성
colors = ['red', 'blue', 'green']

for i in range(3):
    plt.scatter(x[categories == i], y[categories == i], label=f'Group {i}', alpha=0.6)

plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.title("그룹별 산점도")
plt.legend()
plt.show()
```

## 1.6 Seaborn을 활용한 산점도 그리기
Seaborn을 사용하면 좀 더 세련된 스타일의 산점도를 쉽게 만들 수 있습니다.
```python
import seaborn as sns

df = sns.load_dataset("penguins")  # 펭귄 데이터셋 사용
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", hue="species", data=df)
plt.title("Seaborn을 활용한 산점도")
plt.show()
```

## 1.7 산점도의 활용 예시
- 두 변수 간의 관계 분석 (예: 키와 몸무게)
- 주식 시장에서 가격 변동 패턴 분석
- 센서 데이터에서 이상치 탐지

## 1.8 객관식 문제
다음 중 산점도를 생성하는 Matplotlib 함수는 무엇인가?

A) plt.plot()
B) plt.bar()
C) plt.scatter()
D) plt.hist()

정답: C
