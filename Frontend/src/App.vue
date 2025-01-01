<template>
  <div id="app">
    <!-- 헤더 컴포넌트 -->
    <AppHeader />

    <!-- 라우트에 따라 화면 표시 -->
    <router-view />

    <!-- 푸터 컴포넌트 -->
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from './components/Header.vue';
import AppFooter from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style>
/* 글로벌 스타일 또는 루트 요소에 대한 스타일 */
#app {
  text-align: center;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
