##▣ 예제30. Sankey Diagram을 활용한 흐름 데이터 시각화


## 1. Sankey Diagram을 활용한 흐름 데이터 시각화
Sankey Diagram(생키 다이어그램)은 흐름 데이터를 시각적으로 표현하는 데 사용됩니다. 주로 에너지 흐름, 재정 흐름, 사용자 이동 경로 등을 분석하는 데 활용됩니다.

## 1.1 Sankey Diagram의 특징
- 노드(Node)와 링크(Edge)로 구성되어 데이터 흐름을 시각적으로 표현
- 흐름의 방향성과 양을 직관적으로 파악 가능
- 복잡한 시스템의 데이터 이동을 쉽게 분석 가능

## 1.2 Plotly를 이용한 기본 Sankey Diagram 만들기
Plotly의 `go.Sankey()`를 사용하여 Sankey Diagram을 생성할 수 있습니다.
```python
import plotly.graph_objects as go

# 노드 정의
nodes = ["A", "B", "C", "D", "E"]

# 링크 정의
sources = [0, 0, 1, 1, 2, 3]  # 출발 노드 인덱스
targets = [1, 2, 3, 4, 4, 4]  # 도착 노드 인덱스
values = [10, 15, 20, 5, 10, 5]  # 흐름 값

# Sankey Diagram 생성
fig = go.Figure(go.Sankey(
    node=dict(
        label=nodes,
        pad=15,
        thickness=20
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
))

fig.update_layout(title_text="기본 Sankey Diagram", font_size=12)
fig.show()
```

## 1.3 색상 및 스타일 추가
Sankey Diagram에 색상을 추가하여 가독성을 높일 수 있습니다.
```python
fig = go.Figure(go.Sankey(
    node=dict(
        label=nodes,
        pad=15,
        thickness=20,
        color=['blue', 'green', 'red', 'purple', 'orange']
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=['rgba(31, 119, 180, 0.5)', 'rgba(255, 127, 14, 0.5)',
               'rgba(44, 160, 44, 0.5)', 'rgba(214, 39, 40, 0.5)',
               'rgba(148, 103, 189, 0.5)', 'rgba(140, 86, 75, 0.5)']
    )
))

fig.update_layout(title_text="색상이 적용된 Sankey Diagram", font_size=12)
fig.show()
```

## 1.4 Sankey Diagram의 활용 예시
- 에너지 소비 흐름 분석
- 웹사이트 사용자 이동 경로 분석
- 예산 및 재정 흐름 시각화
- 제품 생산 및 물류 흐름 분석

## 1.5 객관식 문제
다음 중 Sankey Diagram을 생성하는 Plotly 함수는 무엇인가?

A) go.Bar()
B) go.Scatter()
C) go.Sankey()
D) go.Heatmap()

정답: C
