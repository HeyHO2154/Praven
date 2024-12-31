from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS 추가
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Flask 앱 생성
app = Flask(__name__)
CORS(app)  # CORS 설정 추가

# 모델 로드
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

# JSON 파일 경로
json_file_path = r"/home/junma97/Desktop/law_embeddings.json"

# JSON 데이터 로드
def load_data(json_file_path):
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# 코사인 유사도 기반 검색 함수
def retrieve_top_k(query, data, model, top_k=5):
    query_vector = model.encode(query, convert_to_tensor=True).cpu().numpy()
    
    results = []
    for item in data:
        text = item["text"]
        vector = np.array(item["vector"])
        similarity = cosine_similarity([query_vector], [vector])[0][0]
        results.append((text, similarity))

    # 유사도 기준으로 정렬
    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results[:top_k]

# 데이터 로드
data = load_data(json_file_path)

# HTTP POST 요청 처리
@app.route("/retrieve", methods=["POST"])
def retrieve():
    # 요청 데이터에서 쿼리 가져오기
    input_data = request.json
    query = input_data.get("query", "")
    
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # 유사한 문장 검색
    top_k_results = retrieve_top_k(query, data, model, top_k=5)

    # 결과 반환
    response = [{"text": text, "similarity": similarity} for text, similarity in top_k_results]
    return jsonify(response)

# 서버 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
