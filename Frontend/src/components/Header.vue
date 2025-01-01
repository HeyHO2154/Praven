<template>
  <header class="header">
    <div class="logo-container">
      <img src="../assets/logo.png" alt="Praven Logo" class="logo" />
    </div>
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
  padding: 20px 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  box-sizing: border-box;
}

/* 로고 컨테이너 */
.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  height: 60px;
  margin-right: 10px;
}

/* 네비게이션 메뉴 */
.nav-menu {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.menu-list {
  display: flex;
  gap: 0%;
  list-style: none;
  margin: 0;
  padding: 0;
  position: relative;
}

.menu-list li {
  position: relative;
}

.menu-list a {
  display: block;
  padding: 20px 20px;
  text-decoration: none;
  font-size: 16px;
  color: black;
  transition: color 0.1s ease;
}

.menu-list a.active,
.menu-list a:hover {
  color: #f57c00;
}

/* 드롭다운 메뉴 스타일 */
.dropdown-menu {
  position: absolute;
  top: 90%;
  left: 0;
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
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.dropdown-menu.visible {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.dropdown-menu li {
  padding: 10px 30px;
  border-bottom: 1px solid #eee;
}

.dropdown-menu li:last-child {
  border-bottom: none;
}

.dropdown-menu li a {
  display: block;
  padding: 10px 0px;
  text-decoration: none;
  font-size: 14px;
  color: black;
  transition: color 0.1s ease;
}

.dropdown-menu li a:hover {
  color: #f57c00;
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
