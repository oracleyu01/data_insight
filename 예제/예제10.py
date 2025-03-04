##▣ 예제10. 박스 플롯(Box Plot)

## 1. 박스 플롯(Box Plot)
박스 플롯(Box Plot)은 데이터의 분포, 중앙값, 이상치를 시각적으로 표현하는 그래프입니다. 특히 데이터의 분포를 비교하거나 이상치를 탐지하는 데 유용합니다.

## 1.1 박스 플롯의 특징
- 최소값(min), 1사분위(Q1), 중앙값(median), 3사분위(Q3), 최대값(max) 표시
- 데이터의 분포와 퍼짐 정도를 한눈에 파악 가능
- 이상치(outlier)를 감지하는 데 효과적

## 1.2 기본적인 박스 플롯 그리기
Matplotlib을 사용하여 박스 플롯을 생성할 수 있습니다.
```python
import matplotlib.pyplot as plt
import numpy as np

# 랜덤 데이터 생성
data = np.random.randn(100) * 10 + 50  # 평균 50, 표준편차 10

# 박스 플롯 그리기
plt.boxplot(data)
plt.title("기본 박스 플롯")
plt.ylabel("값")
plt.show()
```

## 1.3 여러 그룹의 박스 플롯 그리기
여러 개의 데이터 그룹을 비교할 수 있습니다.
```python
# 여러 그룹 데이터 생성
data1 = np.random.randn(100) * 5 + 40  # 평균 40, 표준편차 5
data2 = np.random.randn(100) * 8 + 50  # 평균 50, 표준편차 8
data3 = np.random.randn(100) * 6 + 60  # 평균 60, 표준편차 6

# 박스 플롯 그리기
plt.boxplot([data1, data2, data3], labels=["Group 1", "Group 2", "Group 3"])
plt.title("여러 그룹의 박스 플롯")
plt.ylabel("값")
plt.show()
```

## 1.4 박스 플롯 스타일 설정
박스 색상과 스타일을 변경할 수 있습니다.
```python
plt.boxplot([data1, data2, data3], labels=["Group 1", "Group 2", "Group 3"],
            patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title("색상이 적용된 박스 플롯")
plt.show()
```

## 1.5 수평 박스 플롯 그리기
```python
plt.boxplot([data1, data2, data3], vert=False, labels=["Group 1", "Group 2", "Group 3"])
plt.title("수평 박스 플롯")
plt.xlabel("값")
plt.show()
```

## 1.6 Seaborn을 활용한 박스 플롯
Seaborn을 사용하면 더 세련된 박스 플롯을 쉽게 만들 수 있습니다.
```python
import seaborn as sns

df = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=df, palette="pastel")
plt.title("Seaborn을 활용한 박스 플롯")
plt.show()
```

## 1.7 박스 플롯의 활용 예시
- 시험 점수의 분포 비교
- 연봉 데이터의 이상치 탐색
- 센서 데이터의 이상 탐지

## 1.8 객관식 문제
다음 중 박스 플롯을 생성하는 Matplotlib 함수는 무엇인가?

A) plt.scatter()
B) plt.bar()
C) plt.boxplot()
D) plt.hist()

정답: C
