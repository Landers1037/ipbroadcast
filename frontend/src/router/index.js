import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'index',
    component: () => import("../pages/index"),
    meta: {
      isLogin: true
    }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import("../pages/about")
  },
  {
    path: '/console',
    name: 'myconsole',
    component: () => import("../pages/my-console"),
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import("../pages/dashboard"),
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/echarts',
    name: 'echarts',
    component: () => import("../pages/echarts_console"),
  },
  {
    path: '/doc',
    name: 'doc',
    component: () => import("../pages/doc")
  },
  {
    path: '/dashboard/log',
    component: () => import("../pages/ds_log")
  },
  {
    path: '/middle',
    name: 'middle',
    component: () => import("../pages/middle")
  },
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router
