##▣ 예제5. Seaborn 기본 사용법

## 1. Seaborn 기본 사용법
Seaborn은 Matplotlib을 기반으로 한 데이터 시각화 라이브러리로, 더 세련된 그래프를 간편하게 생성할 수 있습니다.

## 1.1 Seaborn의 주요 특징
- 간단한 코드로 고급 시각화 가능
- Pandas의 데이터프레임과 호환성이 뛰어남
- 다양한 통계적 데이터 시각화 제공 (히트맵, KDE 그래프 등)
- 자동으로 스타일이 적용된 그래프 제공

## 1.2 Seaborn 설치
Seaborn이 설치되어 있지 않다면 아래 명령어로 설치할 수 있습니다.
```python
pip install seaborn
```

## 1.3 Seaborn 라이브러리 불러오기
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 예제 데이터셋 로드
df = sns.load_dataset("tips")
print(df.head())
```

## 1.4 기본적인 그래프 그리기
Seaborn을 사용하면 다양한 유형의 그래프를 쉽게 생성할 수 있습니다.

### 1) 산점도 (Scatter Plot)
```python
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("산점도 예제")
plt.show()
```

### 2) 막대 그래프 (Bar Chart)
```python
sns.barplot(x="day", y="total_bill", data=df)
plt.title("요일별 총 지출")
plt.show()
```

### 3) 박스 플롯 (Box Plot)
```python
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("요일별 총 지출 분포")
plt.show()
```

### 4) 히스토그램 (Histogram, KDE Plot 포함)
```python
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("총 지출 히스토그램")
plt.show()
```

## 1.5 Seaborn 스타일 설정
Seaborn은 다양한 스타일을 제공하며 `sns.set_style()`을 사용하여 변경할 수 있습니다.
```python
sns.set_style("darkgrid")  # 스타일 변경 가능: whitegrid, dark, white, ticks
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("스타일 적용 예제")
plt.show()
```

## 1.6 다중 플롯 (FacetGrid)
FacetGrid를 사용하면 여러 개의 그래프를 한 번에 그릴 수 있습니다.
```python
g = sns.FacetGrid(df, col="sex", row="time")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
plt.show()
```

## 1.7 Seaborn과 Matplotlib 함께 사용하기
Seaborn 그래프는 Matplotlib과 함께 사용할 수 있습니다.
```python
sns.boxplot(x="day", y="total_bill", data=df)
plt.xlabel("요일")
plt.ylabel("총 지출")
plt.title("Seaborn + Matplotlib 예제")
plt.grid(True)
plt.show()
```

## 1.8 객관식 문제
다음 중 Seaborn에서 데이터 프레임을 기반으로 산점도를 그리는 함수는 무엇인가?

A) sns.barplot()
B) sns.scatterplot()
C) sns.histplot()
D) sns.boxplot()

정답: B
