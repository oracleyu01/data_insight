##▣ 예제45. 기온과 강수량 데이터를 활용한 기후 변화 분석

## 1. 기온과 강수량 데이터를 활용한 기후 변화 분석
기온과 강수량 데이터를 분석하여 기후 변화 패턴을 파악할 수 있습니다. Pandas와 Seaborn을 활용하여 데이터 시각화를 수행할 수 있습니다.

## 1.1 기후 데이터 분석의 특징
- 장기적인 기후 변화 및 이상 기후 패턴 탐색 가능
- 온도 상승 추세 및 강수량 변화 분석
- 시계열 분석 및 예측 모델 개발 가능

## 1.2 기온 및 강수량 데이터 로드
```python
import pandas as pd
import numpy as np

# 샘플 데이터 생성
data = {
    "연도": np.arange(2000, 2023),
    "평균기온": np.random.uniform(10, 20, 23),
    "강수량": np.random.uniform(800, 1500, 23)
}
df = pd.DataFrame(data)

print(df.head())
```

## 1.3 기온 변화 시각화
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.lineplot(x=df["연도"], y=df["평균기온"], marker="o", linestyle="-", color="red")
plt.title("연도별 평균 기온 변화")
plt.xlabel("연도")
plt.ylabel("평균 기온 (°C)")
plt.grid()
plt.show()
```

## 1.4 강수량 변화 시각화
```python
plt.figure(figsize=(10, 5))
sns.barplot(x=df["연도"], y=df["강수량"], color="blue")
plt.title("연도별 강수량 변화")
plt.xlabel("연도")
plt.ylabel("강수량 (mm)")
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.5 기온과 강수량 관계 분석
```python
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["평균기온"], y=df["강수량"], color="green")
plt.title("평균 기온 vs 강수량")
plt.xlabel("평균 기온 (°C)")
plt.ylabel("강수량 (mm)")
plt.grid()
plt.show()
```

## 1.6 기온과 강수량 데이터의 활용 예시
- 기후 변화 분석 및 이상 기후 탐색
- 강우 패턴 분석 및 가뭄 예측
- 도시 기후 데이터 분석 및 정책 수립

## 1.7 객관식 문제
다음 중 기후 데이터의 시계열 변화를 분석하는 데 가장 적합한 그래프는 무엇인가?

A) 히스토그램
B) 선 그래프
C) 박스 플롯
D) 파이 차트

정답: B
