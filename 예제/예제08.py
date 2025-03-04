##▣ 예제8. 히스토그램(Histogram)

## 1. 히스토그램(Histogram)
히스토그램(Histogram)은 데이터의 분포를 시각적으로 표현하는 그래프입니다. 특정 구간(bin)별 데이터 개수를 나타내며, 연속형 데이터의 밀도와 분포를 파악하는 데 유용합니다.

## 1.1 히스토그램의 특징
- 연속형 데이터의 분포를 분석하는 데 사용됨
- 특정 구간(bin) 내 데이터 개수를 시각적으로 표현
- 이상치(outlier) 탐지 및 데이터 패턴 분석에 활용 가능

## 1.2 기본적인 히스토그램 그리기
Matplotlib을 사용하여 간단한 히스토그램을 그릴 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 랜덤 데이터 생성
data = np.random.randn(1000)  # 평균 0, 표준편차 1을 따르는 정규분포 데이터

# 히스토그램 그리기
plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.xlabel("값")
plt.ylabel("빈도수")
plt.title("기본 히스토그램")
plt.show()
```

## 1.3 히스토그램의 bin 개수 조정
bin 개수를 조정하면 데이터 분포를 더 세밀하게 혹은 더 넓게 볼 수 있습니다.
```python
plt.hist(data, bins=10, color='green', edgecolor='black', alpha=0.7)
plt.title("Bin 개수 10인 히스토그램")
plt.show()
```
```python
plt.hist(data, bins=50, color='red', edgecolor='black', alpha=0.7)
plt.title("Bin 개수 50인 히스토그램")
plt.show()
```

## 1.4 히스토그램과 커널 밀도 추정(KDE) 추가
Seaborn을 활용하면 히스토그램과 KDE(Kernel Density Estimation)를 함께 표현할 수 있습니다.
```python
import seaborn as sns
sns.histplot(data, bins=30, kde=True, color='purple')
plt.title("히스토그램 + KDE 그래프")
plt.show()
```

## 1.5 여러 개의 히스토그램 비교
다중 데이터를 비교할 때 여러 히스토그램을 한 그래프에 그릴 수 있습니다.
```python
data1 = np.random.randn(1000) * 0.5 + 2  # 평균 2, 표준편차 0.5
data2 = np.random.randn(1000) * 1.0 + 5  # 평균 5, 표준편차 1.0

plt.hist(data1, bins=30, alpha=0.5, label='Data 1', color='blue')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2', color='red')
plt.xlabel("값")
plt.ylabel("빈도수")
plt.title("두 개의 히스토그램 비교")
plt.legend()
plt.show()
```

## 1.6 히스토그램의 활용 예시
- 시험 성적 분포 분석
- 연령별 고객 분포 파악
- 센서 데이터의 이상 탐지

## 1.7 객관식 문제
다음 중 히스토그램을 생성하는 Matplotlib 함수는 무엇인가?

A) plt.bar()
B) plt.scatter()
C) plt.hist()
D) plt.plot()

정답: C
