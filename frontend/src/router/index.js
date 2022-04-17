/* eslint-disable */
import Vue from 'vue';
import VueRouter from 'vue-router';
import VueTabs from 'vue-nav-tabs';

import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Registration from '../views/Registration.vue';
import Questions from '../views/Questions.vue';
import Zobry from '../views/Zobry.vue';
import AuthenticatedPing from '../views/AuthenticatedPing.vue';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../services/api/auth';

Vue.use(VueRouter);
Vue.use(VueTabs);

const PUBLIC_PATHS = ['/', '/register', '/login'];

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/questions',
    name: 'Question',
    component: Zobry
  },
  {
    path: '/register',
    name: 'Registration',
    component: Registration,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/ping',
    name: 'AuthenticatedPing',
    component: AuthenticatedPing,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});


const unAuthenticatedAndPrivatePage = (path) => (!PUBLIC_PATHS.includes(path)
    && !(ACCESS_TOKEN in window.localStorage)
    && !(REFRESH_TOKEN in window.localStorage));

router.beforeEach((to, from, next) => {
  if (unAuthenticatedAndPrivatePage(to.path)) {
    next(`/login?next=${to.path}`);
  } else {
    next();
  }
});

export default router;