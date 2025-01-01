<template>
    <div class="coming-soon">
      <p>준비중인 페이지입니다</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "ComingSoonPage",
  };
  </script>
  
  <style scoped>
  .coming-soon {
    display: flex; /* 중앙 정렬을 위한 Flexbox */
    justify-content: center; /* 수평 중앙 정렬 */
    align-items: center; /* 수직 중앙 정렬 */
    height: 100vh; /* 화면 전체 높이 */
    background-color: #ffffff; /* 배경색 (원하면 변경 가능) */
  }
  
  .coming-soon p {
    font-size: 2.5rem; /* 글자 크기 */
    color: #f57c00; /* 주황색 글자 */
    font-weight: bold; /* 굵은 글자 */
    text-align: center; /* 텍스트 중앙 정렬 */
  }
  </style>
  