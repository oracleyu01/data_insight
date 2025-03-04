##▣ 예제46. 공공데이터 API를 활용한 실시간 대시보드 제작

## 1. 공공데이터 API를 활용한 실시간 대시보드 제작
공공데이터 API를 활용하면 실시간 데이터를 가져와 대시보드에서 시각화할 수 있습니다. Python의 `requests`, `Dash`, `Plotly`를 활용하여 데이터를 수집하고 대화형 대시보드를 제작할 수 있습니다.

## 1.1 공공데이터 API를 활용한 데이터 분석의 특징
- 실시간 데이터를 자동으로 가져와 분석 가능
- 시각화를 통해 데이터 패턴을 직관적으로 이해 가능
- 대시보드를 통해 다양한 데이터 필터링 및 인터랙션 지원

## 1.2 공공데이터 API 요청 및 데이터 가져오기
먼저, `requests` 라이브러리를 사용하여 API에서 데이터를 가져옵니다.
```python
import requests
import pandas as pd

# 공공데이터 API 엔드포인트
api_url = "https://api.example.com/data"
api_key = "YOUR_API_KEY"

# API 요청
response = requests.get(f"{api_url}?apiKey={api_key}")

# JSON 데이터 변환
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data["records"])
    print(df.head())
else:
    print("API 요청 실패")
```

## 1.3 Dash를 활용한 실시간 데이터 대시보드 구축
Dash는 웹 기반 대시보드를 제작하는 라이브러리입니다.
```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Dash 앱 생성
app = dash.Dash(__name__)

# 레이아웃 구성
app.layout = html.Div([
    html.H1("공공데이터 API 실시간 대시보드"),
    dcc.Interval(id='interval-component', interval=60000, n_intervals=0),
    dcc.Graph(id='live-update-graph')
])

# 실시간 데이터 업데이트 콜백 함수
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    response = requests.get(f"{api_url}?apiKey={api_key}")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["records"])
        fig = px.line(df, x='timestamp', y='value', title="실시간 데이터 변화")
        return fig
    return px.line(title="데이터 없음")

# 앱 실행
if __name__ == '__main__':
    app.run_server(debug=True)
```

## 1.4 실행 방법
이 코드를 `app.py`로 저장한 후, 터미널에서 실행:
```sh
python app.py
```

## 1.5 공공데이터 API 활용 예시
- 실시간 대기오염 정보 시각화
- 교통 데이터 API를 활용한 도로 혼잡도 분석
- 날씨 데이터를 이용한 기후 변화 대시보드 구축
- 주식 시장 또는 환율 데이터 실시간 모니터링

## 1.6 객관식 문제
다음 중 공공데이터 API에서 실시간 데이터를 가져오는 데 사용되는 Python 라이브러리는 무엇인가?

A) seaborn
B) requests
C) pandas
D) matplotlib

정답: B
