##▣ 예제37.  회귀 분석 결과 시각화 (Seaborn regplot 활용)

## 1. 회귀 분석 결과 시각화 (Seaborn regplot 활용)
회귀 분석(Regression Analysis)은 변수 간의 관계를 분석하는 기법으로, 데이터의 패턴을 예측하는 데 활용됩니다. Seaborn의 `regplot`을 사용하면 회귀선을 포함한 시각화를 쉽게 구현할 수 있습니다.

## 1.1 회귀 분석 시각화의 특징
- 두 변수 간의 관계를 그래프 형태로 표현
- 회귀선을 추가하여 데이터의 패턴을 예측 가능
- 이상치(Outlier) 및 트렌드 분석 가능

## 1.2 기본적인 Seaborn regplot 사용법
Seaborn의 `regplot()`을 활용하여 회귀선을 포함한 산점도를 그릴 수 있습니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 샘플 데이터 생성
data = pd.DataFrame({
    "광고비": np.random.uniform(10, 100, 50),
    "매출": np.random.uniform(500, 2000, 50) + np.random.normal(0, 100, 50)  # 노이즈 추가
})

# 회귀 분석 그래프 그리기
sns.regplot(x="광고비", y="매출", data=data, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("광고비 vs 매출 회귀 분석")
plt.xlabel("광고비")
plt.ylabel("매출")
plt.show()
```

## 1.3 다항 회귀선을 추가한 회귀 분석
선형 회귀 외에도 다항 회귀를 적용할 수 있습니다.
```python
sns.regplot(x="광고비", y="매출", data=data, order=2, scatter_kws={"color": "blue"}, line_kws={"color": "green"})
plt.title("다항 회귀 분석")
plt.show()
```

## 1.4 그룹별 회귀 분석
여러 그룹의 데이터에 대해 회귀선을 비교할 수도 있습니다.
```python
# 그룹 추가
data["채널"] = np.random.choice(["TV", "온라인", "SNS"], size=len(data))

# 그룹별 회귀 분석
sns.lmplot(x="광고비", y="매출", hue="채널", data=data)
plt.title("채널별 광고비 vs 매출 회귀 분석")
plt.show()
```

## 1.5 회귀 분석 시각화의 활용 예시
- 마케팅 분석(광고비와 매출 간의 관계 분석)
- 금융 데이터(투자 금액과 수익률 관계 분석)
- 의료 데이터(운동량과 체중 감소율 간의 관계 분석)

## 1.6 객관식 문제
다음 중 Seaborn에서 회귀선을 추가하여 데이터를 시각화하는 함수는 무엇인가?

A) sns.scatterplot()
B) sns.regplot()
C) sns.barplot()
D) sns.heatmap()

정답: B
