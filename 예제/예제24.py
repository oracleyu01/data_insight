##▣ 예제24. 지도 시각화(Geo Visualization) - Folium 사용법

## 1. 지도 시각화(Geo Visualization) - Folium 사용법
Folium은 파이썬에서 대화형 지도 시각화를 쉽게 구현할 수 있는 라이브러리입니다. OpenStreetMap을 기반으로 다양한 지도 기능을 제공하며, 마커, 경로, 히트맵 등을 추가하여 분석할 수 있습니다.

## 1.1 Folium의 특징
- OpenStreetMap 기반의 대화형 지도 제공
- 마커, 폴리곤, 히트맵 등 다양한 지도 요소 추가 가능
- HTML 기반의 인터랙티브 지도 생성 가능

## 1.2 Folium 설치
Folium이 설치되어 있지 않다면 아래 명령어로 설치할 수 있습니다.
```python
pip install folium
```

## 1.3 기본적인 지도 생성
Folium을 사용하여 기본적인 지도를 생성할 수 있습니다.
```python
import folium

# 기본 지도 생성
map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)  # 서울 중심 좌표

# 지도 출력
map
```

## 1.4 마커 추가하기
지도에 마커를 추가하여 특정 위치를 강조할 수 있습니다.
```python
# 지도 생성
map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
folium.Marker([37.5665, 126.9780], popup="서울", tooltip="클릭하세요").add_to(map)
folium.Marker([37.5796, 126.9770], popup="경복궁", icon=folium.Icon(color="red"), tooltip="경복궁").add_to(map)

# 지도 출력
map
```

## 1.5 원형 마커 추가
원형 마커를 사용하여 특정 지역을 강조할 수 있습니다.
```python
folium.CircleMarker(
    location=[37.5665, 126.9780],
    radius=10,
    color="blue",
    fill=True,
    fill_color="blue",
    fill_opacity=0.5,
    popup="서울 중심"
).add_to(map)

map
```

## 1.6 다각형(Polygon) 추가
다각형을 사용하여 특정 구역을 강조할 수 있습니다.
```python
folium.Polygon(
    locations=[
        [37.5665, 126.9780],
        [37.5796, 126.9770],
        [37.5700, 126.9900]
    ],
    color="green",
    fill=True,
    fill_color="green",
    fill_opacity=0.4,
    popup="특정 구역"
).add_to(map)

map
```

## 1.7 히트맵 추가하기
히트맵을 사용하여 특정 지역의 데이터 밀도를 표현할 수 있습니다.
```python
from folium.plugins import HeatMap
import numpy as np

# 임의의 위치 데이터 생성
data = np.random.uniform(low=[37.55, 126.95], high=[37.58, 127.00], size=(100, 2)).tolist()

# 히트맵 추가
HeatMap(data).add_to(map)

map
```

## 1.8 경로(Polyline) 추가
경로를 추가하여 이동 경로나 특정 지역을 연결할 수 있습니다.
```python
folium.PolyLine(
    locations=[
        [37.5665, 126.9780],
        [37.5796, 126.9770],
        [37.5700, 126.9900]
    ],
    color="blue",
    weight=5,
    opacity=0.7
).add_to(map)

map
```

## 1.9 지도 시각화의 활용 예시
- 공공 데이터(범죄율, 대기오염 등) 시각화
- 실시간 위치 기반 서비스 개발
- 매장 또는 관광지 위치 분석

## 1.10 객관식 문제
다음 중 Folium에서 히트맵을 생성하는 데 사용되는 함수는 무엇인가?

A) folium.Marker()
B) folium.PolyLine()
C) HeatMap()
D) folium.Circle()

정답: C
