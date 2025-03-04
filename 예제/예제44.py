##▣ 예제44. 웹 스크래핑 데이터를 시각화

## 1. 웹 스크래핑 데이터를 시각화
웹 스크래핑(Web Scraping)은 웹사이트에서 데이터를 추출하는 기술로, 이를 시각화하면 데이터의 의미를 효과적으로 파악할 수 있습니다.

## 1.1 웹 스크래핑의 특징
- 웹에서 데이터를 자동으로 수집 가능
- 텍스트, 테이블, 이미지 등의 다양한 데이터 추출 가능
- 추출한 데이터를 정리하여 시각적으로 표현 가능

## 1.2 웹 스크래핑을 위한 라이브러리 설치
BeautifulSoup와 Requests를 활용하여 데이터를 가져올 수 있습니다.
```python
pip install beautifulsoup4 requests pandas matplotlib seaborn
```

## 1.3 웹 스크래핑을 이용한 데이터 수집 예제
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹 페이지 요청
url = "https://example.com/data-page"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 데이터 추출 (예: 테이블 데이터)
data_list = []
table = soup.find("table")
for row in table.find_all("tr")[1:]:  # 첫 번째 행(헤더) 제외
    cols = row.find_all("td")
    data_list.append([col.text.strip() for col in cols])

# 데이터프레임 변환
df = pd.DataFrame(data_list, columns=["날짜", "값"])
print(df.head())
```

## 1.4 웹 스크래핑 데이터를 시각화하기
```python
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 변환
df["값"] = df["값"].astype(float)
df["날짜"] = pd.to_datetime(df["날짜"])

# 시각화
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["날짜"], y=df["값"], marker="o", linestyle="-")
plt.title("웹 스크래핑 데이터 시각화")
plt.xlabel("날짜")
plt.ylabel("값")
plt.xticks(rotation=45)
plt.grid()
plt.show()
```

## 1.5 웹 스크래핑 데이터의 활용 예시
- 주식 시장 데이터 크롤링 및 시각화
- 날씨 데이터 수집 및 분석
- 뉴스 트렌드 분석

## 1.6 객관식 문제
다음 중 웹 스크래핑을 통해 데이터를 가져오는 데 사용할 수 있는 라이브러리는 무엇인가?

A) matplotlib
B) seaborn
C) beautifulsoup4
D) scikit-learn

정답: C
