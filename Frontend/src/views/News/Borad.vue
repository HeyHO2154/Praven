<template>
  <div class="post-list-container">
    <!-- 상단 메뉴 -->
    <div class="menu-bar">
      <button class="menu-button active">전체글</button>
      <button class="menu-button">개념글</button>
      <button class="menu-button">공지</button>
    </div>

    <!-- 게시글 테이블 -->
    <table class="post-table">
      <thead>
        <tr>
          <th class="number-column">번호</th>
          <th class="title-column">제목</th>
          <th class="author-column">글쓴이</th>
          <th class="date-column">작성일</th>
          <th class="views-column">조회</th>
          <th class="recommendations-column">추천</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in posts" :key="post.id" @click="goToPost(post.id)">
          <td>{{ post.id }}</td>
          <td class="post-title">
            <span v-if="post.type" class="post-type">{{ post.type }}</span>
            {{ post.title }}
          </td>
          <td>{{ post.author }}</td>
          <td>{{ post.date }}</td>
          <td>{{ post.views }}</td>
          <td>{{ post.recommendations }}</td>
        </tr>
      </tbody>
    </table>

    <!-- 하단 글쓰기 버튼 -->
    <div class="write-post">
      <button>글쓰기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostListPage",
  data() {
    return {
      posts: [
        { id: 2615, title: "게임 때문에 가장 큰 타격 입은 것 같은 스타는?", author: "운영자", date: "24.12.30", views: "-", recommendations: "-", type: "질문" },
        { id: 2614, title: "제주공항 여객기 사고 관련", author: "운영자", date: "24.12.31", views: "-", recommendations: "-", type: "공지" },
        { id: 2613, title: "왜 먹하노", author: "ㅇㅇ", date: "09:57", views: 78, recommendations: "-" },
        { id: 2612, title: "존나 잘먹고 잘사는거 같은데", author: "ㅇㅇ", date: "24.12.31", views: 99, recommendations: 12 },
        { id: 2611, title: "선적의 또 솔충하더라", author: "ㅇㅇ", date: "24.12.30", views: 112, recommendations: 2 },
        { id: 2610, title: "갤주가 후원만 뜯어가고 몸을 상담히 사리는거 같음.", author: "ㅇㅇ", date: "24.12.29", views: 260, recommendations: 24 },
        { id: 2609, title: "생활바카라 성공기", author: "조투니", date: "24.12.27", views: 73, recommendations: 0 },
        { id: 2608, title: "밥밥이 사이비", author: "조투니", date: "24.12.27", views: 185, recommendations: 7 },
        { id: 2607, title: "ㅇㅇ", author: "ㅇㅇ", date: "24.12.26", views: 68, recommendations: 0 },
        { id: 2606, title: "[지만원 메시지 464] 이역 국민께 드리는 격문(읽음)", author: "항상겸손하게", date: "24.12.26", views: 118, recommendations: 2 },
      ],
    };
  },
  methods: {
    goToPost(postId) {
      alert(`게시글 ${postId}로 이동합니다.`);
    },
  },
};
</script>

<style scoped>
/* 전체 컨테이너 */
.post-list-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

/* 상단 메뉴 스타일 */
.menu-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.menu-button {
  padding: 10px 20px;
  border: 1px solid #ddd;
  background-color: #f1f1f1;
  cursor: pointer;
  font-size: 1rem;
}

.menu-button.active {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

/* 테이블 스타일 */
.post-table {
  width: 100%;
  border-collapse: collapse;
}

.post-table thead {
  border-top: 2px solid #333; /* 상단 굵은 줄 */
  border-bottom: 1px solid #333; /* 하단 줄 */
}

.post-table th {
  padding: 10px;
  font-size: 0.9rem;
  font-weight: bold; /* 글씨 더 굵게 */
  text-align: center;
}

/* 테이블 셀 스타일 */
.post-table td {
  padding: 10px;
  font-size: 0.9rem;
  text-align: center;
  border-bottom: 1px solid #ddd;
}

/* 제목 열 좌측 정렬 */
.post-title {
  text-align: left !important; /* 좌측 정렬 강제 적용 */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.post-title:hover {
  color: #0056b3;
  cursor: pointer;
}

.post-type {
  display: inline-block;
  background-color: #ffdd57;
  color: #333;
  font-size: 0.8rem;
  padding: 2px 5px;
  border-radius: 3px;
  margin-right: 5px;
}

/* 열 너비 조정 */
.number-column {
  width: 7%;
}
.title-column {
  width: 55%;
}
.author-column {
  width: 15%;
}
.date-column {
  width: 10%;
}
.views-column,
.recommendations-column {
  width: 7.5%;
}

/* 글쓰기 버튼 */
.write-post {
  text-align: right;
  margin-top: 20px;
}

.write-post button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.write-post button:hover {
  background-color: #0056b3;
}
</style>
