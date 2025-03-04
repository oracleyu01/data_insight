##▣ 예제19.  워드클라우드(Word Cloud)

## 1. 워드클라우드(Word Cloud)
워드클라우드(Word Cloud)는 텍스트 데이터에서 단어의 빈도를 기반으로 시각화하는 기법입니다. 단어의 크기는 빈도수에 비례하며, 텍스트 데이터를 분석할 때 유용하게 사용됩니다.

## 1.1 워드클라우드의 특징
- 단어 빈도수를 직관적으로 표현 가능
- 단어의 크기가 빈도수를 반영하여 자동 조절됨
- 텍스트 데이터의 주요 키워드를 파악하는 데 유용함

## 1.2 워드클라우드 설치 및 기본 사용법
`wordcloud` 라이브러리가 필요하며, 없을 경우 아래 명령어로 설치할 수 있습니다.
```python
pip install wordcloud
```

## 1.3 기본적인 워드클라우드 생성
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 샘플 텍스트 데이터
text = "데이터 시각화는 매우 중요합니다. 데이터 분석과 데이터 시각화는 함께 사용됩니다."

# 워드클라우드 생성
wordcloud = WordCloud(font_path=None, background_color='white', width=800, height=400).generate(text)

# 시각화
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("기본 워드클라우드")
plt.show()
```

## 1.4 사용자 지정 폰트 적용하기
한글을 포함한 워드클라우드를 만들 경우, 한글 폰트를 지정해야 합니다.
```python
wordcloud = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("한글 폰트 적용 워드클라우드")
plt.show()
```

## 1.5 텍스트 파일을 이용한 워드클라우드 생성
```python
with open("sample.txt", encoding="utf-8") as f:
    text = f.read()

wordcloud = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("텍스트 파일 기반 워드클라우드")
plt.show()
```

## 1.6 마스킹 이미지 적용하기
이미지를 활용한 워드클라우드(예: 특정 모양의 워드클라우드)를 만들 수 있습니다.
```python
import numpy as np
from PIL import Image

# 마스킹 이미지 로드
mask = np.array(Image.open("cloud_shape.png"))
wordcloud = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color='white', mask=mask).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("마스킹 이미지 적용 워드클라우드")
plt.show()
```

## 1.7 워드클라우드의 활용 예시
- 뉴스 기사에서 핵심 키워드 추출
- 고객 리뷰 또는 피드백 분석
- 소셜 미디어 데이터 분석

## 1.8 객관식 문제
다음 중 워드클라우드를 생성하는 파이썬 라이브러리는 무엇인가?

A) seaborn
B) wordcloud
C) plotly
D) pandas

정답: B
