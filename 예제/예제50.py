##▣ 예제50. 데이터 시각화 프로젝트 종합 실습

"""
▣ 데이터 시각화 프로젝트 종합 실습

1. 프로젝트 개요
   데이터 시각화는 데이터를 효과적으로 분석하고 인사이트를 도출하는 중요한 과정이다. 본 실습에서는 다양한 데이터 시각화 기법을 종합적으로 적용하여 실제 데이터셋을 분석한다.

1.1 실습 목표
   - 다양한 데이터 시각화 기법을 활용하여 데이터를 탐색하고 이해한다.
   - 데이터의 분포, 상관관계, 이상치 등을 시각적으로 표현한다.
   - 샘플링, 집계, 밀도 플롯 등 대규모 데이터 시각화 기법을 적용한다.

1.2 사용 라이브러리 및 데이터셋
   - **라이브러리**: pandas, numpy, matplotlib, seaborn, plotly
   - **데이터셋**: `titanic.csv` (타이타닉 생존자 데이터)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 데이터 로드
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

"""
2. 데이터 탐색 및 전처리
"""

# 데이터 구조 확인
print(df.info())
print(df.describe())

# 결측치 확인
print(df.isnull().sum())

# 결측치 처리 (평균 또는 최빈값으로 채우기)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

"""
3. 데이터 분포 시각화
"""

# 나이 분포 히스토그램
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=30, kde=True, color="blue")
plt.title("연령 분포")
plt.xlabel("나이")
plt.ylabel("빈도")
plt.show()

# 성별 분포 막대 그래프
plt.figure(figsize=(6, 4))
sns.countplot(x="Sex", data=df, palette="pastel")
plt.title("성별 분포")
plt.xlabel("성별")
plt.ylabel("수")
plt.show()

"""
4. 상관관계 분석 및 시각화
"""

# 상관관계 행렬 계산
corr_matrix = df.corr()

# 히트맵 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("특성 간 상관관계")
plt.show()

"""
5. 생존자 분석
"""

# 생존자와 나이 분포 비교
plt.figure(figsize=(8, 5))
sns.kdeplot(df[df["Survived"] == 1]["Age"], label="생존자", shade=True, color="green")
sns.kdeplot(df[df["Survived"] == 0]["Age"], label="비생존자", shade=True, color="red")
plt.title("생존 여부에 따른 연령 분포")
plt.xlabel("나이")
plt.ylabel("밀도")
plt.legend()
plt.show()

# 성별에 따른 생존율 분석
plt.figure(figsize=(6, 4))
sns.barplot(x="Sex", y="Survived", data=df, ci=None, palette="muted")
plt.title("성별에 따른 생존율")
plt.xlabel("성별")
plt.ylabel("생존율")
plt.show()

"""
6. 티켓 클래스와 생존율
"""

# Pclass(티켓 등급)별 생존율 비교
plt.figure(figsize=(6, 4))
sns.barplot(x="Pclass", y="Survived", data=df, ci=None, palette="pastel")
plt.title("티켓 등급에 따른 생존율")
plt.xlabel("티켓 등급")
plt.ylabel("생존율")
plt.show()

"""
7. 대규모 데이터 처리를 위한 샘플링 및 집계
"""

# 샘플링 (50% 데이터만 사용하여 시각화)
sampled_df = df.sample(frac=0.5, random_state=42)

plt.figure(figsize=(8, 5))
sns.histplot(sampled_df["Fare"], bins=30, kde=True, color="purple")
plt.title("운임 요금 분포 (샘플링 적용)")
plt.xlabel("운임 요금")
plt.ylabel("빈도")
plt.show()

"""
8. 이상치 탐지 및 시각화
"""

# Boxplot을 활용한 이상치 탐지
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Fare"], color="orange")
plt.title("운임 요금 이상치 탐지")
plt.xlabel("운임 요금")
plt.show()

"""
9. 대화형 시각화 (Plotly 활용)
"""

# Pclass와 생존율을 비교하는 인터랙티브 그래프
fig = px.bar(df, x="Pclass", y="Survived", color="Sex", barmode="group",
             title="티켓 등급 및 성별에 따른 생존율")
fig.show()

"""
10. 프로젝트 결론 및 요약
   - 나이가 어릴수록 생존율이 높은 경향이 보인다.
   - 여성의 생존율이 남성보다 현저히 높다.
   - 1등급 티켓을 가진 승객의 생존율이 높으며, 3등급 승객의 생존율이 가장 낮다.
   - 운임 요금에서 일부 이상치가 발견되었으며, 이는 특이 승객일 가능성이 있다.

11. 객관식 문제
   다음 중 타이타닉 데이터 분석에서 성별에 따른 생존율을 비교하는 가장 적절한 시각화 방법은?

   A) 히스토그램  
   B) KDE Plot  
   C) 막대 그래프 (Bar Plot)  
   D) 산점도 (Scatter Plot)  

   정답: C
"""
