##▣ 예제42. Dash를 이용한 데이터 분석 대시보드 구축

## 1. Dash를 이용한 데이터 분석 대시보드 구축
Dash는 Plotly 기반의 Python 웹 프레임워크로, 대화형 데이터 분석 대시보드를 쉽게 구축할 수 있습니다.

## 1.1 Dash의 특징
- HTML, CSS, JavaScript 없이 Python 코드만으로 웹 대시보드 개발 가능
- Plotly와 통합되어 강력한 대화형 그래프 제공
- 다양한 입력 요소(슬라이더, 체크박스, 드롭다운 등)를 활용하여 동적 분석 가능

## 1.2 Dash 설치
Dash가 설치되지 않았다면 다음 명령어를 실행하세요.
```python
pip install dash
```

## 1.3 기본적인 Dash 대시보드 만들기
아래 예제는 간단한 웹 대시보드를 만드는 코드입니다.
```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 샘플 데이터 생성
df = px.data.gapminder()

# Dash 앱 생성
app = dash.Dash(__name__)

# 레이아웃 구성
app.layout = html.Div([
    html.H1("Dash 데이터 분석 대시보드"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='Canada',
        clearable=False
    ),
    dcc.Graph(id='line-chart')
])

# 콜백 함수 정의
@app.callback(
    Output('line-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_chart(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'{selected_country} GDP 변화')
    return fig

# 앱 실행
if __name__ == '__main__':
    app.run_server(debug=True)
```

### 실행 방법
이 코드를 `app.py`로 저장한 후, 터미널에서 실행:
```sh
python app.py
```

## 1.4 여러 개의 그래프 포함하기
Dash를 사용하면 한 페이지에 여러 개의 대화형 그래프를 추가할 수 있습니다.
```python
app.layout = html.Div([
    html.H1("다중 그래프 대시보드"),
    dcc.Graph(id='scatter-plot', figure=px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', title="GDP vs 기대수명")),
    dcc.Graph(id='histogram', figure=px.histogram(df, x='continent', title="대륙별 데이터 분포"))
])
```

## 1.5 입력 요소 추가하기
Dash에서는 다양한 입력 요소(슬라이더, 체크박스, 라디오 버튼 등)를 지원합니다.
```python
app.layout = html.Div([
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
    dcc.Graph(id='bar-chart')
])

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('year-slider', 'value')]
)
def update_bar_chart(selected_year):
    filtered_df = df[df['year'] == selected_year]
    fig = px.bar(filtered_df, x='continent', y='pop', color='continent', title=f'{selected_year} 인구 분포')
    return fig
```

## 1.6 Dash의 활용 예시
- 실시간 데이터 분석 대시보드 구축
- 금융 데이터 및 주식 시장 분석
- 머신러닝 모델 결과 시각화 및 해석
- IoT 센서 데이터 모니터링 시스템 구축

## 1.7 객관식 문제
다음 중 Dash에서 대화형 그래프를 추가하는 데 사용하는 라이브러리는 무엇인가?

A) seaborn
B) plotly
C) matplotlib
D) folium

정답: B
