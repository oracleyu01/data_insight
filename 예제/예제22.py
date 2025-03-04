##▣ 예제22. 이동 평균 그래프 및 트렌드 분석

## 1. 이동 평균 그래프 및 트렌드 분석
이동 평균(Moving Average)은 시계열 데이터에서 변동성을 줄이고 장기적인 추세를 분석하는 데 사용됩니다. 이를 활용하면 노이즈를 제거하고 데이터의 트렌드를 더 명확하게 확인할 수 있습니다.

## 1.1 이동 평균의 특징
- 데이터의 변동성을 줄여 장기적인 추세 파악 가능
- 단기(Short-term)와 장기(Long-term) 이동 평균을 비교하여 트렌드 분석 가능
- 금융(주가, 환율), 기후 데이터, 수요 예측 등에 활용

## 1.2 기본적인 이동 평균 계산 및 시각화
Matplotlib을 사용하여 이동 평균을 적용한 시계열 그래프를 생성할 수 있습니다.
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 날짜 생성
date_range = pd.date_range(start="2023-01-01", periods=100, freq='D')

# 랜덤 데이터 생성
data = np.random.randn(100).cumsum()  # 누적합을 이용해 트렌드 생성

df = pd.DataFrame({"Date": date_range, "Value": data})

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

## 1.3 단기 및 장기 이동 평균 비교
단기 이동 평균(Short Moving Average)과 장기 이동 평균(Long Moving Average)을 함께 비교하여 트렌드를 분석할 수 있습니다.
```python
# 단기 및 장기 이동 평균 계산
short_window = 7
long_window = 30
df["Short_MA"] = df["Value"].rolling(window=short_window).mean()
df["Long_MA"] = df["Value"].rolling(window=long_window).mean()

# 이동 평균 비교 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Value"], linestyle='-', alpha=0.3, label='원본 데이터')
plt.plot(df["Date"], df["Short_MA"], linestyle='-', color='blue', label=f'{short_window}일 이동 평균')
plt.plot(df["Date"], df["Long_MA"], linestyle='-', color='red', label=f'{long_window}일 이동 평균')
plt.xlabel("날짜")
plt.ylabel("값")
plt.title("단기 및 장기 이동 평균 비교")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.4 Seaborn을 활용한 이동 평균 그래프
Seaborn의 `lineplot()`을 사용하면 더욱 세련된 그래프를 만들 수 있습니다.
```python
import seaborn as sns

sns.set(style="darkgrid")
sns.lineplot(x="Date", y="Value", data=df, label='원본 데이터', alpha=0.4)
sns.lineplot(x="Date", y="Short_MA", data=df, label=f'{short_window}일 이동 평균', color='blue')
sns.lineplot(x="Date", y="Long_MA", data=df, label=f'{long_window}일 이동 평균', color='red')
plt.xticks(rotation=45)
plt.title("Seaborn을 활용한 이동 평균 그래프")
plt.show()
```

## 1.5 트렌드 분석을 위한 다항 회귀선 추가
이동 평균과 함께 다항 회귀선을 추가하여 장기적인 트렌드를 분석할 수 있습니다.
```python
from numpy.polynomial.polynomial import Polynomial

# 다항 회귀선 생성
x_values = np.arange(len(df))
poly_model = Polynomial.fit(x_values, df["Value"], deg=3)
trend_values = poly_model(x_values)

# 트렌드 분석 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Value"], linestyle='-', alpha=0.3, label='원본 데이터')
plt.plot(df["Date"], trend_values, linestyle='--', color='green', label='트렌드 라인')
plt.xlabel("날짜")
plt.ylabel("값")
plt.title("트렌드 분석을 위한 다항 회귀선")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.6 이동 평균 그래프 및 트렌드 분석의 활용 예시
- 주가 및 환율 변동 분석
- 기후 데이터에서 온도 및 강수량의 변화 추이 분석
- 상품 판매량 및 수요 예측

## 1.7 객관식 문제
다음 중 이동 평균을 계산하는 데 사용되는 Pandas의 함수는 무엇인가?

A) df.mean()
B) df.rolling().mean()
C) df.median()
D) df.cumsum()

정답: B
