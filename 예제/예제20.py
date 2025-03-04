## ##▣ 예제20. Boxen Plot을 활용한 데이터 분포 분석

## 1. Boxen Plot을 활용한 데이터 분포 분석
Boxen Plot(박스엔 플롯)은 박스 플롯(Box Plot)과 유사하지만, 극단값을 포함한 대량의 데이터를 보다 효과적으로 시각화할 수 있도록 설계된 그래프입니다. 

## 1.1 Boxen Plot의 특징
- 박스 플롯보다 많은 데이터 범위를 효과적으로 표현
- 이상치(outlier)와 데이터의 분포를 더 정밀하게 분석 가능
- 특히 데이터 개수가 많고, 긴 꼬리를 가진 분포에서 유용

## 1.2 Boxen Plot 그리기
Seaborn의 `boxenplot()`을 사용하여 Boxen Plot을 생성할 수 있습니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 예제 데이터 생성
data = np.random.exponential(scale=2, size=1000)  # 긴 꼬리를 가진 데이터

# Boxen Plot 그리기
sns.boxenplot(y=data)
plt.title("기본 Boxen Plot")
plt.show()
```

## 1.3 여러 그룹의 Boxen Plot 그리기
여러 개의 범주형 데이터를 비교하는 데 사용할 수 있습니다.
```python
# 샘플 데이터셋 로드
df = sns.load_dataset("diamonds")

# Boxen Plot 그리기
sns.boxenplot(x="cut", y="price", data=df, palette="Set3")
plt.title("다이아몬드 등급별 가격 분포 Boxen Plot")
plt.show()
```

## 1.4 Box Plot과 Boxen Plot 비교
Boxen Plot은 데이터 분포를 더 자세하게 표현할 수 있습니다.
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(x="cut", y="price", data=df, ax=axes[0], palette="pastel")
axes[0].set_title("Box Plot")

sns.boxenplot(x="cut", y="price", data=df, ax=axes[1], palette="Set2")
axes[1].set_title("Boxen Plot")

plt.show()
```

## 1.5 Boxen Plot의 활용 예시
- 긴 꼬리를 가진 데이터의 분포 분석 (예: 소득 분포, 부동산 가격 등)
- 대량의 데이터를 다룰 때 이상치(outlier) 탐색
- 그룹 간의 데이터 분포 비교

## 1.6 객관식 문제
다음 중 Seaborn에서 Boxen Plot을 생성하는 함수는 무엇인가?

A) sns.boxplot()
B) sns.violinplot()
C) sns.boxenplot()
D) sns.histplot()

정답: C
