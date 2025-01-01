<template>
    <footer>
      <p>개발자: 허성준</p>
      <p>이메일: junma97@naver.com</p>
      <p>
        <a href="https://sites.google.com/view/praven-privacy/%ED%99%88" target="_blank">개인정보처리방침</a>
      </p>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'AppFooter',
  };
  </script>
  
  <style>
  footer {
    background-color: #e1770e;
    color: white;
    padding: 5px;
    text-align: center;
  }
  footer p {
    margin: 10px 0; /* 상하 간격 5px로 설정 */
    line-height: 1.2; /* 줄 간격 줄이기 */
  }
  footer a:visited {
    color: white; /* 클릭 후에도 링크 색상 유지 */
    border-bottom: 1px solid white; /* 클릭 후 밑줄 색상 유지 */
  }

  /* 기본 여백 제거 */
  body {
    margin: 0;
    padding: 0;
  }
  </style>
  