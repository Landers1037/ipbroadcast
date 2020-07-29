import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import axios from 'axios'
import store from './store'
import {MessageBox} from "element-ui";
import echarts from 'echarts'
//import Mock from './mock'
//add es5 support
import '@babel/polyfill'

Vue.prototype.$echarts = echarts; //echarts
//使用axios进行api的请求
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
