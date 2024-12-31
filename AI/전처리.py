import os
import json
from docx import Document
from sentence_transformers import SentenceTransformer
import re

# 파일 경로 설정
file_path = r"C:\Users\PRO\Desktop\law.docx"  # 원본 문서 경로
output_file_path = r"C:\Users\PRO\Desktop\law_embeddings.json"  # 결과 저장 경로

# 모델 로드
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

# 텍스트 추출 함수
def extract_text_from_docx(file_path):
    """DOCX 파일에서 텍스트 추출"""
    document = Document(file_path)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text.strip() + "\n"
    return text

# 텍스트 전처리 함수
def preprocess_text(text):
    """제N조(*) 패턴을 기준으로 청크 나누기"""
    # "제N조(*)"로 시작하는 텍스트를 기준으로 분리
    chunks = re.split(r'(제\d+조\(.*?\))', text)  # "제N조(내용)"를 기준으로 텍스트를 나눔
    result_chunks = []

    # "제N조(*)"와 그 내용을 합쳐 청크로 만듦
    current_chunk = ""
    for part in chunks:
        if re.match(r'제\d+조\(.*?\)', part):  # "제N조(*)"와 매칭
            if current_chunk:
                result_chunks.append(current_chunk.strip())  # 이전 청크 저장
            current_chunk = part  # 새 조문 시작
        else:
            current_chunk += " " + part  # 조문 내용 추가

    # 마지막 청크 저장
    if current_chunk:
        result_chunks.append(current_chunk.strip())

    # Chunk 1,2 제거
    if result_chunks:
        result_chunks.pop(0)
        result_chunks.pop(0)

    # 후속 전처리: 불필요한 텍스트 제거
    cleaned_chunks = []
    for chunk in result_chunks:
        chunk = re.sub(r'\[[^]]*\]', '', chunk)
        chunk = re.sub(r'\<[^>]*\]', '', chunk)

        chunk = re.sub(r'제\d+장[^\n]*', '', chunk)
        chunk = re.sub(r'제\d+절[^\n]*', '', chunk)
        # chunk = re.sub(r'제\d+조', '', chunk)
        # chunk = re.sub(r'\([^)]*\)', '', chunk)
        # chunk = re.sub(r'\「[^」]*\」', '', chunk)
        # chunk = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩\d+\.]', '', chunk)
        # chunk = re.sub(r'제조', '', chunk)
        # chunk = re.sub(r'제항에 따른', '', chunk)
        # chunk = re.sub(r'에도 불구하고', '', chunk)

        #청크 길이 너무 적은 경우 제거
        if len(chunk.strip()) > 0:
            cleaned_chunks.append(chunk.strip())

    return cleaned_chunks

# 벡터화 함수
def embed_text(data_chunks):
    """청크 데이터를 벡터화"""
    embeddings = model.encode(data_chunks, convert_to_tensor=False)
    return embeddings

# 텍스트와 벡터를 JSON 파일로 저장
def save_to_json(data_chunks, embeddings, output_file_path):
    """텍스트와 벡터 데이터를 JSON 파일로 저장"""
    # 디버깅: 청크와 임베딩 개수 확인
    print(f"Number of Chunks: {len(data_chunks)}")
    print(f"Number of Embeddings: {len(embeddings)}")
    
    if len(data_chunks) != len(embeddings):
        print("Error: Number of chunks and embeddings do not match!")
        return

    # 데이터 저장
    data = [{"text": chunk, "vector": embedding.tolist()} for chunk, embedding in zip(data_chunks, embeddings)]
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # 디버깅: 저장된 데이터 확인
    print(f"Saved {len(data)} chunks to JSON.")

# 메인 처리
if os.path.exists(file_path):
    # 텍스트 추출
    raw_text = extract_text_from_docx(file_path)

    # 텍스트 전처리 및 청크 생성
    chunks = preprocess_text(raw_text)
    print(f"Total Chunks Created: {len(chunks)}")
    for idx, chunk in enumerate(chunks[:20]):  # 첫 20개 청크만 출력
        print(f"Chunk {idx + 1}:\n{chunk}\n{'-'*50}")

    # 벡터화
    embeddings = embed_text(chunks)
    
    # 텍스트와 벡터를 JSON으로 저장
    save_to_json(chunks, embeddings, output_file_path)
    print(f"텍스트와 벡터가 JSON 파일로 저장되었습니다: {output_file_path}")
else:
    print("File not found. Please check the file path.")
