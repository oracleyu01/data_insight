## ▣ 예제3.  Matplotlib 기본 문법

## 1. Matplotlib 기본 문법
Matplotlib은 파이썬에서 가장 널리 사용되는 데이터 시각화 라이브러리로, 다양한 그래프를 손쉽게 만들 수 있습니다.

## 1.1 Matplotlib의 기본 구조
Matplotlib은 `pyplot` 모듈을 통해 그래프를 생성합니다.

### 기본적인 그래프 생성 예제
```python
import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# 그래프 그리기
plt.plot(x, y)
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("기본 선 그래프")
plt.show()
```

## 1.2 그래프 스타일 변경
Matplotlib은 다양한 스타일을 제공하며, `plt.style.use()`를 사용하여 설정할 수 있습니다.

### 스타일 적용 예제
```python
plt.style.use('ggplot')  # ggplot 스타일 적용
plt.plot(x, y, marker='o', linestyle='--', color='r', label='Line 1')
plt.legend()
plt.show()
```

## 1.3 여러 개의 그래프 그리기
Matplotlib에서는 `subplot()`을 사용하여 여러 개의 그래프를 한 번에 그릴 수 있습니다.

### 다중 서브플롯 예제
```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # 1행 2열의 서브플롯

axes[0].plot(x, y, color='b')
axes[0].set_title("첫 번째 그래프")

axes[1].bar(x, y, color='g')
axes[1].set_title("두 번째 그래프")

plt.show()
```

## 1.4 축과 범례 설정
그래프의 가독성을 높이기 위해 축 라벨, 타이틀, 범례 등을 설정할 수 있습니다.

### 축과 범례 추가 예제
```python
plt.plot(x, y, marker='s', linestyle='-', color='m', label='데이터 라인')
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.title("Matplotlib 축과 범례 설정")
plt.legend()
plt.grid(True)  # 격자 추가
plt.show()
```

## 1.5 다양한 그래프 유형
Matplotlib은 다양한 그래프 유형을 지원합니다.

### 1) 막대 그래프
```python
plt.bar(x, y, color='c')
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("막대 그래프")
plt.show()
```

### 2) 히스토그램
```python
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title("히스토그램")
plt.show()
```

### 3) 산점도
```python
plt.scatter(x, y, color='r')
plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("산점도")
plt.show()
```

## 1.6 그래프 저장하기
Matplotlib에서 `savefig()`를 사용하여 그래프를 파일로 저장할 수 있습니다.

### 그래프 저장 예제
```python
plt.plot(x, y, marker='o', linestyle='--', color='r')
plt.title("그래프 저장 예제")
plt.savefig("graph.png", dpi=300)  # 해상도 300 DPI로 저장
plt.show()
```

## 1.7 객관식 문제
다음 중 Matplotlib에서 여러 개의 그래프를 한 번에 그릴 수 있도록 도와주는 함수는?

A) plt.plot()
B) plt.bar()
C) plt.subplot()
D) plt.show()

정답: C
