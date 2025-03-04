##▣ 예제36. 지도 위에 GPS 데이터 시각화

## 1. 지도 위에 GPS 데이터 시각화
GPS 데이터를 지도에 시각화하면 위치 기반 데이터를 분석하고 이동 경로를 시각적으로 파악하는 데 유용합니다. 주로 `folium` 라이브러리를 활용하여 구현할 수 있습니다.

## 1.1 GPS 데이터 시각화의 특징
- 위도(latitude)와 경도(longitude) 좌표를 기반으로 지도에 데이터 표시
- 차량 이동 경로, 사용자 위치 데이터 분석에 활용 가능
- 마커, 라인(경로), 히트맵 등 다양한 방법으로 시각화 가능

## 1.2 Folium을 활용한 기본 GPS 마커 시각화
`folium` 라이브러리를 사용하여 GPS 데이터를 지도에 표시할 수 있습니다.

### Folium 설치
Folium이 설치되지 않았다면 다음 명령어를 실행하세요.
```python
pip install folium
```

### 기본적인 GPS 마커 시각화
```python
import folium

# 지도 생성
map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# GPS 좌표 데이터
gps_data = [
    [37.5665, 126.9780, "서울"],
    [37.5796, 126.9770, "경복궁"],
    [37.5700, 126.9900, "종로"],
    [37.5610, 126.9950, "명동"]
]

# 마커 추가
for lat, lon, location in gps_data:
    folium.Marker([lat, lon], popup=location).add_to(map)

# 지도 출력
map
```

## 1.3 GPS 경로 데이터 시각화 (Polyline 활용)
GPS 데이터가 경로를 포함하는 경우 `folium.PolyLine()`을 사용하여 이동 경로를 시각화할 수 있습니다.
```python
# 이동 경로 데이터
gps_path = [
    [37.5665, 126.9780],
    [37.5796, 126.9770],
    [37.5700, 126.9900],
    [37.5610, 126.9950]
]

# PolyLine 추가
folium.PolyLine(gps_path, color="blue", weight=3, opacity=0.7).add_to(map)

# 지도 출력
map
```

## 1.4 GPS 히트맵 시각화
GPS 데이터의 밀도를 히트맵으로 표현하려면 `HeatMap`을 사용할 수 있습니다.
```python
from folium.plugins import HeatMap
import numpy as np

# 임의의 GPS 데이터 생성
gps_heatmap_data = np.random.uniform(low=[37.55, 126.95], high=[37.58, 127.00], size=(100, 2)).tolist()

# 히트맵 추가
HeatMap(gps_heatmap_data).add_to(map)

# 지도 출력
map
```

## 1.5 GPS 데이터 시각화의 활용 예시
- 차량 또는 배달 경로 분석
- 실시간 위치 데이터 시각화
- 관광객 방문 패턴 분석
- 대중교통 이동 경로 최적화

## 1.6 객관식 문제
다음 중 Folium에서 GPS 이동 경로를 시각화하는 데 사용하는 함수는 무엇인가?

A) folium.Marker()
B) folium.PolyLine()
C) folium.HeatMap()
D) folium.GeoJson()

정답: B
