##▣ 예제16. 히트맵(Heatmap)

## 1. 히트맵(Heatmap)
히트맵(Heatmap)은 2차원 데이터의 값을 색상으로 표현하는 그래프입니다. 주로 데이터의 상관관계 분석, 패턴 탐색, 행렬 데이터 시각화 등에 사용됩니다.

## 1.1 히트맵의 특징
- 데이터의 패턴 및 관계를 한눈에 파악 가능
- 색상의 강도를 이용해 값의 크기를 표현
- 주로 상관관계 행렬, 카운트 데이터, 공간적 데이터 분석에 활용

## 1.2 기본적인 히트맵 그리기
Seaborn의 `heatmap()` 함수를 사용하여 히트맵을 생성할 수 있습니다.
```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 랜덤 데이터 생성
data = np.random.rand(10, 10)  # 10x10 행렬 데이터

# 히트맵 그리기
sns.heatmap(data, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("기본 히트맵")
plt.show()
```

## 1.3 상관관계 행렬 히트맵
히트맵은 데이터프레임의 변수 간 상관관계를 시각화하는 데 자주 사용됩니다.
```python
import pandas as pd

# 샘플 데이터 생성
df = sns.load_dataset("iris")
corr_matrix = df.corr()  # 상관관계 행렬 계산

# 상관관계 히트맵 그리기
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, fmt=".2f", linewidths=0.5)
plt.title("상관관계 행렬 히트맵")
plt.show()
```

## 1.4 히트맵의 색상 조정
히트맵의 색상을 변경하여 데이터를 강조할 수 있습니다.
```python
sns.heatmap(data, cmap="viridis", annot=True)
plt.title("색상이 변경된 히트맵")
plt.show()
```

## 1.5 히트맵에서 축 조정 및 라벨 추가
```python
sns.heatmap(data, cmap="Blues", xticklabels=range(1, 11), yticklabels=range(1, 11))
plt.xlabel("X축 레이블")
plt.ylabel("Y축 레이블")
plt.title("축 레이블이 추가된 히트맵")
plt.show()
```

## 1.6 대각선 히트맵 마스킹
상관관계 행렬에서 대각선을 제외하고 시각화할 수 있습니다.
```python
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # 상삼각행렬 마스킹
sns.heatmap(corr_matrix, mask=mask, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("대각선이 마스킹된 히트맵")
plt.show()
```

## 1.7 히트맵의 활용 예시
- 변수 간 상관관계 분석
- 시간별 또는 지역별 데이터 분포 분석
- 웹사이트 방문자 행동 패턴 분석

## 1.8 객관식 문제
다음 중 Seaborn에서 히트맵을 그리는 함수는 무엇인가?

A) sns.barplot()
B) sns.scatterplot()
C) sns.heatmap()
D) sns.boxplot()

정답: C
