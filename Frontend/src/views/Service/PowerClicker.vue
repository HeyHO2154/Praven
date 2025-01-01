<template>
    <section class="power-clicker-section">
      <div class="title-container">
        <h2>주요 어플리케이션</h2>
        <p>Main Application</p>
      </div>
      <div class="content-container">
        <div class="text-content">
          <h3>파워클리커</h3>
          <p>
            파워클리커는 단순한 클릭 게임으로 출시되고 시간에 간편하게 좋은 게임입니다.
            타겟층은 평소 업무나 활동이 많아 피로하여 깊은 게임은 하기 어려운 2030 직장인들을 대상으로 하였습니다.
          </p>
          <p><strong>주요 컨텐츠는 아래와 같습니다</strong></p>
          <ul>
            <li>게임 서버 기반형 회원관리</li>
            <li>모든 회원 포인트 순위 확인 및 경쟁</li>
            <li>사용자 테마 구매 및 변경</li>
            <li>고양이 클릭을 통한 포인트 획득</li>
            <li>강아지 피하기를 통한 포인트 획득</li>
            <li>카드 게임을 통한 포인트 베팅</li>
          </ul>
          <!-- 다운로드 버튼 -->
          <div class="download-buttons">           
            <a href="https://play.google.com/store/apps/details?id=com.hsj.powerclicker" target="_blank">
              <img src="@/assets/downloadG.png" alt="download" class="download-icon" />
              <img src="@/assets/downloadA.png" alt="download" class="download-icon" />
            </a>
          </div>
        </div>
        <div class="image-content">
          <img src="@/assets/powerclicker.png" alt="PowerClicker Image" />
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "PowerClickerPage",
  };
  </script>
  
  <style scoped>
  /* 전체 섹션 스타일 */
  .power-clicker-section {
    padding: 50px 20px;
    text-align: center;
    background-color: white;
  }
  
  /* 제목 스타일 */
  .title-container {
    margin-bottom: 40px;
  }
  
  .title-container h2 {
    font-size: 2rem;
    font-weight: bold;
    margin: 0;
  }
  
  .title-container p {
    font-size: 1.2rem;
    color: gray;
    margin: 5px 0 0 0;
  }
  
  /* 내용 컨테이너 스타일 */
  .content-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
    flex-wrap: wrap;
  }
  
  /* 텍스트 컨텐츠 스타일 */
  .text-content {
    max-width: 600px;
    text-align: left;
  }
  
  .text-content h3 {
    font-size: 1.8rem;
    color: #f57c00;
    margin-bottom: 10px;
  }
  
  .text-content p {
    font-size: 1.1rem;
    color: #555;
    margin-bottom: 20px;
    line-height: 1.6;
  }
  
  .text-content ul {
    list-style-type: disc;
    padding-left: 20px;
    color: #555;
  }
  
  .text-content ul li {
    margin-bottom: 10px;
  }
  
  /* 이미지 컨텐츠 스타일 */
  .image-content {
    position: relative;
    text-align: center;
  }
  
  .image-content img {
    max-width: 90%;
    height: auto;
    border-radius: 10px;
  }
  
  .download-buttons {
  margin-left: 20px;
  display: flex; /* Flexbox를 사용하여 내부 요소를 가로로 정렬 */
  justify-content: center; /* 가운데 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
}

.download-buttons a {
  display: flex; /* 각 링크 안에서도 내부 요소를 가로 정렬 */
  flex-direction: row; /* 기본값으로 가로 정렬 */
  gap: 1%;
}

.download-icon {
  width: 50%; /* 적절한 크기 조정 */
  height: auto;
  cursor: pointer;
  transition: transform 0.3s ease; /* 호버 시 효과 추가 */
}

.download-icon:hover {
  transform: scale(1.1); /* 호버 시 확대 */
}

  </style>
  