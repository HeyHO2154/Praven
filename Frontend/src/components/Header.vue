<template>
  <header class="header">
    <div class="header-container">
      <img src="../assets/logo.png" alt="Praven Logo" class="logo" />
      <nav class="nav-menu">
        <ul class="menu-list">
          <li class="dropdown" @mouseenter="showDropdown('news')" @mouseleave="hideDropdown('news')">
            <a :class="{ active: isDropdownVisible.news }" href="#">프라벤 소식지 ▼</a>
            <ul class="dropdown-menu" :class="{ visible: isDropdownVisible.news }">
              <li><a href="#">공지사항</a></li>
              <li><a href="#">활동사진</a></li>
            </ul>
          </li>
          <li>
            <a href="#">회사소개</a>
          </li>
          <li class="dropdown" @mouseenter="showDropdown('service')" @mouseleave="hideDropdown('service')">
            <a :class="{ active: isDropdownVisible.service }" href="#">서비스 ▼</a>
            <ul class="dropdown-menu" :class="{ visible: isDropdownVisible.service }">
              <li><a href="#">파워 클릭커</a></li>
              <li><a href="#">잇(IT)법</a></li>
            </ul>
          </li>
          <li class="dropdown" @mouseenter="showDropdown('contact')" @mouseleave="hideDropdown('contact')">
            <a :class="{ active: isDropdownVisible.contact }" href="#">소통 창구 ▼</a>
            <ul class="dropdown-menu" :class="{ visible: isDropdownVisible.contact }">
              <li><a href="#">문의사항</a></li>
              <li><a href="#">자유게시판</a></li>
            </ul>
          </li>
          <li class="dropdown" @mouseenter="showDropdown('recruit')" @mouseleave="hideDropdown('recruit')">
            <a :class="{ active: isDropdownVisible.recruit }" href="#">입사지원 ▼</a>
            <ul class="dropdown-menu" :class="{ visible: isDropdownVisible.recruit }">
              <li><a href="#">채용공고</a></li>
              <li><a href="#">합격자 발표</a></li>
            </ul>
          </li>
          <li>
            <a href="#">ESG</a>
          </li>
        </ul>
      </nav>
      <div class="login-button">
        <button>로그인</button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader",
  data() {
    return {
      isDropdownVisible: {
        news: false,
        service: false,
        contact: false,
        recruit: false,
      },
    };
  },
  methods: {
    showDropdown(menu) {
      this.isDropdownVisible[menu] = true;
    },
    hideDropdown(menu) {
      this.isDropdownVisible[menu] = false;
    },
  },
};
</script>

<style scoped>
/* Header 전체 스타일 */
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: white;
  z-index: 1000;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px 0;
  display: flex;
  justify-content: center; /* 헤더 전체 중앙 정렬 */
  box-sizing: border-box;
  border-bottom: 1px solid #ddd;
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between; /* 요소 간 동일 간격 배치 */
  width: 100%; /* 헤더의 전체 너비 */
  max-width: 1100px; /* 헤더의 최대 너비 */
}

/* 로고 스타일 */
.logo {
  height: 60px;
}

/* 네비게이션 메뉴 */
.nav-menu {
  flex-grow: 1;
}

.menu-list {
  display: flex;
  justify-content: space-evenly; /* A 글자들 간 동일 간격 */
  list-style: none;
  margin: 0;
  padding: 0;
}

.menu-list a {
  text-decoration: none;
  font-size: 16px;
  color: black;
  padding: 10px 0;
  transition: color 0.1s ease;
}

.menu-list a.active,
.menu-list a:hover {
  color: #f57c00;
}

/* 부모 li 요소를 기준으로 드롭다운 메뉴 위치 지정 */
.menu-list li {
  position: relative; /* 부모 li를 기준으로 드롭다운 메뉴 위치 */
}

/* 드롭다운 메뉴 */
.dropdown-menu {
  position: absolute;
  top: 150%; /* A 글자 바로 아래에 배치 */
  left: 0; /* 부모 li의 왼쪽 기준 */
  background-color: white;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  list-style: none;
  padding: 0;
  margin: 0;
  border: 1px solid #ddd;
  z-index: 1000;
  width: 200px;

  /* 숨김 상태 초기화 */
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.dropdown-menu.visible {
  opacity: 1;
  transform: translateY(0); /* 부드럽게 나타나기 */
  pointer-events: auto;
}


.dropdown-menu li {
  padding: 10px 20px;
  border-bottom: 1px solid #eee;
}

.dropdown-menu li:last-child {
  border-bottom: none;
}

.dropdown-menu li a {
  position: relative; /* ::before를 사용할 수 있도록 position 설정 */
  display: block;
  text-decoration: none;
  font-size: 14px;
  color: black;
  padding: 10px 5px;
  transition: color 0.1s ease, background-color 0.1s ease; /* 배경색 전환 추가 */
}

.dropdown-menu li a:hover,
.dropdown-menu li a.active {
  color: #f57c00;
}

.dropdown-menu li a:hover::before,
.dropdown-menu li a.active::before {
  content: ''; /* 가상 요소 활성화 */
  position: absolute;
  left: -20px; /* 왼쪽으로 이동하여 드롭다운 메뉴에 밀착 */
  top: -10px;
  width: 4px; /* 직사각형 너비 */
  height: 150%; /* 글자의 높이에 맞춤 */
  background-color: #f57c00; /* 주황색 */
  border-radius: 0px; /* 직사각형에 약간의 곡률 */
}


/* 로그인 버튼 */
.login-button button {
  background-color: #f57c00;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.5s ease;
}

.login-button button:hover {
  background-color: #d65f00;
}
</style>
