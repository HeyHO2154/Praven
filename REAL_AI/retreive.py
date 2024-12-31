import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity

def load_json(file_path):
    """JSON 파일 로드"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def vectorize_lda_single(input_text, documents, n_topics=2):
    """단일 문장을 LDA 방식으로 벡터화"""
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(documents + [input_text])
    
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_matrix = lda.fit_transform(count_matrix)
    
    return lda_matrix[-1]  # 입력 문장의 벡터 반환

def find_top_similar_vectors(input_vector, vectors, top_n=5):
    """입력 벡터와 저장된 벡터 간의 유사도를 계산하여 상위 N개 반환"""
    similarities = cosine_similarity([input_vector], vectors)[0]
    top_indices = np.argsort(similarities)[::-1][:top_n]
    
    return [(index, similarities[index]) for index in top_indices]

def main(input_text, json_path, n_topics=2, top_n=5):
    """
    사용자 입력 문장을 벡터화하여 JSON 파일의 벡터와 비교한 상위 N개의 유사도를 출력.
    
    input_text: 사용자 입력 문장
    json_path: 벡터와 문장이 저장된 JSON 파일 경로
    """
    # JSON 로드
    data = load_json(json_path)
    documents = data["documents"]
    stored_vectors = np.array(data["vectors"])
    
    # 입력 문장을 벡터화
    input_vector = vectorize_lda_single(input_text, documents, n_topics=n_topics)
    
    # 상위 N개의 유사도 계산
    top_similar = find_top_similar_vectors(input_vector, stored_vectors, top_n=top_n)
    
    # 결과 출력
    print()
    for rank, (index, similarity) in enumerate(top_similar, 1):
        print(f"{rank}. 유사도: {similarity:.4f}, 문장: {documents[index]}")

# 실행 예시
if __name__ == "__main__":
    # 사용자 입력
    input_sentence = input("문장을 입력하세요: ")
    
    # JSON 파일 경로
    json_file_path = r"C:\Users\SSAFY\Desktop\output.json"
    
    # LDA 방식으로 유사도 계산 및 출력
    main(input_sentence, json_file_path, n_topics=100, top_n=5)
