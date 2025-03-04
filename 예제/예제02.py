##▣ 예제2. 주요 라이브러리 소개 (Matplotlib, Seaborn, Plotly 등)

## 1. 주요 라이브러리 소개 (Matplotlib, Seaborn, Plotly 등)

## 1.1 Matplotlib
Matplotlib은 파이썬에서 가장 널리 사용되는 데이터 시각화 라이브러리로, 다양한 유형의 그래프를 생성할 수 있습니다.

### Matplotlib의 특징
- 기본적인 2D 그래프(선 그래프, 막대 그래프, 히스토그램 등) 생성 가능
- 세밀한 그래프 스타일링 및 커스터마이징 가능
- 다양한 형식(PNG, PDF, SVG 등)으로 저장 가능
- 인터랙티브한 플롯 기능 지원

### Matplotlib 사용 예제
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Matplotlib Line Plot')
plt.legend()
plt.show()
```

## 1.2 Seaborn
Seaborn은 Matplotlib을 기반으로 한 통계적 데이터 시각화 라이브러리로, 보다 미적인 그래프를 쉽게 만들 수 있습니다.

### Seaborn의 특징
- Matplotlib보다 간결한 코드로 고급 시각화 가능
- 데이터 프레임 기반으로 차트 생성 가능
- 다양한 테마 및 색상 스타일 지원
- 통계 분석을 위한 시각화 기능 포함 (예: 히트맵, 박스플롯, KDE 그래프 등)

### Seaborn 사용 예제
```python
import seaborn as sns
import pandas as pd

# 예제 데이터셋 로드
df = sns.load_dataset("tips")

# 요일별로 요금 분포를 보여주는 박스플롯
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Box Plot of Total Bill by Day")
plt.show()
```

## 1.3 Plotly
Plotly는 대화형(인터랙티브) 시각화 기능이 뛰어난 라이브러리로, 웹 기반 시각화에 적합합니다.

### Plotly의 특징
- HTML 기반의 인터랙티브한 그래프 생성 가능
- 대화형 차트 (줌, 팬, 호버 기능 포함)
- 다양한 차트 유형 지원 (3D 플롯, 지도 시각화 등)
- Dash 프레임워크와 결합하여 웹 대시보드 제작 가능

### Plotly 사용 예제
```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Interactive Scatter Plot with Plotly")
fig.show()
```

## 1.4 주요 라이브러리 비교
| 라이브러리 | 주요 특징 | 장점 | 단점 |
|------------|----------------|-----------------|-----------------|
| Matplotlib | 기본적인 2D 플롯 | 강력한 커스터마이징 | 코드가 다소 복잡 |
| Seaborn | 통계적 데이터 시각화 | 고급 그래픽 표현 용이 | Matplotlib보다 유연성이 낮음 |
| Plotly | 인터랙티브 그래프 | 웹 대시보드와 호환 가능 | 데이터 크기가 커지면 속도 저하 |

## 1.5 결론
Matplotlib, Seaborn, Plotly는 각각의 장점과 용도를 가지고 있으며, 상황에 맞게 적절한 라이브러리를 선택하는 것이 중요합니다.

## 1.6 객관식 문제
다음 중 인터랙티브한 데이터 시각화를 제공하는 라이브러리는 무엇인가?

A) Matplotlib
B) Seaborn
C) Plotly
D) Pandas

정답: C
