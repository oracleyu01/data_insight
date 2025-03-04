##▣ 예제13. 누적 막대 그래프(Stacked Bar Chart)

## 1. 누적 막대 그래프(Stacked Bar Chart)
누적 막대 그래프(Stacked Bar Chart)는 여러 개의 데이터 시리즈를 하나의 막대에 쌓아 올려 누적값을 표현하는 그래프입니다. 각 범주별 전체 합과 세부 항목의 구성 비율을 동시에 확인하는 데 유용합니다.

## 1.1 누적 막대 그래프의 특징
- 여러 그룹의 값을 하나의 막대 안에 누적하여 표현 가능
- 전체 데이터의 분포와 개별 그룹 간 비율을 동시에 분석 가능
- 범주형 데이터 비교 및 비율 분석에 적합

## 1.2 기본적인 누적 막대 그래프 그리기
Matplotlib을 사용하여 두 개 이상의 데이터를 누적하여 막대 그래프로 표현할 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
categories = ['A', 'B', 'C', 'D']
values1 = [10, 15, 20, 25]  # 그룹 1 데이터
values2 = [12, 18, 22, 28]  # 그룹 2 데이터

x = np.arange(len(categories))  # X축 위치

# 누적 막대 그래프 그리기
plt.bar(x, values1, label='그룹 1', color='blue')
plt.bar(x, values2, bottom=values1, label='그룹 2', color='red')

plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("기본 누적 막대 그래프")
plt.legend()
plt.show()
```

## 1.3 색상 및 스타일 변경
```python
plt.bar(x, values1, label='그룹 1', color='green', edgecolor='black', hatch='/')
plt.bar(x, values2, bottom=values1, label='그룹 2', color='purple', edgecolor='black', hatch='\\')

plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("스타일이 적용된 누적 막대 그래프")
plt.legend()
plt.show()
```

## 1.4 여러 개의 그룹을 포함하는 누적 막대 그래프
세 개 이상의 그룹을 포함할 수도 있습니다.
```python
values3 = [8, 14, 18, 24]  # 그룹 3 데이터

plt.bar(x, values1, label='그룹 1', color='blue')
plt.bar(x, values2, bottom=values1, label='그룹 2', color='red')
plt.bar(x, values3, bottom=np.array(values1) + np.array(values2), label='그룹 3', color='orange')

plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("세 개 이상의 그룹을 포함한 누적 막대 그래프")
plt.legend()
plt.show()
```

## 1.5 Seaborn을 활용한 누적 막대 그래프
Seaborn을 사용하면 더욱 세련된 스타일의 그래프를 쉽게 만들 수 있습니다.
```python
import seaborn as sns
import pandas as pd

# 데이터프레임 생성
data = pd.DataFrame({
    "카테고리": categories * 3,
    "값": values1 + values2 + values3,
    "그룹": ["그룹 1"] * 4 + ["그룹 2"] * 4 + ["그룹 3"] * 4
})

# Seaborn을 활용한 누적 막대 그래프
sns.barplot(x="카테고리", y="값", hue="그룹", data=data, palette="Set2")
plt.title("Seaborn 누적 막대 그래프")
plt.show()
```

## 1.6 누적 막대 그래프의 활용 예시
- 제품별 연도별 매출 비교
- 지역별 인구 통계 분석
- 설문 조사 응답 비율 비교

## 1.7 객관식 문제
다음 중 누적 막대 그래프를 그리는 Matplotlib 함수는 무엇인가?

A) plt.plot()
B) plt.scatter()
C) plt.bar()
D) plt.hist()

정답: C
