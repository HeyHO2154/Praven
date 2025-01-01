import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';  //http 통신 보내는 라이브러리

const app = createApp(App);

// Axios 전역 등록
app.config.globalProperties.$axios = axios;

app.use(router).mount('#app');
