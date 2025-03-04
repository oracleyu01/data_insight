##▣ 예제29.네트워크 그래프(Network Graph)

## 1. 네트워크 그래프(Network Graph)
네트워크 그래프(Network Graph)는 노드(Node)와 엣지(Edge)로 구성된 데이터 구조를 시각화하는 방법입니다. 주로 관계형 데이터 분석, 소셜 네트워크 분석, 웹 크롤링 결과 시각화 등에 활용됩니다.

## 1.1 네트워크 그래프의 특징
- 노드(Node)와 엣지(Edge)를 통해 객체 간의 관계를 시각적으로 표현
- 복잡한 관계형 데이터의 패턴을 직관적으로 분석 가능
- 소셜 네트워크, 웹 네트워크, 통신망, 생물학적 네트워크 등 다양한 분야에서 활용

## 1.2 NetworkX를 이용한 기본 네트워크 그래프 만들기
`networkx`는 파이썬에서 네트워크 그래프를 생성하고 분석하는 데 사용되는 라이브러리입니다.

### 설치
NetworkX가 설치되지 않았다면 아래 명령어를 실행하세요.
```python
pip install networkx
```

### 기본 네트워크 그래프 생성
```python
import networkx as nx
import matplotlib.pyplot as plt

# 그래프 객체 생성
G = nx.Graph()

# 노드 추가
G.add_nodes_from(["A", "B", "C", "D", "E"])

# 엣지 추가 (노드 간 연결)
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])

# 네트워크 그래프 시각화
plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
plt.title("기본 네트워크 그래프")
plt.show()
```

## 1.3 방향성 네트워크 그래프 (Directed Graph)
방향성이 있는 그래프를 만들려면 `DiGraph()`를 사용합니다.
```python
G = nx.DiGraph()
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C")])

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightcoral', edge_color='black', node_size=2000, font_size=10, arrows=True)
plt.title("방향성 네트워크 그래프")
plt.show()
```

## 1.4 네트워크 그래프에서 노드 크기 및 색상 변경
노드 크기와 색상을 데이터 속성에 따라 다르게 설정할 수 있습니다.
```python
node_sizes = {"A": 1000, "B": 2000, "C": 1500, "D": 2500, "E": 1800}
node_colors = {"A": "red", "B": "blue", "C": "green", "D": "purple", "E": "orange"}

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color=[node_colors[node] for node in G.nodes()],
        node_size=[node_sizes[node] for node in G.nodes()], edge_color='gray', font_size=10)
plt.title("노드 크기 및 색상이 적용된 네트워크 그래프")
plt.show()
```

## 1.5 Plotly를 활용한 대화형 네트워크 그래프
Plotly를 사용하면 대화형 네트워크 그래프를 만들 수 있습니다.
```python
import plotly.graph_objects as go

# 네트워크 그래프 데이터 생성
pos = nx.spring_layout(G)
x_nodes = [pos[k][0] for k in G.nodes()]
y_nodes = [pos[k][1] for k in G.nodes()]

edges_x = []
edges_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edges_x.extend([x0, x1, None])
    edges_y.extend([y0, y1, None])

# 노드 및 엣지 추가
fig = go.Figure()
fig.add_trace(go.Scatter(x=edges_x, y=edges_y, mode='lines', line=dict(width=1, color='gray')))
fig.add_trace(go.Scatter(x=x_nodes, y=y_nodes, mode='markers+text', text=list(G.nodes()),
                         marker=dict(size=20, color='lightblue'), textposition='top center'))
fig.update_layout(title="대화형 네트워크 그래프", showlegend=False)
fig.show()
```

## 1.6 네트워크 그래프의 활용 예시
- 소셜 네트워크 분석(SNA)
- 웹 크롤링을 통한 링크 구조 분석
- 통신망 및 물류 네트워크 분석
- 유전자 및 단백질 상호작용 네트워크 분석

## 1.7 객관식 문제
다음 중 네트워크 그래프를 생성하는 데 사용되는 라이브러리는 무엇인가?

A) seaborn
B) networkx
C) folium
D) pandas

정답: B
