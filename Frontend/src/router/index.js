import { createRouter, createWebHistory } from 'vue-router';

import nullpage from '@/views/nullpage.vue';
import MainPage from '../views/MainPage.vue';
import About from "../views/About/About.vue";
import PowerClicker from '@/views/Service/PowerClicker.vue';

const routes = [
  { path: '/', component: MainPage, name: 'MainPage' },
  { path: "/about", component: About, name: "About" },
  { path: "/powerclicker", component: PowerClicker, name: "PowerClicker"},
  { path: '/nullpage', component: nullpage, name: 'nullpage' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
