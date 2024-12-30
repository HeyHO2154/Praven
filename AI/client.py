import requests

# Flask 서버 URL
url = "http://ekaf.kro.kr:6000/retrieve"  # <라즈베리파이_IP>를 실제 IP 주소로 변경하세요.

# 요청 데이터 (JSON 형식)
payload = {
    "query": "길가다가 모르는 사람을 때렸는데... 처벌 받을까요?"
}

# 헤더 설정
headers = {
    "Content-Type": "application/json"
}

# POST 요청 보내기
try:
    response = requests.post(url, json=payload, headers=headers)

    # 응답 처리
    if response.status_code == 200:
        print("응답 성공!")
        print("응답 데이터:", response.json())
    else:
        print(f"오류 발생! 상태 코드: {response.status_code}")
        print("응답 내용:", response.text)

except Exception as e:
    print(f"요청 중 오류 발생: {e}")
