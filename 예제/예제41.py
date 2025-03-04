##▣ 예제41. Streamlit을 활용한 데이터 시각화 웹 앱 만들기

## 1. Streamlit을 활용한 데이터 시각화 웹 앱 만들기
Streamlit은 Python 기반의 데이터 시각화 및 대화형 웹 애플리케이션을 손쉽게 만들 수 있는 라이브러리입니다.

## 1.1 Streamlit의 특징
- Python 코드만으로 대화형 웹 애플리케이션 개발 가능
- 간단한 문법으로 데이터 분석 및 시각화 구현 가능
- Matplotlib, Seaborn, Plotly 등의 라이브러리와 쉽게 연동 가능

## 1.2 Streamlit 설치
Streamlit이 설치되지 않았다면 다음 명령어를 실행하세요.
```python
pip install streamlit
```

## 1.3 기본적인 Streamlit 앱 만들기
Streamlit 앱은 `.py` 파일로 저장하고, 터미널에서 실행해야 합니다.
```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 제목 및 설명
st.title("Streamlit을 활용한 데이터 시각화")
st.write("이 웹 앱은 Streamlit을 사용하여 데이터를 시각화하는 예제입니다.")

# 샘플 데이터 생성
data = pd.DataFrame({
    "X": np.arange(1, 101),
    "Y": np.random.randn(100).cumsum()
})

# 라인 차트
st.line_chart(data.set_index("X"))
```
### 실행 방법
이 코드를 `app.py`로 저장한 후, 터미널에서 다음 명령어 실행:
```sh
streamlit run app.py
```

## 1.4 Streamlit과 Matplotlib 연동하기
```python
fig, ax = plt.subplots()
ax.plot(data["X"], data["Y"], marker="o", linestyle="-", color="blue")
ax.set_title("Matplotlib 그래프")
st.pyplot(fig)
```

## 1.5 Streamlit과 Plotly 연동하기
```python
import plotly.express as px

fig = px.line(data, x="X", y="Y", title="Plotly 대화형 그래프")
st.plotly_chart(fig)
```

## 1.6 사용자 입력을 활용한 대화형 앱 만들기
```python
# 슬라이더 추가
num_points = st.slider("데이터 포인트 수 선택", min_value=10, max_value=200, value=50)

# 선택된 수만큼 데이터 생성
new_data = pd.DataFrame({
    "X": np.arange(1, num_points + 1),
    "Y": np.random.randn(num_points).cumsum()
})

# 새로운 차트 표시
st.line_chart(new_data.set_index("X"))
```

## 1.7 Streamlit의 활용 예시
- 데이터 분석 대시보드 개발
- 머신러닝 모델 배포 및 결과 시각화
- 실시간 데이터 모니터링 시스템 구축

## 1.8 객관식 문제
다음 중 Streamlit에서 웹 애플리케이션을 실행하는 명령어는 무엇인가?

A) python app.py
B) flask run app.py
C) streamlit run app.py
D) dash run app.py

정답: C
