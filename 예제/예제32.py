##▣ 예제32. Seaborn FacetGrid를 활용한 그룹별 데이터 비교

## 1. Seaborn FacetGrid를 활용한 그룹별 데이터 비교
Seaborn의 `FacetGrid`는 여러 개의 서브플롯을 생성하여 그룹별 데이터 비교를 쉽게 할 수 있도록 도와주는 기능입니다. 주로 범주형 데이터나 다중 변수를 분석할 때 유용합니다.

## 1.1 Seaborn FacetGrid의 특징
- 그룹별 데이터 비교를 위해 여러 개의 서브플롯 생성 가능
- 행(row)과 열(col) 기준으로 데이터를 분할하여 시각화
- 다양한 차트 유형(산점도, 히스토그램, KDE 등)과 결합 가능

## 1.2 Seaborn FacetGrid 설치 및 기본 사용법
Seaborn이 설치되지 않았다면 다음 명령어로 설치할 수 있습니다.
```python
pip install seaborn
```

### 기본적인 FacetGrid 생성
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터 로드
df = sns.load_dataset("penguins")

# 기본적인 FacetGrid 사용
g = sns.FacetGrid(df, col="species")
g.map_dataframe(sns.histplot, x="flipper_length_mm", bins=20)
plt.show()
```

## 1.3 FacetGrid의 행(row)과 열(col) 활용
`row`와 `col`을 함께 사용하면 다차원 데이터를 더욱 효과적으로 비교할 수 있습니다.
```python
g = sns.FacetGrid(df, row="sex", col="species")
g.map_dataframe(sns.scatterplot, x="bill_length_mm", y="bill_depth_mm")
plt.show()
```

## 1.4 색상 및 스타일 변경
FacetGrid에서는 색상과 스타일을 지정할 수도 있습니다.
```python
g = sns.FacetGrid(df, col="species", hue="sex", palette="coolwarm", height=4)
g.map_dataframe(sns.scatterplot, x="flipper_length_mm", y="body_mass_g")
g.add_legend()
plt.show()
```

## 1.5 FacetGrid에서 KDE(커널 밀도) 플롯 활용
```python
g = sns.FacetGrid(df, col="species", hue="sex", palette="Set2", height=4)
g.map_dataframe(sns.kdeplot, x="bill_length_mm", fill=True)
g.add_legend()
plt.show()
```

## 1.6 FacetGrid의 활용 예시
- 고객 데이터를 그룹별로 비교 (예: 연령대별 구매 패턴 분석)
- 생물학적 데이터에서 종별 특징 비교
- 금융 데이터에서 시장 변동성을 연도별 비교

## 1.7 객관식 문제
다음 중 Seaborn에서 그룹별 데이터를 시각적으로 비교하는 데 사용되는 함수는 무엇인가?

A) sns.boxplot()
B) sns.FacetGrid()
C) sns.barplot()
D) sns.histplot()

정답: B
