from flask import Flask, request, jsonify
from flask_cors import CORS  # CORS 라이브러리 추가
import requests

app = Flask(__name__)
CORS(app)  # Flask 앱에 CORS 적용

# 원격 백엔드 URL
BACKEND_URLS = {
    "retrieve": "http://ekaf.kro.kr:8000/retrieve",
    "translate": "http://ekaf.kro.kr:5000/translate",
    "chat": "http://ekaf.kro.kr:11434/v1/chat/completions",
}

@app.route("/retrieve", methods=["POST"])
def proxy_retrieve():
    return handle_proxy("retrieve")

@app.route("/translate", methods=["POST"])
def proxy_translate():
    return handle_proxy("translate")

@app.route("/chat", methods=["POST"])
def proxy_chat():
    return handle_proxy("chat")

def handle_proxy(endpoint):
    try:
        # 백엔드 URL 가져오기
        backend_url = BACKEND_URLS.get(endpoint)
        if not backend_url:
            print(f"Invalid endpoint: {endpoint}")
            return jsonify({"error": "Invalid endpoint"}), 404

        # 클라이언트 요청 데이터
        client_data = request.json
        print(f"클라이언트 요청 데이터 ({endpoint}): {client_data}")
        if not client_data:
            print("Invalid request data")
            return jsonify({"error": "Invalid request data"}), 400

        # 백엔드로 요청 전달
        backend_response = requests.post(
            backend_url,
            json=client_data,
            headers={"Content-Type": "application/json"}
        )

        # 백엔드 응답 처리
        print(f"백엔드 응답 상태 코드 ({endpoint}): {backend_response.status_code}")
        if backend_response.status_code == 200:
            print(f"백엔드 응답 데이터 ({endpoint}): {backend_response.json()}")
            return jsonify(backend_response.json())
        else:
            print(f"백엔드 오류 ({endpoint}): {backend_response.text}")
            return jsonify({"error": "Backend error", "details": backend_response.text}), backend_response.status_code

    except Exception as e:
        print(f"예외 발생 ({endpoint}): {str(e)}")
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=25901)
