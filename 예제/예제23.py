##▣ 예제23. 주식 데이터 시각화 (OHLC 및 캔들차트)

## 1. 주식 데이터 시각화 (OHLC 및 캔들차트)
주식 데이터 시각화는 주가의 변동을 효과적으로 분석하는 데 중요한 역할을 합니다. 대표적인 방법으로 OHLC(Open, High, Low, Close) 차트와 캔들차트(Candlestick Chart)가 있습니다.

## 1.1 OHLC 차트와 캔들차트의 특징
- **OHLC 차트(Open-High-Low-Close Chart)**: 각 거래일의 시가(Open), 고가(High), 저가(Low), 종가(Close)를 막대 형태로 표현
- **캔들차트(Candlestick Chart)**: OHLC 차트를 시각적으로 개선하여 상승/하락을 색상으로 구분
- 주가의 패턴과 트렌드를 분석하는 데 유용

## 1.2 주식 데이터 가져오기
`yfinance` 라이브러리를 사용하여 실시간 또는 과거 주식 데이터를 가져올 수 있습니다.
```python
pip install yfinance mplfinance
```
```python
import yfinance as yf
import pandas as pd

# 삼성전자(005930.KQ) 데이터 가져오기
ticker = "005930.KQ"
data = yf.download(ticker, start="2023-01-01", end="2023-12-31")
print(data.head())
```

## 1.3 OHLC 차트 그리기
Matplotlib을 사용하여 OHLC 차트를 생성할 수 있습니다.
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(data.index, data['Open'], label='Open', linestyle='--')
plt.plot(data.index, data['High'], label='High', linestyle='dotted')
plt.plot(data.index, data['Low'], label='Low', linestyle='dashed')
plt.plot(data.index, data['Close'], label='Close', color='black')

plt.xlabel("날짜")
plt.ylabel("가격")
plt.title("OHLC 차트")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.4 캔들차트 그리기 (mplfinance 활용)
`mplfinance` 라이브러리를 사용하면 캔들차트를 손쉽게 만들 수 있습니다.
```python
import mplfinance as mpf

mpf.plot(data, type='candle', style='charles', volume=True, figsize=(12,6))
plt.title("캔들차트")
plt.show()
```

## 1.5 이동 평균 추가한 캔들차트
```python
mpf.plot(data, type='candle', style='charles', volume=True, figsize=(12,6),
         mav=(5, 20), title="이동 평균이 포함된 캔들차트")
plt.show()
```

## 1.6 주식 데이터 시각화의 활용 예시
- 주식 시장 분석 및 트레이딩 전략 개발
- 특정 패턴(골든크로스, 데드크로스 등) 탐지
- 특정 종목의 가격 변동성 및 추세 분석

## 1.7 객관식 문제
다음 중 캔들차트를 생성하는 데 사용되는 Python 라이브러리는 무엇인가?

A) mplfinance
B) seaborn
C) pandas
D) numpy

정답: A
