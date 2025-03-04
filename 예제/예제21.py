##▣ 예제21. 시계열 데이터(Time Series) 시각화

## 1. 시계열 데이터(Time Series) 시각화
시계열 데이터(Time Series Data)는 시간에 따라 변하는 데이터를 의미하며, 주로 금융, 기후, 트래픽 분석 등에서 활용됩니다. 
시계열 데이터를 효과적으로 분석하기 위해 다양한 시각화 기법을 사용할 수 있습니다.

## 1.1 시계열 데이터 시각화의 중요성
- 데이터의 변동 패턴 및 트렌드를 한눈에 파악 가능
- 계절성(Seasonality) 및 이상치(Outlier) 탐지 가능
- 데이터 예측을 위한 기초 분석 도구로 활용 가능

## 1.2 기본적인 시계열 데이터 그래프 그리기
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 날짜 생성
date_range = pd.date_range(start="2023-01-01", periods=100, freq='D')

# 랜덤 데이터 생성
data = np.random.randn(100).cumsum()  # 누적합을 이용해 트렌드 생성

df = pd.DataFrame({"Date": date_range, "Value": data})

# 시계열 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Value"], linestyle='-', marker='o', color='b', label='값')
plt.xlabel("날짜")
plt.ylabel("값")
plt.title("기본 시계열 데이터 시각화")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.3 이동 평균을 활용한 시계열 데이터 스무딩
이동 평균(Moving Average)을 적용하면 데이터의 변동성을 줄이고 추세를 파악할 수 있습니다.
```python
# 이동 평균 계산
window_size = 7
df["Moving_Avg"] = df["Value"].rolling(window=window_size).mean()

# 이동 평균 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Value"], linestyle='-', marker='o', alpha=0.5, label='원본 데이터')
plt.plot(df["Date"], df["Moving_Avg"], linestyle='-', color='r', label=f'{window_size}일 이동 평균')
plt.xlabel("날짜")
plt.ylabel("값")
plt.title("이동 평균을 적용한 시계열 그래프")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.4 Seaborn을 활용한 시계열 시각화
Seaborn의 `lineplot()`을 활용하면 세련된 시계열 그래프를 쉽게 만들 수 있습니다.
```python
import seaborn as sns

sns.set(style="darkgrid")
sns.lineplot(x="Date", y="Value", data=df, label='값')
sns.lineplot(x="Date", y="Moving_Avg", data=df, label=f'{window_size}일 이동 평균', color='red')
plt.xticks(rotation=45)
plt.title("Seaborn을 활용한 시계열 시각화")
plt.show()
```

## 1.5 시계열 데이터의 이상치 탐지
이상치(Outlier)를 탐지하기 위해 특정 임계값을 기준으로 데이터를 시각화할 수 있습니다.
```python
threshold = df["Value"].mean() + 2 * df["Value"].std()

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Value"], label='값')
plt.axhline(y=threshold, color='r', linestyle='--', label='이상치 기준')
plt.xlabel("날짜")
plt.ylabel("값")
plt.title("이상치 탐지를 위한 시계열 그래프")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.6 시계열 데이터 시각화의 활용 예시
- 주식 시장 가격 변동 분석
- 기후 데이터(온도, 강수량 등) 변화 분석
- 웹사이트 트래픽 및 사용자 행동 패턴 분석

## 1.7 객관식 문제
다음 중 Seaborn에서 시계열 데이터를 시각화하는 데 가장 적합한 함수는 무엇인가?

A) sns.scatterplot()
B) sns.lineplot()
C) sns.boxplot()
D) sns.histplot()

정답: B
