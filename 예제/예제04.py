## ▣ 예제4. 한글 폰트 설정 및 그래프 저장 방법

## 1. 한글 폰트 설정 및 그래프 저장 방법
Matplotlib에서 한글을 올바르게 표시하려면 한글 폰트를 설정해야 합니다. 또한, 그래프를 다양한 형식으로 저장할 수도 있습니다.

## 1.1 한글 폰트 설정하기
Matplotlib은 기본적으로 한글을 지원하지 않으며, 한글이 깨지는 문제가 발생할 수 있습니다. 이를 해결하기 위해 적절한 한글 폰트를 설정해야 합니다.

### 한글 폰트 설정 예제
```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (예: 맑은 고딕)
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 사용자의 경우
# plt.rcParams['font.family'] = 'AppleGothic'  # macOS 사용자의 경우
# plt.rcParams['font.family'] = fm.FontProperties(fname='/usr/share/fonts/truetype/nanum/NanumGothic.ttf').get_name()  # Linux 사용자의 경우

plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

# 그래프 그리기
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.plot(x, y, marker='o', linestyle='--', color='b')
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.title("한글 폰트 설정 예제")
plt.show()
```

## 1.2 시스템 내 설치된 한글 폰트 확인하기
사용 가능한 한글 폰트를 확인하고 적절한 폰트를 선택할 수 있습니다.

### 설치된 한글 폰트 확인 예제
```python
import matplotlib.font_manager as fm

# 시스템 내 설치된 폰트 목록 확인
for font in fm.findSystemFonts():
    if "Nanum" in font or "Malgun" in font or "Apple" in font:
        print(font)
```

## 1.3 그래프 저장 방법
Matplotlib에서는 `savefig()` 함수를 사용하여 그래프를 파일로 저장할 수 있습니다.

### 그래프 저장 기본 예제
```python
plt.plot(x, y, marker='s', linestyle='-', color='g')
plt.xlabel("X 축")
plt.ylabel("Y 축")
plt.title("그래프 저장 예제")
plt.savefig("graph.png", dpi=300)  # PNG 형식으로 저장 (300 DPI)
plt.show()
```

### 다양한 파일 형식으로 저장하기
Matplotlib은 여러 형식(PNG, PDF, SVG, JPG 등)으로 그래프를 저장할 수 있습니다.
```python
plt.savefig("graph.pdf")  # PDF 파일로 저장
plt.savefig("graph.svg")  # SVG 파일로 저장
plt.savefig("graph.jpg", dpi=200)  # JPG 파일로 저장 (200 DPI)
```

### 투명한 배경으로 저장하기
```python
plt.savefig("transparent_graph.png", transparent=True, dpi=300)
```

## 1.4 객관식 문제
Matplotlib에서 그래프를 파일로 저장하는 함수는 무엇인가?

A) plt.store()
B) plt.save()
C) plt.savefig()
D) plt.export()

정답: C
