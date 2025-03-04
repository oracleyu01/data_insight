##▣ 예제15. 바이올린 플롯(Violin Plot)

## 1. 바이올린 플롯(Violin Plot)

바이올린 플롯(Violin Plot)은 박스 플롯(Box Plot)과 KDE(커널 밀도 추정, Kernel Density Estimation)를 결합한 그래프입니다.   

데이터의 분포와 밀도를 시각적으로 표현하는 데 유용합니다.

## 1.1 바이올린 플롯의 특징
- 데이터의 분포(밀도)를 시각적으로 표현 가능
- 박스 플롯과 KDE의 장점을 결합하여 데이터의 퍼짐 정도를 쉽게 파악 가능
- 이상치(outlier)를 감지하고 데이터의 대칭성을 분석하는 데 유용함

## 1.2 기본적인 바이올린 플롯 그리기
Seaborn을 사용하여 간단한 바이올린 플롯을 생성할 수 있습니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 예제 데이터셋 로드
df = sns.load_dataset("tips")

# 바이올린 플롯 그리기
sns.violinplot(x="day", y="total_bill", data=df)
plt.title("기본 바이올린 플롯")
plt.show()
```

## 1.3 바이올린 플롯에서 색상 추가
```python
sns.violinplot(x="day", y="total_bill", data=df, palette="Set2")
plt.title("색상이 추가된 바이올린 플롯")
plt.show()
```

## 1.4 바이올린 플롯에서 내부 데이터 표현 방법 조정
바이올린 플롯 내부에 박스 플롯 또는 개별 데이터를 표시할 수 있습니다.
```python
sns.violinplot(x="day", y="total_bill", data=df, inner="quartile")  # 사분위수 표시
plt.title("사분위수가 포함된 바이올린 플롯")
plt.show()
```
```python
sns.violinplot(x="day", y="total_bill", data=df, inner="point")  # 개별 데이터 점 표시
plt.title("데이터 포인트가 포함된 바이올린 플롯")
plt.show()
```

## 1.5 그룹별 바이올린 플롯
바이올린 플롯은 여러 그룹의 데이터 분포를 비교하는 데 유용합니다.
```python
sns.violinplot(x="day", y="total_bill", hue="sex", data=df, split=True, palette="pastel")
plt.title("성별 그룹을 포함한 바이올린 플롯")
plt.show()
```

## 1.6 바이올린 플롯과 박스 플롯 비교
박스 플롯과 바이올린 플롯을 함께 사용하면 데이터의 분포를 더 명확하게 이해할 수 있습니다.
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(x="day", y="total_bill", data=df, ax=axes[0])
axes[0].set_title("박스 플롯")

sns.violinplot(x="day", y="total_bill", data=df, ax=axes[1])
axes[1].set_title("바이올린 플롯")

plt.show()
```

## 1.7 바이올린 플롯의 활용 예시
- 실험 데이터의 분포 분석
- 여러 그룹 간의 데이터 밀도 비교
- 이상치 탐지 및 데이터의 대칭성 분석

## 1.8 객관식 문제
다음 중 Seaborn에서 바이올린 플롯을 그리는 함수는 무엇인가?

A) sns.boxplot()
B) sns.violinplot()
C) sns.histplot()
D) sns.kdeplot()

정답: B
