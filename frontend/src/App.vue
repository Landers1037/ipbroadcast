<template>
  <div id="app">
<!--      <keep-alive>-->
<!--        <router-view v-if="$route.meta.keepAlive"></router-view>-->
<!--      </keep-alive>-->
<!--      <router-view v-if="!$route.meta.keepAlive"></router-view>-->
      <router-view></router-view>
  </div>
</template>

<script>

</script>

<style>
*{
  margin: 0;
  padding: 0;
}
html{height: 100%;width:100%}
body{margin: 0;background-color: #f5f5f5;height: 100%;width: 100%}

#app {
  font-family: 'sh',sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  text-decoration: none!important;
  border-bottom: none;
  height: 100%;
  width: 100%;
}

@media (max-width: 1600px) and (min-width: 600px) {
  .el-message-box{width: 420px!important;}
}
@media (max-width: 600px) and (min-width: 300px) {
  .el-message-box{width: 300px!important;}
}
</style>
