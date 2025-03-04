##▣ 예제38.  고급 상관 행렬(Advanced Correlation Matrix)

## 1. 고급 상관 행렬(Advanced Correlation Matrix)
상관 행렬(Correlation Matrix)은 변수 간의 상관관계를 분석하는 데 사용됩니다. Seaborn과 Matplotlib을 활용하여 고급 시각화를 구현할 수 있습니다.

## 1.1 상관 행렬의 특징
- 변수 간의 상관계수를 한눈에 확인 가능
- 양의 상관관계(1에 가까울수록 강한 양의 관계) 및 음의 상관관계(-1에 가까울수록 강한 음의 관계)를 분석 가능
- 색상과 숫자를 활용하여 가독성을 높일 수 있음

## 1.2 기본적인 상관 행렬 시각화
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 샘플 데이터 생성
data = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])

# 상관 행렬 계산
corr_matrix = data.corr()

# 기본 상관 행렬 시각화
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
plt.title("기본 상관 행렬")
plt.show()
```

## 1.3 마스킹을 활용한 대각선 제외 상관 행렬
대각선(자기 자신과의 상관관계)을 제외하고 분석할 수도 있습니다.
```python
# 마스킹 설정
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# 마스킹된 히트맵
sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f', mask=mask, linewidths=0.5)
plt.title("대각선 제외 상관 행렬")
plt.show()
```

## 1.4 상관 행렬을 클러스터링하여 그룹화
변수 간의 유사도를 기반으로 클러스터링할 수도 있습니다.
```python
sns.clustermap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
plt.title("클러스터링된 상관 행렬")
plt.show()
```

## 1.5 고급 스타일 적용
```python
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, cmap='RdYlBu', annot=True, fmt='.2f', linewidths=1, vmin=-1, vmax=1,
            cbar_kws={'shrink': 0.8, 'label': 'Correlation Coefficient'})
plt.title("스타일이 적용된 상관 행렬")
plt.show()
```

## 1.6 고급 상관 행렬의 활용 예시
- 금융 데이터에서 자산 간 상관관계 분석
- 유전자 데이터에서 특징 간의 관계 분석
- 마케팅 데이터에서 고객 행동 분석

## 1.7 객관식 문제
다음 중 Seaborn에서 상관 행렬을 시각화하는 함수는 무엇인가?

A) sns.lineplot()
B) sns.boxplot()
C) sns.heatmap()
D) sns.barplot()

정답: C
