##▣ 예제25. Choropleth 지도 만들기

## 1. Choropleth 지도 만들기
Choropleth 지도는 지역별 데이터를 색상으로 구분하여 시각적으로 표현하는 지도입니다. 주로 인구 통계, 경제 데이터, 선거 결과 등의 분석에 활용됩니다.

## 1.1 Choropleth 지도의 특징
- 지리적 데이터를 색상으로 시각화하여 지역별 차이를 강조
- 행정구역(국가, 주, 도시 등) 단위로 데이터를 비교 가능
- 인구, 경제, 환경 데이터 등의 분석에 유용

## 1.2 Folium을 이용한 Choropleth 지도 생성
Folium 라이브러리를 사용하여 Choropleth 지도를 쉽게 만들 수 있습니다.
```python
import folium
import pandas as pd
import json
from folium.plugins import Choropleth

# 기본 지도 생성
map = folium.Map(location=[37.5665, 126.9780], zoom_start=7)

# 샘플 데이터 준비
data = {
    "서울특별시": 500,
    "부산광역시": 300,
    "대구광역시": 200,
    "인천광역시": 400,
    "광주광역시": 250,
    "대전광역시": 150
}

# 데이터프레임 변환
df = pd.DataFrame(list(data.items()), columns=["Region", "Value"])

# GeoJSON 파일 로드 (행정구역 경계 데이터)
geo_json_path = "korea_geo.json"  # 예제 GeoJSON 파일 경로
with open(geo_json_path, encoding='utf-8') as f:
    geo_data = json.load(f)

# Choropleth 지도 추가
Choropleth(
    geo_data=geo_data,
    data=df,
    columns=["Region", "Value"],
    key_on="feature.properties.name",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="데이터 값"
).add_to(map)

# 지도 출력
map
```

## 1.3 색상 조정 및 스타일 변경
색상 테마를 조정하여 가독성을 높일 수 있습니다.
```python
Choropleth(
    geo_data=geo_data,
    data=df,
    columns=["Region", "Value"],
    key_on="feature.properties.name",
    fill_color="BuPu",  # 색상 테마 변경
    fill_opacity=0.8,
    line_opacity=0.3,
    legend_name="지역별 데이터"
).add_to(map)
map
```

## 1.4 팝업 정보 추가
각 지역을 클릭하면 세부 정보를 표시할 수 있습니다.
```python
for _, row in df.iterrows():
    folium.Marker(
        location=[37.5665, 126.9780],
        popup=f"{row['Region']}: {row['Value']}"
    ).add_to(map)
map
```

## 1.5 Choropleth 지도의 활용 예시
- 인구밀도, 실업률, 소득 수준 등의 데이터 분석
- 선거 결과 지도
- 환경오염, 에너지 소비량 등의 시각화

## 1.6 객관식 문제
다음 중 Folium에서 지역별 데이터를 색상으로 표현하는 지도는 무엇인가?

A) folium.Marker()
B) folium.Choropleth()
C) folium.PolyLine()
D) folium.CircleMarker()

정답: B
