<template>
  <div class="app">
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
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style>
/* 전역 스타일 */
</style>
