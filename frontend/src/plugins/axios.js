"use strict";

import Vue from 'vue';
import axios from "axios";
import {MessageBox} from "element-ui";
import router from "../router";

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let config = {
  // baseURL: process.env.baseURL || process.env.apiUrl || "",
  baseURL: "/",
  timeout: 60 * 1000, // Timeout
  // withCredentials: true, // Check cross-site Access-Control
};

const _axios = axios.create(config);

//加载动画
let loading;
let needLoadingRequestCount = 0 ;// 声明一个对象用于存储请求个数
function startLoading () {
  loading = Vue.prototype.$loading({
    lock: true,
    text: '努力加载中...',
    background: 'rgba(0,0,0,0.8)',
    color: '#409EFF',
    target: document.querySelector('.loading-area') // 设置加载动画区域
  })
}
function endLoading () {
  loading.close()
}
function showFullScreenLoading () {
  if (needLoadingRequestCount === 0) {
    startLoading()
  }
  needLoadingRequestCount++;
}
function hideFullScreenLoading () {
  if (needLoadingRequestCount <= 0) return needLoadingRequestCount--;
  if (needLoadingRequestCount === 0) {
    endLoading()
  }
}

_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    let token = localStorage.getItem('Authorization');
    if (config.isLoading !== false) { // 如果配置了isLoading: false，则不显示loading
      startLoading();
      // showFullScreenLoading()
    }
    if(token){
      config.headers.Authorization = token
    }
    return config;
  },
  function(error) {
    // Do something with request error
    hideFullScreenLoading();
    if (error.response) {
      switch (error.response.status) {
        case 401: {
          MessageBox.alert("登录信息失效");
          localStorage.removeItem('Authorization');
          router.replace({
            path: '/',
            query: {redirect: router.currentRoute.fullPath}
          })
        }
      }
    }
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    //暂停加载动画
    loading.close();
    // hideFullScreenLoading();
    return response;
  },
  function(error) {
    // Do something with response error
    loading.close();
    if (error.response) {
      switch (error.response.status) {
        case 401:
          MessageBox.alert("登录信息失效");
          hideFullScreenLoading();
          // 返回 401 清除token信息并跳转到登录页面
          localStorage.removeItem('Authorization');
          router.replace({
            path: '/',
            query: {redirect: router.currentRoute.fullPath}
          });
      }
    }
    return Promise.reject(error);
  }
);

Plugin.install = function(Vue, options) {
  Vue.axios = _axios;
  window.axios = _axios;
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      }
    },
    $axios: {
      get() {
        return _axios;
      }
    },
  });
};

Vue.use(Plugin)

export default Plugin;
