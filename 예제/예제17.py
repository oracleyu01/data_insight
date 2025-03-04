##▣ 예제17. 버블 차트(Bubble Chart)

## 1. 버블 차트(Bubble Chart)
버블 차트(Bubble Chart)는 산점도(Scatter Plot)와 유사하지만, 점의 크기를 추가하여 세 개의 변수를 동시에 표현할 수 있는 차트입니다.

## 1.1 버블 차트의 특징
- X축과 Y축을 이용해 두 개의 변수 표현
- 점(Bubble)의 크기를 이용해 세 번째 변수를 시각적으로 표현 가능
- 여러 변수 간의 관계를 한눈에 비교 가능

## 1.2 기본적인 버블 차트 그리기
Matplotlib을 사용하여 버블 차트를 만들 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
np.random.seed(0)
x = np.random.rand(30) * 100  # X축 데이터
y = np.random.rand(30) * 100  # Y축 데이터
size = np.random.rand(30) * 1000  # 버블 크기

# 버블 차트 그리기
plt.scatter(x, y, s=size, alpha=0.5, color='blue', edgecolors='black')
plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.title("기본 버블 차트")
plt.show()
```

## 1.3 색상과 투명도 조정
버블의 색상을 다르게 지정하고 투명도를 조정할 수 있습니다.
```python
colors = np.random.rand(30)  # 색상 설정
plt.scatter(x, y, s=size, c=colors, cmap='coolwarm', alpha=0.6, edgecolors='black')
plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.title("색상이 추가된 버블 차트")
plt.colorbar(label="색상 값")  # 색상 바 추가
plt.show()
```

## 1.4 여러 그룹을 포함한 버블 차트
Seaborn을 활용하면 그룹별로 다른 색상을 사용할 수 있습니다.
```python
import seaborn as sns
import pandas as pd

# 데이터프레임 생성
data = pd.DataFrame({
    "X": x,
    "Y": y,
    "크기": size,
    "그룹": np.random.choice(["A", "B", "C"], size=30)
})

# Seaborn을 활용한 버블 차트
sns.scatterplot(data=data, x="X", y="Y", size="크기", hue="그룹", palette="Set2", alpha=0.6)
plt.title("그룹별 버블 차트")
plt.show()
```

## 1.5 버블 차트의 활용 예시
- 마케팅 데이터에서 광고 예산(X)과 매출(Y), ROI(버블 크기) 비교
- 경제 데이터에서 나라별 GDP(X), 인구(Y), 무역량(버블 크기) 분석
- 센서 데이터에서 위치(X, Y) 및 측정값(버블 크기) 시각화

## 1.6 객관식 문제
다음 중 버블 차트를 생성하는 Matplotlib 함수는 무엇인가?

A) plt.bar()
B) plt.scatter()
C) plt.hist()
D) plt.boxplot()

정답: B
