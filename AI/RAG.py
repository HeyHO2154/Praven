import requests
import json

# Flask 서버 URL 및 LLM URL
retrieve_url = "http://ekaf.kro.kr:6000/retrieve"
llm_url = "http://ekaf.kro.kr:11434/v1/chat/completions"
translate_url = "http://ekaf.kro.kr:5000/translate"

def translate_text(text, source_lang, target_lang):
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(translate_url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("translatedText", "Translation Error")
        else:
            print(f"Translation error: {response.status_code}")
            return "Translation Error"
    except requests.exceptions.RequestException as e:
        print(f"Translation request failed: {e}")
        return "Translation Error"

def detect_language(text):
    payload = {
        "q": text,
        "source": "auto",
        "target": "en",
        "format": "text"
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(translate_url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("detectedLanguage", {}).get("language", "en")
        else:
            print(f"Language detection error: {response.status_code}")
            return "en"
    except requests.exceptions.RequestException as e:
        print(f"Language detection request failed: {e}")
        return "en"

def send_message_with_streaming():
    while True:
        # 사용자 입력
        prompt = input("Enter your message (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Exiting... Goodbye!")
            break

        # 입력 언어 감지
        source_lang = detect_language(prompt)
        print("사용자 언어: "+source_lang)

        # Retrieve 단계
        retrieve_payload = {"query": prompt}
        retrieve_headers = {"Content-Type": "application/json"}

        try:
            retrieve_response = requests.post(retrieve_url, json=retrieve_payload, headers=retrieve_headers)

            if retrieve_response.status_code == 200:
                print("Retrieve 성공!")
                retrieve_data = retrieve_response.json()

                # text 필드만 추출하여 하나의 문자열로 합치기
                print("질문 텍스트:", prompt)
                # 질문 번역 (원래 언어에서 영어로)
                temp_qu = translate_text(prompt, source_lang, "en")
                print("번역된 Retrieve 데이터:", temp_qu)

                # text 필드만 추출하여 하나의 문자열로 합치기
                temp_rt = " ".join(item["text"] for item in retrieve_data)
                print("결합된 Retrieve 텍스트:", temp_rt)
                # Retrieve 결과 번역 (원래 언어에서 영어로)
                translated_retrieve_data = translate_text(temp_rt, source_lang, "en")
                print("번역된 Retrieve 데이터:", translated_retrieve_data)

                # LLM 단계
                messages = [
                    {
                        "role": "system",
                        "content": "You are an Police officer, and your task is to accurately understand the provided document and respond accordingly. Only answer based on the given content. Question is "+temp_qu,
                    },
                    {"role": "user", "content": "provided document: "+translated_retrieve_data},
                ]
                print("LLM에 전송될 메시지:", messages)

                llm_payload = {
                    "model": "llama3.2:1b",
                    "messages": messages,
                    "stream": True
                }
                llm_headers = {"Content-Type": "application/json; charset=utf-8"}

                with requests.post(llm_url, headers=llm_headers, data=json.dumps(llm_payload), stream=True) as llm_response:
                    if llm_response.status_code == 200:
                        print("LLM Response stream started:")
                        assistant_response = ""

                        for line in llm_response.iter_lines(decode_unicode=True):
                            if line:
                                line = line.strip()
                                if line.startswith("data:"):
                                    json_string = line[5:].strip()

                                    if json_string == "[DONE]":
                                        print("\n[Complete]\n")
                                        break

                                    try:
                                        decoded_line = json.loads(json_string)
                                        content = decoded_line.get("choices", [{}])[0].get("delta", {}).get("content", "")
                                        assistant_response += content
                                        print(content, end="", flush=True)
                                    except json.JSONDecodeError:
                                        print("\n[Error decoding JSON]\n")

                        # LLM 결과 번역 (영어에서 원래 언어로)
                        translated_response = translate_text(assistant_response, "en", source_lang)
                        print("\n번역된 LLM 응답:", translated_response)
                    else:
                        print(f"[Error] HTTP {llm_response.status_code}: {llm_response.text}")
            else:
                print(f"Retrieve 오류 발생! 상태 코드: {retrieve_response.status_code}")
                print("Retrieve 응답 내용:", retrieve_response.text)

        except requests.exceptions.RequestException as e:
            print(f"요청 중 오류 발생: {e}")

if __name__ == "__main__":
    send_message_with_streaming()
