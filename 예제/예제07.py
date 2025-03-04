##▣ 예제7. 막대 그래프(Bar Chart)

## 1. 막대 그래프(Bar Chart)
막대 그래프(Bar Chart)는 범주형 데이터를 비교하는 데 유용한 차트로, 각 범주의 값을 막대의 길이로 표현합니다.

## 1.1 막대 그래프의 특징
- 범주형 데이터 비교에 적합
- 데이터 값의 크기를 직관적으로 확인 가능
- 수직형과 수평형 막대 그래프 지원

## 1.2 기본적인 막대 그래프 그리기
Matplotlib을 사용하여 간단한 막대 그래프를 만들 수 있습니다.
```python
import matplotlib.pyplot as plt

# 데이터 준비
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]

# 막대 그래프 그리기
plt.bar(categories, values, color='blue')
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("기본 막대 그래프")
plt.show()
```

## 1.3 색상 및 막대 스타일 변경
```python
plt.bar(categories, values, color=['red', 'green', 'blue', 'purple', 'orange'])
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("색상이 추가된 막대 그래프")
plt.show()
```

## 1.4 수평 막대 그래프 그리기
`barh()` 함수를 사용하여 수평 막대 그래프를 만들 수 있습니다.
```python
plt.barh(categories, values, color='cyan')
plt.xlabel("값")
plt.ylabel("카테고리")
plt.title("수평 막대 그래프")
plt.show()
```

## 1.5 여러 개의 막대 그래프 그리기
```python
import numpy as np

x = np.arange(len(categories))
values2 = [12, 18, 22, 30, 27]

plt.bar(x - 0.2, values, width=0.4, label='데이터 1', color='blue')
plt.bar(x + 0.2, values2, width=0.4, label='데이터 2', color='red')
plt.xticks(ticks=x, labels=categories)
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("그룹형 막대 그래프")
plt.legend()
plt.show()
```

## 1.6 누적 막대 그래프 그리기
```python
plt.bar(categories, values, label='데이터 1', color='blue')
plt.bar(categories, values2, bottom=values, label='데이터 2', color='red')
plt.xlabel("카테고리")
plt.ylabel("값")
plt.title("누적 막대 그래프")
plt.legend()
plt.show()
```

## 1.7 막대 그래프의 활용 예시
- 매출 비교 분석
- 제품별 판매량 비교
- 연도별 성장률 분석

## 1.8 객관식 문제
다음 중 Matplotlib에서 막대 그래프를 그리는 함수는 무엇인가?

A) plt.scatter()
B) plt.plot()
C) plt.bar()
D) plt.hist()

정답: C
