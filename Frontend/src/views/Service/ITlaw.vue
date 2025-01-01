<template>
  <div class="itlaw-container">
    <!-- 배경 이미지 -->
    <div class="background-image">
      <img src="@/assets/lawyer.png" alt="Lawyer Background" class="background-img" />
    </div>

    <!-- AI 채팅 영역 -->
    <div class="chat-box">
      <div class="ai-response">
        <h2>법률 AI 서비스</h2>
        <p v-if="relatedLaws.length > 0"><strong>관련 법 조항:</strong></p>
        <ul v-if="relatedLaws.length > 0">
          <li v-for="(law, index) in relatedLaws" :key="index">{{ law }}</li>
        </ul>
        <p v-if="aiAdvice"><strong>변호사 AI 조언:</strong></p>
        <p>{{ aiAdvice }}</p>
      </div>
      
      <!-- 사용자 입력 필드 -->
      <div class="input-container">
        <input 
          type="text" 
          v-model="userInput" 
          placeholder="법적 질문을 입력해주세요..." 
        />
        <button @click="sendQuestion">보내기</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ITlawPage",
  data() {
    return {
      userInput: "", // 사용자가 입력한 질문
      relatedLaws: [], // 관련 법 조항
      aiAdvice: "", // 변호사 AI의 최종 조언
      originalLanguage: "ko", // 기본 언어
    };
  },
  methods: {
    async sendQuestion() {
      if (!this.userInput.trim()) {
        alert("질문을 입력해주세요.");
        return;
      }

      try {
        // 1. Retrieve 단계 (관련 법 조항 가져오기)
        const retrieveResponse = await fetch("http://ekaf.kro.kr:25901/retrieve", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ query: this.userInput }),
        });
        const retrieveData = await retrieveResponse.json();
        this.relatedLaws = retrieveData.map((item) => item.text);

        // 2. 관련 법 조항 번역 (한국어 → 영어)
        const translateRetrieveResponse = await fetch("http://ekaf.kro.kr:25901/translate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            q: this.relatedLaws.join(" "),
            source: "ko",
            target: "en",
          }),
        });
        const translatedRetrieveData = await translateRetrieveResponse.json();
        const translatedRetrieveText = translatedRetrieveData.translatedText;

        // 3. LLM 모델로 질문과 번역된 법 조항 전송
        const llmResponse = await fetch("http://ekaf.kro.kr:25901/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            model: "llama3.2:1b",
            messages: [
              { role: "system", content: "You are a helpful legal assistant." },
              { role: "user", content: `Question: ${this.userInput}\nRelated Laws: ${translatedRetrieveText}` },
            ],
            stream: false,
          }),
        });
        const llmData = await llmResponse.json();
        const llmAdvice = llmData.choices[0].message.content;

        // 4. LLM 모델 응답 번역 (영어 → 한국어)
        const finalTranslationResponse = await fetch("http://ekaf.kro.kr:25901/translate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            q: llmAdvice,
            source: "en",
            target: "ko",
          }),
        });
        const finalTranslation = await finalTranslationResponse.json();
        this.aiAdvice = finalTranslation.translatedText;

      } catch (error) {
        console.error("Error:", error);
        alert("문제가 발생했습니다. 다시 시도해주세요.");
      }
    },
  },
};
</script>

<style scoped>
.itlaw-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: relative;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: -1; /* 배경 이미지가 다른 요소들 뒤로 가게 설정 */
}

.background-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.chat-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.8); /* 반투명 배경 */
  padding: 30px;
  border-radius: 10px;
  width: 60%;
  max-width: 800px;
  margin-top: 20px;
}

.ai-response h2 {
  font-size: 1.8rem;
  margin-bottom: 20px;
  text-align: center;
}

.ai-response p {
  font-size: 1rem;
  color: #333;
  margin-bottom: 10px;
}

.ai-response ul {
  list-style-type: disc;
  padding-left: 20px;
}

.input-container {
  display: flex;
  margin-top: 20px;
}

.input-container input {
  padding: 10px;
  font-size: 1rem;
  width: 80%;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.input-container button {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #f57c00;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 10px;
}

.input-container button:hover {
  background-color: #e76f00;
}
</style>
