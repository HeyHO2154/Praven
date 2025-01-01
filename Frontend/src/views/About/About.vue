<template>
    <section class="info-section">
      <h2>프라벤은 색다른 재미를 추구합니다</h2>
      <p>고객과의 소통을 통해 사용자 맞춤형 게임을 제작하여, 인디 게임의 강점을 극대화합니다.</p>
      <div class="info-cards">
        <div class="info-card">
          <img src="@/assets/mysql.png" alt="MySQL Logo" />
          <h3>안전한 데이터베이스</h3>
          <p>MySQL과 MariaDB를 사용하여, 사용자 데이터와 게임 및 사이트 정보를 안전하게 저장합니다.</p>
        </div>
        <div class="info-card">
          <img src="@/assets/springboot.png" alt="Spring Boot Logo" />
          <h3>최적화된 로직</h3>
          <p>프론트와 백엔드간 정보 중 필수적인 내용만 백엔드에서 활용하여 HTTP 통신을 최소화합니다.</p>
        </div>
        <div class="info-card">
          <img src="@/assets/flutter.png" alt="Flutter Logo" />
          <h3>사용자 친화적 UI</h3>
          <p>다양한 테스터들과 함께 환경을 테스트하며 사용자 편의성을 극대화하기 위해 개선해 나갑니다.</p>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "AboutPage",
  };
  </script>
  
  <style scoped>
  .info-section {
    text-align: center;
    padding: 50px 20px;
    background-color: white;
    margin-top: 60px;
    margin-bottom: 80px;
  }
  .info-section h2 {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 10px;
  }
  .info-section p {
    font-size: 1.2rem;
    color: #555;
    margin-bottom: 30px;
  }
  .info-cards {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  .info-card {
    text-align: center;
    max-width: 300px;
  }
  .info-card img {
    width: 50%;
    height: auto;
    margin-bottom: 15px;
  }
  .info-card h3 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  .info-card p {
    font-size: 1rem;
    color: #777;
  }
  </style>
  