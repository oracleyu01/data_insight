##▣ 예제48. 머신러닝 모델의 Feature Importance 시각화

## 1. 머신러닝 모델의 Feature Importance 시각화
Feature Importance(특성 중요도)는 머신러닝 모델이 예측을 수행하는 데 있어 어떤 특성이 중요한지를 나타내는 지표입니다. 이를 시각화하면 모델의 해석 가능성을 높이고, 성능 최적화를 위한 인사이트를 얻을 수 있습니다.

## 1.1 Feature Importance의 특징
- 모델이 특정 변수를 얼마나 중요하게 활용하는지 평가 가능
- 특성 선택(Feature Selection) 및 모델 최적화에 도움을 줌
- 결정 트리, 랜덤 포레스트, 부스팅 계열 모델에서 자주 활용됨

## 1.2 머신러닝 모델 학습 및 Feature Importance 계산
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# 데이터 로드
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# 랜덤 포레스트 모델 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(df, y)

# Feature Importance 추출
feature_importance = model.feature_importances_
features = df.columns
```

## 1.3 Feature Importance 시각화
```python
# 중요도 데이터프레임 생성
importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": feature_importance
}).sort_values(by="Importance", ascending=False)

# 막대 그래프 시각화
plt.figure(figsize=(8, 5))
plt.barh(importance_df["Feature"], importance_df["Importance"], color="skyblue")
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.title("Feature Importance Visualization")
plt.gca().invert_yaxis()
plt.grid()
plt.show()
```

## 1.4 SHAP(Shapley Values) 기반 Feature Importance 시각화
SHAP(Shapley Additive Explanations)은 모델의 개별 예측을 설명하는 강력한 방법입니다.
```python
import shap

# SHAP 값 계산
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(df)

# SHAP Summary Plot
shap.summary_plot(shap_values, df, feature_names=features)
```

## 1.5 Feature Importance 시각화의 활용 예시
- 모델 해석 가능성 향상 및 의사 결정 지원
- 중요도가 낮은 변수를 제거하여 성능 개선
- 비즈니스 인사이트 도출(예: 고객 행동 분석에서 주요 변수 탐색)

## 1.6 이상치 탐지(Anomaly Detection) 및 시각화
이상치 탐지는 정상 데이터 패턴에서 벗어난 데이터를 식별하는 과정으로, 데이터 정제 및 보안 시스템에서 중요한 역할을 합니다.

### 1.6.1 이상치 탐지 방법
- **통계적 방법**: IQR(사분위 범위), 표준 편차 활용
- **머신러닝 기반**: Isolation Forest, One-Class SVM 등
- **딥러닝 기반**: 오토인코더 활용

### 1.6.2 IQR(Interquartile Range)을 활용한 이상치 탐지
```python
# IQR 계산
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# 이상치 기준 설정
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 이상치 탐지
outliers = (df < lower_bound) | (df > upper_bound)
print(outliers.sum())
```

### 1.6.3 이상치 탐지 시각화 (Box Plot 활용)
```python
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.boxplot(data=df)
plt.title("Box Plot을 활용한 이상치 탐지")
plt.show()
```

### 1.6.4 Isolation Forest를 활용한 이상치 탐지
```python
from sklearn.ensemble import IsolationForest

# Isolation Forest 모델 학습
iso_forest = IsolationForest(contamination=0.05, random_state=42)
outlier_pred = iso_forest.fit_predict(df)

# 이상치 시각화
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df.iloc[:, 0], y=df.iloc[:, 1], hue=outlier_pred, palette={1: "blue", -1: "red"})
plt.title("Isolation Forest 기반 이상치 탐지")
plt.show()
```

## 1.7 이상치 탐지 및 Feature Importance의 활용 예시
- 금융 데이터의 이상 거래 탐지
- 제조업 공정 데이터의 이상 현상 탐지
- 사이버 보안 및 네트워크 이상 감지

## 1.8 객관식 문제
다음 중 이상치 탐지를 수행하는 데 사용할 수 있는 머신러닝 기법은 무엇인가?

A) 선형 회귀 (Linear Regression)
B) 랜덤 포레스트 (Random Forest)
C) Isolation Forest
D) K-평균 클러스터링 (K-Means Clustering)

정답: C
