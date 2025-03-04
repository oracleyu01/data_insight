##▣ 예제43. Voila + Jupyter를 활용한 대화형 데이터 분석

## 1. Voila + Jupyter를 활용한 대화형 데이터 분석
Voila는 Jupyter Notebook을 대화형 웹 애플리케이션으로 변환할 수 있는 도구로, 데이터 분석을 시각적으로 공유하는 데 유용합니다.

## 1.1 Voila의 특징
- Jupyter Notebook을 코드 수정 없이 대화형 웹 앱으로 변환 가능
- Dash, Streamlit과 유사한 기능 제공하지만 Jupyter 기반으로 작동
- HTML, CSS, JavaScript 없이 데이터 분석 대시보드 구축 가능

## 1.2 Voila 설치
Voila가 설치되지 않았다면 다음 명령어를 실행하세요.
```python
pip install voila
```

## 1.3 Jupyter Notebook에서 Voila 실행 방법
1. Jupyter Notebook에서 데이터 분석 코드 작성
2. 다음 명령어로 Notebook을 대화형 웹 애플리케이션으로 실행
```sh
voila notebook.ipynb
```

## 1.4 간단한 Voila 대시보드 예제
```python
import ipywidgets as widgets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성
df = pd.DataFrame({
    "X": np.arange(1, 101),
    "Y": np.random.randn(100).cumsum()
})

# 슬라이더 위젯
num_points = widgets.IntSlider(value=50, min=10, max=100, step=10, description="데이터 포인트 수")

# 대화형 그래프 함수
def update_chart(n):
    plt.figure(figsize=(8, 5))
    plt.plot(df["X"][:n], df["Y"][:n], marker="o", linestyle="-")
    plt.title(f"{n}개의 데이터 포인트를 포함한 그래프")
    plt.xlabel("X 값")
    plt.ylabel("Y 값")
    plt.grid()
    plt.show()

widgets.interactive(update_chart, n=num_points)
```

## 1.5 Pandas 데이터 테이블과 Voila 활용
Jupyter의 `display()` 함수를 사용하면 데이터 테이블을 인터랙티브하게 표시할 수 있습니다.
```python
from IPython.display import display

# 데이터 테이블 출력
display(df.head())
```

## 1.6 Voila와 Plotly를 활용한 대화형 그래프
```python
import plotly.express as px

fig = px.line(df, x="X", y="Y", title="Plotly를 활용한 대화형 그래프")
fig.show()
```

## 1.7 Voila의 활용 예시
- 대화형 데이터 분석 보고서 공유
- 머신러닝 모델 결과 시각화
- 웹 기반 데이터 대시보드 구축

## 1.8 객관식 문제
다음 중 Voila를 사용하여 Jupyter Notebook을 대화형 웹 애플리케이션으로 실행하는 명령어는 무엇인가?

A) streamlit run notebook.ipynb
B) voila notebook.ipynb
C) python notebook.ipynb
D) flask run notebook.ipynb

정답: B
