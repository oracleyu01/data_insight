##▣ 예제35. Word2Vec 결과를 2D 공간에서 시각화

## 1. Word2Vec 결과를 2D 공간에서 시각화
Word2Vec은 단어를 벡터로 변환하는 자연어 처리 기법으로, 유사한 단어들이 가까운 벡터 공간에 위치하도록 학습됩니다. 이 결과를 2D 공간에서 시각화하면 단어 간의 관계를 직관적으로 이해할 수 있습니다.

## 1.1 Word2Vec의 특징
- 단어 간의 의미적 유사성을 벡터 공간에서 분석 가능
- 고차원 벡터를 저차원으로 차원 축소하여 시각화 가능
- 유사한 의미를 가진 단어들이 가까운 위치에 배치됨

## 1.2 Word2Vec 모델 학습 및 벡터 생성
```python
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# 샘플 문장 데이터
sentences = [
    "I love machine learning and deep learning.",
    "Natural language processing is amazing.",
    "I enjoy solving problems with AI.",
    "Word2Vec helps to understand word embeddings.",
    "Neural networks are the backbone of AI."
]

# 토큰화 수행
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Word2Vec 모델 학습
model = Word2Vec(tokenized_sentences, vector_size=10, window=3, min_count=1, workers=4)
```

## 1.3 Word2Vec 벡터를 2D로 차원 축소하여 시각화
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 단어 리스트 및 벡터 추출
words = list(model.wv.index_to_key)
vectors = np.array([model.wv[word] for word in words])

# PCA를 이용한 2D 차원 축소
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

# 시각화
plt.figure(figsize=(8, 6))
for word, coord in zip(words, reduced_vectors):
    plt.scatter(coord[0], coord[1], color='blue')
    plt.text(coord[0]+0.02, coord[1]+0.02, word, fontsize=12)
plt.title("Word2Vec Embeddings Visualization (PCA)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid()
plt.show()
```

## 1.4 t-SNE를 활용한 Word2Vec 시각화
PCA보다 더 나은 시각적 분포를 위해 t-SNE를 활용할 수도 있습니다.
```python
from sklearn.manifold import TSNE

# t-SNE를 활용한 2D 차원 축소
tsne = TSNE(n_components=2, random_state=42, perplexity=3)
tsne_vectors = tsne.fit_transform(vectors)

# 시각화
plt.figure(figsize=(8, 6))
for word, coord in zip(words, tsne_vectors):
    plt.scatter(coord[0], coord[1], color='green')
    plt.text(coord[0]+0.02, coord[1]+0.02, word, fontsize=12)
plt.title("Word2Vec Embeddings Visualization (t-SNE)")
plt.xlabel("t-SNE Component 1")
plt.ylabel("t-SNE Component 2")
plt.grid()
plt.show()
```

## 1.5 Word2Vec 결과 시각화의 활용 예시
- 단어 유사도 분석 및 군집화
- 텍스트 데이터에서 주요 개념 파악
- 챗봇 및 추천 시스템에서 유사한 단어 군집 확인

## 1.6 객관식 문제
다음 중 Word2Vec 벡터를 2D로 차원 축소하여 시각화하는 데 사용될 수 있는 기법은 무엇인가?

A) PCA
B) t-SNE
C) UMAP
D) 위의 모든 방법

정답: D
