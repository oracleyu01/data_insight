##▣ 예제18. 파이 차트(Pie Chart) 및 도넛 차트(Donut Chart)

## 1. 파이 차트(Pie Chart) 및 도넛 차트(Donut Chart)
파이 차트(Pie Chart)와 도넛 차트(Donut Chart)는 전체 데이터에서 각 범주가 차지하는 비율을 시각적으로 표현하는 데 사용됩니다.

## 1.1 파이 차트의 특징
- 전체 대비 각 항목의 비율을 한눈에 파악 가능
- 원형으로 표현되며, 각 조각이 전체에서 차지하는 비율을 나타냄
- 데이터의 비율을 강조할 때 유용

## 1.2 기본적인 파이 차트 그리기
Matplotlib을 사용하여 간단한 파이 차트를 만들 수 있습니다.
```python
import matplotlib.pyplot as plt

# 데이터 준비
labels = ['A', 'B', 'C', 'D']
values = [30, 20, 35, 15]

# 파이 차트 그리기
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['blue', 'red', 'green', 'purple'])
plt.title("기본 파이 차트")
plt.show()
```

## 1.3 파이 차트에서 특정 조각 강조하기
`explode` 매개변수를 사용하여 특정 조각을 강조할 수 있습니다.
```python
explode = [0, 0.1, 0, 0]  # 두 번째 조각만 강조
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['blue', 'red', 'green', 'purple'], explode=explode)
plt.title("강조된 파이 차트")
plt.show()
```

## 1.4 도넛 차트(Donut Chart) 그리기
도넛 차트는 파이 차트의 중앙을 비워서 만든 차트입니다.
```python
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['blue', 'red', 'green', 'purple'], wedgeprops={'edgecolor': 'white'})
plt.gca().add_artist(plt.Circle((0,0), 0.5, fc='white'))  # 가운데 원 추가하여 도넛 모양 생성
plt.title("도넛 차트")
plt.show()
```

## 1.5 파이 차트와 도넛 차트의 활용 예시
- 매출 기여도 분석
- 설문조사 결과(예: 고객 만족도 비율)
- 시장 점유율 비교

## 1.6 객관식 문제
다음 중 Matplotlib에서 파이 차트를 그리는 함수는 무엇인가?

A) plt.scatter()
B) plt.hist()
C) plt.pie()
D) plt.boxplot()

정답: C
