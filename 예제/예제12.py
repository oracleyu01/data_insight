##▣ 예제12. 그룹별 막대 그래프 (Grouped Bar Chart)

## 1. 그룹별 막대 그래프 (Grouped Bar Chart)
그룹별 막대 그래프(Grouped Bar Chart)는 여러 개의 범주형 데이터를 비교할 때 유용합니다. 주로 그룹 간의 차이를 분석할 때 활용됩니다.

## 1.1 그룹별 막대 그래프의 특징
- 두 개 이상의 범주형 데이터를 한 그래프에서 비교 가능
- 그룹별 데이터 비교를 통해 패턴 분석 가능
- 여러 개의 데이터 시리즈를 시각적으로 쉽게 표현 가능

## 1.2 기본적인 그룹별 막대 그래프 그리기
Matplotlib을 사용하여 두 개 이상의 데이터를 그룹별로 막대 그래프로 표현할 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
categories = ['A', 'B', 'C', 'D']
values1 = [10, 15, 20, 25]  # 그룹 1 데이터
values2 = [12, 18, 22, 28]  # 그룹 2 데이터

x = np.arange(len(categories))  # X축 위치
width = 0.4  # 막대 너비

# 그룹별 막대 그래프 그리기
plt.bar(x - width/2, values1, width=width, label='그룹 1', color='blue')
plt.bar(x + width/2, values2, width=width, label='그룹 2', color='red')

plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("기본 그룹별 막대 그래프")
plt.legend()
plt.show()
```

## 1.3 색상 및 스타일 변경
```python
plt.bar(x - width/2, values1, width=width, label='그룹 1', color='green', edgecolor='black', hatch='/')
plt.bar(x + width/2, values2, width=width, label='그룹 2', color='purple', edgecolor='black', hatch='\\')

plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("스타일이 적용된 그룹별 막대 그래프")
plt.legend()
plt.show()
```

## 1.4 여러 개의 그룹을 포함하는 막대 그래프
세 개 이상의 그룹을 포함할 수도 있습니다.
```python
values3 = [8, 14, 18, 24]  # 그룹 3 데이터

plt.bar(x - width, values1, width=width, label='그룹 1', color='blue')
plt.bar(x, values2, width=width, label='그룹 2', color='red')
plt.bar(x + width, values3, width=width, label='그룹 3', color='orange')

plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("세 개 이상의 그룹을 포함한 막대 그래프")
plt.legend()
plt.show()
```

## 1.5 Seaborn을 활용한 그룹별 막대 그래프
Seaborn을 사용하면 더욱 세련된 스타일의 그래프를 쉽게 만들 수 있습니다.
```python
import seaborn as sns
import pandas as pd

# 데이터프레임 생성
data = pd.DataFrame({
    "카테고리": categories * 2,
    "값": values1 + values2,
    "그룹": ["그룹 1"] * 4 + ["그룹 2"] * 4
})

# Seaborn을 활용한 그룹별 막대 그래프
sns.barplot(x="카테고리", y="값", hue="그룹", data=data, palette="Set2")
plt.title("Seaborn 그룹별 막대 그래프")
plt.show()
```

## 1.6 그룹별 막대 그래프의 활용 예시
- 제품별 연도별 매출 비교
- 지역별 고객 만족도 분석
- 연령대별 선호도 조사

## 1.7 객관식 문제
다음 중 그룹별 막대 그래프를 그리는 Matplotlib 함수는 무엇인가?

A) plt.plot()
B) plt.scatter()
C) plt.bar()
D) plt.hist()

정답: C
