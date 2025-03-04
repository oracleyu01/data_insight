##▣ 예제6. 선 그래프(Line Plot)

## 1. 선 그래프(Line Plot)
선 그래프(Line Plot)는 데이터의 변화를 시각적으로 표현하는 데 유용하며, 주로 시간에 따른 추세 분석에 사용됩니다.

## 1.1 선 그래프의 특징
- 연속적인 데이터 변화를 표현하는 데 적합
- X축과 Y축을 사용하여 값의 변화를 직관적으로 이해 가능
- 여러 개의 선을 한 그래프에 표시하여 비교 가능

## 1.2 기본적인 선 그래프 그리기
Matplotlib을 사용하여 간단한 선 그래프를 그릴 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 선 그래프 그리기
plt.plot(x, y)
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("기본 선 그래프")
plt.show()
```

## 1.3 여러 개의 선 그래프 그리기
여러 개의 데이터를 한 그래프에서 비교할 수 있습니다.
```python
y2 = np.cos(x)
plt.plot(x, y, label="Sine Wave", linestyle='-', color='b')
plt.plot(x, y2, label="Cosine Wave", linestyle='--', color='r')
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("다중 선 그래프")
plt.legend()
plt.show()
```

## 1.4 스타일 및 마커 추가하기
선 스타일과 마커를 추가하여 그래프를 강조할 수 있습니다.
```python
plt.plot(x, y, linestyle='-.', marker='o', color='g', label='Sine')
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("마커가 추가된 선 그래프")
plt.legend()
plt.show()
```

## 1.5 선의 두께 및 색상 변경
```python
plt.plot(x, y, linewidth=2, color='m', label='Sine Wave')
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("선 두께 변경")
plt.legend()
plt.show()
```

## 1.6 그래프 스타일 변경하기
Matplotlib은 다양한 스타일을 제공합니다.
```python
plt.style.use("ggplot")  # 스타일 변경
plt.plot(x, y, label="Sine Wave")
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("ggplot 스타일 적용")
plt.legend()
plt.show()
```

## 1.7 선 그래프의 활용 예시
선 그래프는 다양한 분야에서 활용됩니다.
- 주가 변동 분석
- 기온 변화 시각화
- 판매량 변화 분석

## 1.8 객관식 문제
다음 중 Matplotlib에서 선 그래프를 그리는 함수는 무엇인가?

A) plt.bar()
B) plt.hist()
C) plt.scatter()
D) plt.plot()

정답: D
