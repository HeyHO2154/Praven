import { createRouter, createWebHistory } from 'vue-router';

import nullpage from '@/views/nullpage.vue';
import MainPage from '../views/MainPage.vue';
import About from "../views/About/About.vue";
import PowerClicker from '@/views/Service/PowerClicker.vue';
import ITlaw from '@/views/Service/ITlaw.vue';
import Borad from '@/views/News/Borad.vue';

const routes = [
  { path: '/nullpage', component: nullpage, name: 'nullpage' },
  { path: '/', component: MainPage, name: 'MainPage' },
  { path: "/about", component: About, name: "About" },
  { path: "/powerclicker", component: PowerClicker, name: "PowerClicker"},
  { path: '/itlaw', component: ITlaw, name: 'ITlaw' },
  { path: '/board', component: Borad, name: 'Borad' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
