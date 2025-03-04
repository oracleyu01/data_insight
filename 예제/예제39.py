##▣ 예제39.Bokeh를 활용한 대화형 시각화

## 1. Bokeh를 활용한 대화형 시각화
Bokeh는 대화형(Interactive) 데이터 시각화를 위한 강력한 파이썬 라이브러리로, 웹 기반의 시각화 기능을 제공합니다.

## 1.1 Bokeh의 특징
- HTML 기반의 대화형 시각화 지원
- 줌(Zoom), 팬(Pan), 툴팁(Tooltip) 등의 인터랙티브 기능 제공
- Matplotlib보다 웹 친화적인 시각화 가능
- 대량의 데이터를 효과적으로 렌더링 가능

## 1.2 Bokeh 설치 및 기본 사용법
Bokeh가 설치되지 않았다면 다음 명령어를 실행하세요.
```python
pip install bokeh
```

### 기본적인 Bokeh 그래프 생성
```python
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()  # Jupyter Notebook에서 실행 가능하게 설정

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 그래프 생성
p = figure(title="기본 Bokeh 그래프", x_axis_label="X 값", y_axis_label="Y 값", tools="pan,box_zoom,reset,save")
p.line(x, y, legend_label="라인 그래프", line_width=2)

# 그래프 출력
show(p)
```

## 1.3 Bokeh에서 점(Scatter) 플롯 생성
```python
from bokeh.plotting import figure, show

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 산점도 그래프 생성
p = figure(title="Bokeh 산점도", x_axis_label="X 값", y_axis_label="Y 값", tools="pan,box_zoom,reset,save")
p.scatter(x, y, size=10, color="navy", alpha=0.5)

# 그래프 출력
show(p)
```

## 1.4 Bokeh에서 막대 그래프(Bar Chart) 생성
```python
from bokeh.io import output_file
from bokeh.plotting import figure, show

# 데이터 준비
categories = ["A", "B", "C", "D", "E"]
values = [10, 20, 15, 25, 30]

# 막대 그래프 생성
p = figure(x_range=categories, title="Bokeh 막대 그래프", x_axis_label="카테고리", y_axis_label="값", tools="pan,box_zoom,reset,save")
p.vbar(x=categories, top=values, width=0.5, color="blue")

# 그래프 출력
show(p)
```

## 1.5 Bokeh에서 툴팁(Tooltip) 추가하기
툴팁을 추가하여 마우스를 올릴 때 데이터를 표시할 수 있습니다.
```python
from bokeh.models import HoverTool

# 그래프 생성
p = figure(title="Bokeh 툴팁 추가", x_axis_label="X 값", y_axis_label="Y 값", tools="pan,box_zoom,reset,save")
p.scatter(x, y, size=10, color="green", alpha=0.6)

# 툴팁 추가
tooltips = HoverTool(tooltips=[("X 값", "@x"), ("Y 값", "@y")])
p.add_tools(tooltips)

# 그래프 출력
show(p)
```

## 1.6 Bokeh의 활용 예시
- 실시간 데이터 모니터링 대시보드
- 웹 기반 데이터 시각화
- 금융 시장 데이터 분석
- IoT 센서 데이터 시각화

## 1.7 객관식 문제
다음 중 Bokeh에서 대화형 그래프를 생성하는 데 사용되는 함수는 무엇인가?

A) plt.scatter()
B) px.line()
C) figure()
D) sns.histplot()

정답: C
