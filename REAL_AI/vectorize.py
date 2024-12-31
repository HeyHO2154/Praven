import json
from docx import Document
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def read_docx(file_path):
    """.docx 파일에서 텍스트를 추출"""
    doc = Document(file_path)
    return [para.text for para in doc.paragraphs if para.text.strip()]

def save_to_json(data, output_path):
    """데이터를 JSON 파일로 저장"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def vectorize_lda(documents, n_topics=2):
    """Count 벡터화 후 LDA로 벡터화"""
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(documents)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_matrix = lda.fit_transform(count_matrix)
    return lda_matrix.tolist()

def main(file_path, output_path, method="lda", n_topics=10):
    """
    .docx 파일을 읽고 지정된 방식으로 벡터화한 결과를 JSON으로 저장.
    
    method: "lda" (기본값)
    """
    # .docx 파일 읽기
    documents = read_docx(file_path)
    print(f"문서에서 {len(documents)}개의 문장을 추출했습니다.")
    
    # 벡터화
    if method == "lda":
        vectors = vectorize_lda(documents, n_topics=n_topics)
    else:
        raise ValueError("현재 지원되는 방식은 'lda' 뿐입니다.")
    
    # 결과를 JSON으로 저장
    data = {"documents": documents, "vectors": vectors}
    save_to_json(data, output_path)
    print(f"결과가 {output_path}에 저장되었습니다.")

# 실행 예시
if __name__ == "__main__":
    input_file = r"C:\Users\SSAFY\Desktop\data.docx"  # .docx 파일 경로
    output_file = r"C:\Users\SSAFY\Desktop\output.json"  # 저장할 JSON 파일 경로
    main(input_file, output_file, method="lda", n_topics=100)  # LDA 방식
