##▣ 예제31.  Pandas + Matplotlib을 활용한 데이터 분석

## 1. Pandas + Matplotlib을 활용한 데이터 분석
Pandas와 Matplotlib은 데이터 분석과 시각화를 위해 자주 사용되는 라이브러리입니다. Pandas를 사용하여 데이터를 다루고, Matplotlib을 활용하여 시각적으로 표현할 수 있습니다.

## 1.1 Pandas + Matplotlib의 특징
- Pandas를 사용하여 데이터 로드, 처리, 변환 가능
- Matplotlib을 활용하여 데이터 분포, 추세, 패턴을 시각적으로 분석 가능
- 데이터프레임을 바로 그래프로 표현할 수 있어 편리함

## 1.2 기본적인 데이터프레임 생성 및 시각화
```python
import pandas as pd
import matplotlib.pyplot as plt

# 샘플 데이터 생성
data = {
    "연도": [2018, 2019, 2020, 2021, 2022],
    "매출": [500, 600, 750, 800, 950]
}
df = pd.DataFrame(data)

# 라인 차트 그리기
plt.plot(df["연도"], df["매출"], marker="o", linestyle="-", color="b", label="매출")
plt.xlabel("연도")
plt.ylabel("매출")
plt.title("연도별 매출 변화")
plt.legend()
plt.grid()
plt.show()
```

## 1.3 바 차트(Bar Chart) 활용
```python
plt.bar(df["연도"], df["매출"], color="green", alpha=0.7)
plt.xlabel("연도")
plt.ylabel("매출")
plt.title("연도별 매출 바 차트")
plt.show()
```

## 1.4 히스토그램(Histogram) 활용
```python
import numpy as np

# 랜덤 데이터 생성
sales_data = np.random.normal(750, 150, 1000)

# 히스토그램 그리기
plt.hist(sales_data, bins=20, color="purple", alpha=0.6, edgecolor="black")
plt.xlabel("매출")
plt.ylabel("빈도수")
plt.title("매출 분포 히스토그램")
plt.show()
```

## 1.5 박스 플롯(Box Plot) 활용
```python
plt.boxplot(sales_data)
plt.xlabel("매출")
plt.title("매출 분포 박스 플롯")
plt.show()
```

## 1.6 산점도(Scatter Plot) 활용
```python
# 랜덤 데이터 생성
df["광고비"] = [50, 60, 70, 90, 120]
plt.scatter(df["광고비"], df["매출"], color="red", alpha=0.7)
plt.xlabel("광고비")
plt.ylabel("매출")
plt.title("광고비 vs 매출 산점도")
plt.grid()
plt.show()
```

## 1.7 Pandas 내장 플롯 기능 활용
Pandas 데이터프레임은 자체적으로 Matplotlib 기반의 그래프를 생성할 수 있습니다.
```python
df.plot(x="연도", y="매출", kind="line", marker="o", title="Pandas 내장 그래프")
plt.show()
```

## 1.8 Pandas + Matplotlib의 활용 예시
- 판매 데이터 분석 및 시각화
- 고객 행동 분석을 위한 데이터 시각화
- 시계열 데이터 분석 및 추세 예측

## 1.9 객관식 문제
다음 중 Pandas 데이터프레임을 직접 시각화할 수 있는 함수는 무엇인가?

A) df.plot()
B) df.scatter()
C) df.show()
D) df.graph()

정답: A
