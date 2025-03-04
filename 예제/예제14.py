##▣ 예제14. 커널 밀도 그래프(KDE Plot)

## 1. 커널 밀도 그래프(KDE Plot)
커널 밀도 그래프(KDE Plot, Kernel Density Estimation Plot)는 데이터의 분포를 부드러운 곡선 형태로 시각화하는 그래프입니다. 이는 히스토그램과 유사하지만, 연속적인 확률 밀도 함수를 제공한다는 점에서 차이가 있습니다.

## 1.1 커널 밀도 그래프의 특징
- 데이터의 분포를 부드러운 곡선 형태로 표현
- 히스토그램보다 매끄럽고 연속적인 데이터 패턴 제공
- 확률 밀도 함수를 기반으로 데이터의 밀집도를 파악 가능

## 1.2 기본적인 KDE 그래프 그리기
Seaborn을 사용하여 간단한 KDE 그래프를 생성할 수 있습니다.
```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 랜덤 데이터 생성
data = np.random.randn(1000)  # 평균 0, 표준편차 1을 따르는 정규분포 데이터

# KDE 그래프 그리기
sns.kdeplot(data, shade=True, color='blue')
plt.title("기본 KDE 그래프")
plt.show()
```

## 1.3 히스토그램과 KDE 그래프 함께 그리기
```python
sns.histplot(data, bins=30, kde=True, color='purple', alpha=0.6)
plt.title("히스토그램 + KDE 그래프")
plt.show()
```

## 1.4 여러 개의 KDE 그래프 비교
여러 개의 데이터셋을 한 그래프에서 비교할 수도 있습니다.
```python
data1 = np.random.randn(1000) * 0.5 + 2  # 평균 2, 표준편차 0.5
data2 = np.random.randn(1000) * 1.0 + 5  # 평균 5, 표준편차 1.0

sns.kdeplot(data1, shade=True, color='blue', label='Data 1')
sns.kdeplot(data2, shade=True, color='red', label='Data 2')
plt.title("두 개의 KDE 그래프 비교")
plt.legend()
plt.show()
```

## 1.5 KDE 그래프의 밴드너비(Bandwidth) 조정
밴드너비(bandwidth)는 커널 밀도의 부드러움을 결정하는 중요한 요소입니다.
```python
sns.kdeplot(data, bw_adjust=0.5, label='Bandwidth = 0.5', linestyle='--')
sns.kdeplot(data, bw_adjust=1, label='Bandwidth = 1')
sns.kdeplot(data, bw_adjust=2, label='Bandwidth = 2', linestyle=':')
plt.title("밴드너비 조정에 따른 KDE 그래프 변화")
plt.legend()
plt.show()
```

## 1.6 다변량 KDE 그래프 (2D 밀도 그래프)
KDE는 2차원 데이터에서도 활용할 수 있습니다.
```python
data_x = np.random.randn(1000)
data_y = np.random.randn(1000) + 2  # Y축 데이터는 2만큼 이동

sns.kdeplot(x=data_x, y=data_y, cmap="Blues", fill=True)
plt.title("2D KDE 그래프")
plt.show()
```

## 1.7 KDE 그래프의 활용 예시
- 데이터의 분포 파악 및 이상치 탐지
- 정규 분포 여부 확인
- 여러 그룹 간의 데이터 밀도 비교

## 1.8 객관식 문제
다음 중 Seaborn에서 KDE 그래프를 그리는 함수는 무엇인가?

A) sns.histplot()
B) sns.scatterplot()
C) sns.kdeplot()
D) sns.boxplot()

정답: C
