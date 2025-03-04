##▣ 예제33.  다변량 데이터 시각화 (Pair Plot, Joint Plot)

## 1. 다변량 데이터 시각화 (Pair Plot, Joint Plot)
다변량 데이터(여러 개의 변수로 이루어진 데이터)를 시각적으로 탐색할 때 `Pair Plot`과 `Joint Plot`이 유용합니다. Seaborn 라이브러리를 활용하여 다변량 데이터를 효과적으로 분석할 수 있습니다.

## 1.1 다변량 데이터 시각화의 특징
- 변수 간의 관계를 직관적으로 탐색 가능
- 데이터의 분포 및 상관관계를 분석하는 데 유용
- 회귀선, 히스토그램, 산점도를 결합하여 패턴을 쉽게 확인 가능

## 1.2 Pair Plot을 활용한 다변량 데이터 비교
Pair Plot(페어 플롯)은 여러 변수 간의 관계를 행렬 형태로 표현하는 그래프입니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터 로드
df = sns.load_dataset("penguins")

# Pair Plot 생성
sns.pairplot(df, hue="species", palette="husl")
plt.show()
```

### Pair Plot의 주요 기능
- `hue` 옵션을 사용하면 그룹별로 색상을 다르게 지정 가능
- `diag_kind="kde"` 옵션을 추가하면 대각선에 KDE(커널 밀도) 그래프를 표시 가능
```python
sns.pairplot(df, hue="species", diag_kind="kde", palette="coolwarm")
plt.show()
```

## 1.3 Joint Plot을 활용한 변수 간 관계 분석
Joint Plot(조인트 플롯)은 두 변수 간의 관계를 산점도와 히스토그램으로 결합한 시각화 기법입니다.
```python
# 기본 Joint Plot 생성
sns.jointplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.show()
```

### Joint Plot의 주요 기능
- `kind="kde"` 옵션을 사용하여 밀도 기반의 관계 표현 가능
```python
sns.jointplot(data=df, x="bill_length_mm", y="bill_depth_mm", kind="kde", hue="species")
plt.show()
```

- `kind="reg"` 옵션을 사용하면 회귀선을 추가하여 변수 간의 관계를 분석 가능
```python
sns.jointplot(data=df, x="bill_length_mm", y="bill_depth_mm", kind="reg", hue="species")
plt.show()
```

## 1.4 다변량 데이터 시각화의 활용 예시
- 금융 데이터에서 여러 변수 간 상관관계 분석
- 생물학적 데이터에서 종별 특징 비교
- 마케팅 데이터에서 고객 행동 패턴 분석

## 1.5 객관식 문제
다음 중 Seaborn에서 다변량 데이터를 시각화하는 데 사용되는 함수는 무엇인가?

A) sns.histplot()
B) sns.boxplot()
C) sns.pairplot()
D) sns.barplot()

정답: C
