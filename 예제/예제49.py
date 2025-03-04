##▣ 예제49. 대규모 데이터셋을 효율적으로 시각화하는 기법

"""
▣ 대규모 데이터셋을 효율적으로 시각화하는 기법

1. 대규모 데이터셋 시각화 개요
   대규모 데이터셋을 효과적으로 시각화하는 것은 데이터의 구조를 이해하고 패턴을 발견하는 데 중요한 역할을 한다. 하지만 데이터가 너무 크면 성능 저하, 시각적 혼잡 등의 문제가 발생할 수 있다.

1.1 대규모 데이터 시각화의 주요 도전 과제
   - 과부하 문제: 수백만 개의 데이터 포인트를 직접 플로팅하면 렌더링 속도가 느려짐
   - 가독성 문제: 데이터가 겹쳐져 패턴을 분석하기 어려움
   - 스토리지 문제: 시각화를 위해 데이터를 처리할 때 많은 메모리를 사용함
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

# 데이터 생성 (100만 개의 데이터)
np.random.seed(42)
data = pd.DataFrame({
    "x": np.random.rand(1_000_000),
    "y": np.random.rand(1_000_000)
})

"""
2. 대규모 데이터셋을 위한 주요 시각화 기법
2.1 샘플링(Sampling)
   데이터의 일부만 선택하여 시각화하는 방식으로, 전체 경향을 유지하면서 성능을 개선할 수 있다.
"""

# 샘플링 (1% 데이터만 선택)
sampled_data = data.sample(frac=0.01, random_state=42)

# 산점도 시각화
plt.figure(figsize=(8, 5))
plt.scatter(sampled_data["x"], sampled_data["y"], alpha=0.5)
plt.title("샘플링을 활용한 시각화")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""
2.2 히트맵(Heatmap)
   많은 데이터 포인트가 존재할 때, 밀도를 나타내는 방식이다.
"""

# 2D 히스토그램 (Hexbin Plot)
plt.figure(figsize=(8, 5))
plt.hexbin(data["x"], data["y"], gridsize=50, cmap="Blues")
plt.colorbar(label="Count")
plt.title("히트맵을 활용한 데이터 시각화")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""
2.3 KDE(커널 밀도 추정, Kernel Density Estimation)
   밀도 기반 시각화로, 데이터가 집중된 영역을 쉽게 확인할 수 있다.
"""

plt.figure(figsize=(8, 5))
sns.kdeplot(x=data["x"], y=data["y"], cmap="Reds", fill=True)
plt.title("KDE Plot을 활용한 데이터 밀도 시각화")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""
2.4 데이터 집계(Aggregation)
   수백만 개의 데이터 포인트를 직접 표시하는 대신, 특정 그룹별로 평균이나 합계를 표시하는 방식이다.
"""

# x 축을 100개의 구간으로 나눠 그룹별 평균 계산
data["x_bin"] = pd.cut(data["x"], bins=100)
aggregated = data.groupby("x_bin")["y"].mean()

# 집계된 데이터 시각화
plt.figure(figsize=(8, 5))
aggregated.plot(kind="bar", width=1.0)
plt.title("데이터 집계를 활용한 시각화")
plt.xlabel("X 구간")
plt.ylabel("Y 평균")
plt.show()

"""
2.5 이상치 탐지(Anomaly Detection) 및 시각화
   이상치 탐지는 정상 데이터 패턴에서 벗어난 데이터를 식별하는 과정이다.
"""

# IQR 계산
Q1 = data["y"].quantile(0.25)
Q3 = data["y"].quantile(0.75)
IQR = Q3 - Q1

# 이상치 기준 설정
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 이상치 탐지
outliers = (data["y"] < lower_bound) | (data["y"] > upper_bound)
print(f"이상치 개수: {outliers.sum()}")

"""
2.6 Isolation Forest를 활용한 이상치 탐지
   머신러닝 기반의 이상치 탐지 기법 중 하나로, 대규모 데이터에서 이상치를 빠르게 탐지할 수 있다.
"""

# Isolation Forest 모델 학습
iso_forest = IsolationForest(contamination=0.01, random_state=42)
outlier_pred = iso_forest.fit_predict(data[["x", "y"]])

# 이상치 시각화
plt.figure(figsize=(8, 5))
sns.scatterplot(x=data["x"], y=data["y"], hue=outlier_pred, palette={1: "blue", -1: "red"})
plt.title("Isolation Forest 기반 이상치 탐지")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(["정상", "이상치"])
plt.show()

"""
3. 대규모 데이터셋 시각화 기법의 활용 예시
   - 금융 데이터 분석: 대규모 트랜잭션 데이터를 샘플링하여 사기 거래 탐지
   - SNS 데이터 분석: 수백만 개의 사용자 데이터를 히트맵으로 표현하여 트렌드 파악
   - IoT 센서 데이터 분석: 실시간 스트리밍 데이터를 KDE 플롯으로 표현하여 패턴 분석

4. 객관식 문제
   다음 중 대규모 데이터셋을 효과적으로 시각화하는 방법으로 적절하지 않은 것은?

   A) 데이터 샘플링을 활용하여 일부만 시각화한다.
   B) 밀도를 표현하는 히트맵을 활용한다.
   C) 모든 데이터를 플롯에 직접 그려서 표현한다.
   D) 데이터 집계를 활용하여 그룹별 평균을 구해 표현한다.

   정답: C
"""
