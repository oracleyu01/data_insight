##▣ 예제11. 다중 선 그래프 그리기

## 1. 다중 선 그래프 그리기
다중 선 그래프(Multiple Line Plot)는 여러 개의 데이터 시리즈를 하나의 그래프에서 비교할 때 유용합니다. 주로 시간에 따른 여러 지표를 비교하거나, 다양한 그룹 간의 변화를 분석하는 데 활용됩니다.

## 1.1 다중 선 그래프의 특징
- 여러 개의 데이터 시리즈를 한 그래프에 표현 가능
- 색상과 스타일을 다르게 설정하여 비교 분석 용이
- 범례(legend)를 활용하여 데이터 그룹을 명확히 구분 가능

## 1.2 기본적인 다중 선 그래프 그리기
Matplotlib을 사용하여 두 개 이상의 데이터를 한 그래프에 표시할 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 다중 선 그래프 그리기
plt.plot(x, y1, label="Sine Wave", linestyle='-', color='b')
plt.plot(x, y2, label="Cosine Wave", linestyle='--', color='r')

plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("다중 선 그래프 예제")
plt.legend()
plt.show()
```

## 1.3 선 스타일과 색상 변경
각 그래프의 선 스타일, 마커, 색상을 변경하여 가독성을 높일 수 있습니다.
```python
plt.plot(x, y1, linestyle='-', marker='o', color='g', label='Sine')
plt.plot(x, y2, linestyle='--', marker='s', color='m', label='Cosine')

plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("선 스타일 및 마커 추가된 다중 선 그래프")
plt.legend()
plt.grid(True)
plt.show()
```

## 1.4 여러 개의 데이터 시리즈 추가
세 개 이상의 선 그래프를 한 그래프에 표현할 수 있습니다.
```python
y3 = np.tan(x) / 4  # 탄젠트 함수 추가

plt.plot(x, y1, label="Sine", linestyle='-', color='b')
plt.plot(x, y2, label="Cosine", linestyle='--', color='r')
plt.plot(x, y3, label="Tangent", linestyle='-.', color='g')

plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("세 개 이상의 선 그래프")
plt.legend()
plt.ylim(-2, 2)  # Y축 제한 설정
plt.grid(True)
plt.show()
```

## 1.5 여러 개의 그래프를 하나의 그림에 표시 (서브플롯)
여러 개의 그래프를 한 Figure 내에 개별적으로 표시할 수도 있습니다.
```python
fig, axes = plt.subplots(2, 1, figsize=(8, 6))

axes[0].plot(x, y1, color='b', label='Sine')
axes[0].set_title("Sine Wave")
axes[0].legend()

axes[1].plot(x, y2, color='r', linestyle='--', label='Cosine')
axes[1].set_title("Cosine Wave")
axes[1].legend()

plt.tight_layout()
plt.show()
```

## 1.6 다중 선 그래프의 활용 예시
- 주식 시장에서 여러 종목의 가격 변화 비교
- 기온, 강수량, 습도 등의 기후 데이터 비교
- 제품별 매출 변화 분석

## 1.7 객관식 문제
다음 중 Matplotlib에서 다중 선 그래프를 그리는 데 사용되는 함수는 무엇인가?

A) plt.bar()
B) plt.hist()
C) plt.plot()
D) plt.scatter()

정답: C
