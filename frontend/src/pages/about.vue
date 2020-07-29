<template>
    <div id="main">
        <h2 style="margin-bottom: 20px">关于该项目</h2>
        <p><span style="color: #0079ba">NMS</span>基于PCBA智能硬件的ip广播管理系统</p>
        <p>设计者：廖仁杰 华中科技大学</p>
        <p>2020 毕业设计</p>
        <img src="../assets/nms.jpg" class="nms-logo">
        <br>
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>开发工具</span>
            </div>
            <div :key="t" v-for="(t,index) in items"  class="text item">
                <p v-if="index >= 3" style="color: darkcyan;font-weight: bold">{{ t }}</p>
                <p v-else style="font-weight: bold;color: cornflowerblue">{{ t }}</p>
            </div>
        </el-card>
        <h3 style="margin-top: 30px">项目地址</h3>
        <a href="https://github.com/landers1037/ipbroadcast">https://github.com/landers1037/ipbroadcast</a>

    </div>
</template>

<script>
    export default {
        name: "about",
        data() {
            return{
                items : ['Pycharm','Webstorm','Chrome','Python3.7','Vue-cli@4.1','Fontawsome@5.1.2']
            }
        }
    }

</script>

<style scoped>
#main{font-family: 'sh',sans-serif!important;padding-top: 40px}
.box-card{max-width: 576px;margin: 0 auto}
a{text-decoration: none;color: coral}
.nms-logo{position: fixed;top: 10%;right: 100px;width: 140px;height: auto;border-radius: 20px}
/*移动适配    */
@media (max-width: 1600px) and (min-width:900px){
    #main .nms-logo{position: fixed;top: 10%;right: 100px;width: 140px;height: auto;border-radius: 20px}
}
@media (max-width: 900px) and (min-width:200px){
    #main .nms-logo{position: fixed;top: 5%;right: 20px;width: 70px;height: auto;border-radius: 20px}
}
</style>