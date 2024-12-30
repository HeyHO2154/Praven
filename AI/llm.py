import requests
import json

def send_message_with_streaming():
    api_url = "http://ekaf.kro.kr:11434/v1/chat/completions"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        # 사용자 입력
        prompt = input("Enter your message (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Exiting... Goodbye!")
            break

        # 메시지 추가
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": "llama3.2:1b",
            "messages": messages,
            "stream": True
        }
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }

        try:
            # 스트리밍 요청
            with requests.post(api_url, headers=headers, data=json.dumps(payload), stream=True) as response:
                if response.status_code == 200:
                    print("Response stream started:")
                    assistant_response = ""

                    for line in response.iter_lines(decode_unicode=True):
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
                else:
                    print(f"[Error] HTTP {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"[Error] Request failed: {e}")

if __name__ == "__main__":
    send_message_with_streaming()
