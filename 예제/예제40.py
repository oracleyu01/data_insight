##▣ 예제40.  Plotly Express로 간단한 대화형 그래프 만들기

## 1. Plotly Express로 간단한 대화형 그래프 만들기
Plotly Express는 Plotly의 고수준 API로, 간단한 코드로 대화형 그래프를 쉽게 만들 수 있습니다.

## 1.1 Plotly Express의 특징
- 간단한 코드로 다양한 대화형 그래프 생성 가능
- HTML 기반의 인터랙티브 기능(줌, 팬, 툴팁 등) 제공
- Pandas 데이터프레임과 통합되어 데이터 시각화가 편리함

## 1.2 Plotly Express 설치
Plotly Express는 `plotly` 패키지에 포함되어 있습니다. 설치되지 않았다면 다음 명령어를 실행하세요.
```python
pip install plotly
```

## 1.3 기본적인 선 그래프(Line Chart) 만들기
```python
import plotly.express as px
import pandas as pd
import numpy as np

# 샘플 데이터 생성
df = pd.DataFrame({
    "날짜": pd.date_range(start="2023-01-01", periods=100, freq='D'),
    "값": np.random.randn(100).cumsum()
})

# 대화형 선 그래프
fig = px.line(df, x="날짜", y="값", title="대화형 선 그래프")
fig.show()
```

## 1.4 막대 그래프(Bar Chart) 만들기
```python
# 샘플 데이터 생성
df = pd.DataFrame({
    "카테고리": ["A", "B", "C", "D"],
    "값": [10, 20, 15, 25]
})

# 대화형 막대 그래프
fig = px.bar(df, x="카테고리", y="값", title="대화형 막대 그래프", color="카테고리")
fig.show()
```

## 1.5 산점도(Scatter Plot) 만들기
```python
# 샘플 데이터 생성
df = pd.DataFrame({
    "X": np.random.randn(100),
    "Y": np.random.randn(100),
    "크기": np.random.rand(100) * 100,
    "그룹": np.random.choice(["A", "B", "C"], size=100)
})

# 대화형 산점도
fig = px.scatter(df, x="X", y="Y", size="크기", color="그룹", title="대화형 산점도")
fig.show()
```

## 1.6 히트맵(Heatmap) 만들기
```python
# 샘플 데이터 생성
z = np.random.rand(10, 10)

# 대화형 히트맵
fig = px.imshow(z, color_continuous_scale="Viridis", title="대화형 히트맵")
fig.show()
```

## 1.7 Plotly Express의 활용 예시
- 데이터 분석 대시보드 제작
- 실시간 데이터 시각화
- 대화형 보고서 및 프레젠테이션 제작

## 1.8 객관식 문제
다음 중 Plotly Express에서 대화형 그래프를 생성하는 함수는 무엇인가?

A) px.scatter()
B) sns.scatterplot()
C) plt.scatter()
D) folium.scatter()

정답: A
