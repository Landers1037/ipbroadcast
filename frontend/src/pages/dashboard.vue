<template>
    <div class="dashboard">
        <div class="tool-bar">
                <el-menu
                        background-color="#409eff"
                        text-color="#ffffff"
                        :collapse="isCollapse"
                        class="left-bar"
                        unique-opened
                        collapse-transition
                >
                    <el-menu-item style="padding: 50px 10px;position: relative;vertical-align: middle;">
                        <img id="avatar" :src="img_num" @click="collapse" :style="avatarclass">
                        <span id="leftbar_name">{{userinfo.name}}</span>
                    </el-menu-item>

                    <el-submenu index="1">
                        <template slot="title">
                            <i class="el-icon-user-solid"></i>
                            <span>用户管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="1-1" @click="change_for_user">当前用户</el-menu-item>
                            <el-menu-item index="1-2" @click="change_for_userlist">用户列表</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>

                    <el-submenu index="2">
                        <template slot="title">
                            <i class="el-icon-s-platform"></i>
                            <span>终端管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="2-1" @click="change_for_media">终端列表</el-menu-item>
<!--                            <el-menu-item index="2-2">添加终端</el-menu-item>-->
                        </el-menu-item-group>
                    </el-submenu>

                    <el-submenu index="3">
                        <template slot="title">
                            <i class="el-icon-message-solid"></i>
                            <span>任务管理</span>
                        </template>
                        <el-menu-item-group>
                            <el-menu-item index="3-1" @click="change_for_task">任务列表</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-menu-item index="4" @click="go_log">
                            <i class="el-icon-s-management"></i>
                            <span slot="title">运行日志</span>
                    </el-menu-item>
                    <el-menu-item index="5" @click="go_echarts">
                            <i class="el-icon-s-data"></i>
                            <span slot="title">后台监控</span>
                    </el-menu-item>
                    <el-menu-item index="5" @click="go_console">
                        <i class="el-icon-s-platform"></i>
                        <span slot="title">后端测试</span>
                    </el-menu-item>
                    <el-menu-item index="5" @click="go_doc">
                        <i class="el-icon-document"></i>
                        <span slot="title">查看文档</span>
                    </el-menu-item>
                    <el-menu-item index="5" @click="go_about">
                        <i class="el-icon-umbrella"></i>
                        <span slot="title">关于项目</span>
                    </el-menu-item>
                    <el-menu-item index="6" @click="change_user_show">
                        <i class="el-icon-s-custom"></i>
                        <span slot="title">切换用户</span>
                    </el-menu-item>
                    <el-menu-item index="7" @click="logout">
                        <i class="el-icon-remove"></i>
                        <span slot="title">退出登录</span>
                    </el-menu-item>
                </el-menu>

            <div class="area">
                <component :is="what"></component>
            </div>
        </div>

        <el-dialog
                title="切换用户"
                :visible.sync="showUserchange"
                class="dialog"
        >
            <el-input v-model="input_user" placeholder="账号" id="input_user"></el-input>
            <el-input placeholder="请输入密码" v-model="input_pass" show-password id="input_pass"></el-input>
            <span slot="footer" class="dialog-footer">
                <el-button type="warning" @click="showUserchange = false">关闭</el-button>
                <el-button type="primary" @click="change_user">登录</el-button>
              </span>
        </el-dialog>
</div>
</template>


<script>
    import { Base64 } from 'js-base64';
    import { mapMutations } from 'vuex';
    import {MessageBox} from 'element-ui'

    import user_panel from "./panel/user_panel";
    import task_panel from "./panel/task_panel";
    import media_panel from "./panel/media_panel";
    import user_list from "./panel/user_list";

    var r_num = Math.floor(Math.random()*6) + 1;
    export default {
        name: "dashboard",
        components: {user_panel,task_panel,media_panel,user_list},
        data() {
            return {
                activeIndex: '1',
                isCollapse: false, //折叠
                flag: this.ismobile(), //是否为移动设备
                ipStatus: null,
                avatarclass: {
                    width: "50px",
                    height: "50px",
                    left: "10px"
                },
                hide: {
                    opacity: 1
                },
                userinfo: {},
                img_num: require("../assets/avatar/1.jpg"),
                what: "user_panel",
                showUserchange : false,
                //切换用户
                input_user : '',
                input_pass: '',
                timer: null //定时器
            };
        },
        created(){
            let flag = this.flag;
            if (flag){
                this.isCollapse = true;
            }else {
                this.isCollapse = false;
            }
        },
        mounted() {
            let _this = this;
            console.log(localStorage.getItem('Authorization'));
            _this.loadicon(); //随机头像
            _this.$axios
                .post('/api/get_user_info')
                .then(res => {
                    if(res.data === 'bad'){
                        _this.$message.error('无法获取用户信息')
                    }else {
                        _this.userinfo = res.data; //当前登录用户信息
                    }
                });
            //定时检查后端是否在线
            _this.check_ipstatus();
        },
        beforeDestroy(){
          //在组件周期结束时清空计时器
          if(this.timer){
              clearInterval(this.timer);
          }
        },
        watch: {
            img_num: function () {},
            flag: function(){
                let flag = this.flag;
                this.isCollapse = !!flag;
            },
            isCollapse: function () {
                if(this.isCollapse && !this.flag){
                    //折叠后的样式
                    // document.querySelector(".sidebar").style.width = 64 + "px";
                    document.querySelector(".area").style.marginLeft = 64 + "px";
                    document.getElementById("leftbar_name").style.display = "none";

                }else if(!this.isCollapse && !this.flag){
                    // document.querySelector(".sidebar").style.width = 210 + "px";
                    document.querySelector(".area").style.marginLeft = 210 + "px";
                    document.getElementById("leftbar_name").style.display = "inline-block";
                }else if(this.isCollapse && this.flag){
                    // document.querySelector(".sidebar").style.width = 64 + "px";
                    document.querySelector(".area").style.marginLeft = 64 + "px";
                    document.getElementById("leftbar_name").style.display = "none";
                }
                else if(!this.isCollapse && this.flag){
                    // document.querySelector(".sidebar").style.width = 210 + "px";
                    document.querySelector(".area").style.marginLeft = 64 + "px";
                    document.getElementById("leftbar_name").style.display = "inline-block";
                }
            },
            ipStatus: function () {
                if(!this.ipStatus){
                    this.$message.error('身份认证过期，请重新登录');
                    setTimeout(()=>{
                        this.logout();
                    },1500);
                }
            }
        },
        methods: {
            ...mapMutations(['changeLogin']),
            logout(){
                console.log(localStorage.getItem('Authorization'));
                localStorage.removeItem('Authorization');
                console.log(localStorage.getItem('Authorization'));
                this.$router.push('/'); //返回登录页面
            },
            //路由跳转
            go_about(){
                this.$router.push('/about')
            },
            //后台
            go_console(){
                this.$router.push('/console')
            },
            //文档
            go_doc(){
                this.$router.push('/doc')
            },
            //查看日志
            go_log(){
                this.$router.push('/dashboard/log');
            },
            //图表
            go_echarts(){
                this.$router.push('/echarts');
            },
            //用户切换
            change_user_show(){
                //切换用户
                this.input_user = "";
                this.input_pass = "";
                this.showUserchange = true;
            },
            change_user(){
                let _this = this;
                if(_this.user!=="" && _this.input_pass!==""){
                    var after_pass = Base64.encode(_this.input_pass);
                    var user = _this.input_user;
                    _this.showUserchange = false;
                    let user_data = {"user": user, "pass": after_pass};
                    _this.$axios
                        .post('/api/login', user_data)
                        .then(res => {
                            var userToken = res.data.token;
                            if(userToken){
                                sessionStorage.setItem('accessToken', res.data.token);
                                _this.changeLogin({Authorization: userToken});
                                _this.showUserchange = false;
                                setTimeout(()=>{
                                    _this.$router.push({name: 'middle',params: {url: "/dashboard"}});
                                },500);
                            }else {
                                MessageBox.alert("用户名或密码错误！");
                            }
                        }).catch(error => {
                        _this.$message.error('后端离线');
                    });
                }else {
                    _this.$message.error('请输入用户名和密码');
                }

            },
            //用户的权限判断
            checkUser(part,userdata){
                switch (part) {
                    case 'user':
                        if(userdata.indexOf('u')!==-1){
                            return true;
                        }else {
                            this.$message.error('您没有权限进行此操作');
                            return false;
                        }
                    case 'task':
                        if(userdata.indexOf('t')!==-1){
                            return true;
                        }else {
                            this.$message.error('您没有权限进行此操作');
                            return false;
                        }
                    case 'media':
                        if(userdata.indexOf('m')!==-1){
                            return true;
                        }else {
                            this.$message.error('您没有权限进行此操作');
                            return false;
                        }
                }
            },
            //动态组件
            change_for_user(){this.what = "user_panel"},
            change_for_task(){if(this.checkUser('task',this.userinfo.ml)) this.what = "task_panel"},
            change_for_media(){if(this.checkUser('media',this.userinfo.ml)) this.what = "media_panel"},
            change_for_userlist(){if(this.checkUser('user',this.userinfo.ml)) this.what = "user_list"},
            //移动适配
            ismobile(){
                    let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
                    return flag;
            },
            collapse(){
                let now = this.isCollapse;
                this.isCollapse  = !now;
            },
            //动态加载头像
            loadicon() {
                let _this = this;
                if (r_num){
                    switch (r_num) {
                        case 1: _this.img_num = require("../assets/avatar/1.jpg");break;
                        case 2: _this.img_num = require("../assets/avatar/2.jpg");break;
                        case 3: _this.img_num = require("../assets/avatar/3.jpg");break;
                        case 4: _this.img_num = require("../assets/avatar/4.jpg");break;
                        case 5: _this.img_num = require("../assets/avatar/5.jpg");break;
                        case 6: _this.img_num = require("../assets/avatar/7.jpg");break;
                    }
                }
            },
            //心跳包
            check_ipstatus(){
                let _this = this;
                // 定时包的发送不需要动画加载
                _this.timer = setInterval(()=>{
                    _this.$axios.post('/api/keepalive',{},{isLoading: false}).then(res=>{
                        _this.ipStatus = !!res.data.status;
                        if(!res.data.status){
                            clearInterval(_this.timer)
                        }
                    }).catch(()=>{
                        _this.ipStatus = false;
                        clearInterval(_this.timer);
                    });
                },60000);
            }
        },
    }
</script>

<style scoped>
    *:hover{outline: none}
    .dashboard{padding: 0;height: 100%}

    .tool-bar{height: 100%;position: relative;width: 100%}
    .tool-bar .left-bar .el-menu{border-right: none}
    #avatar{border-radius:50%;cursor: pointer;outline: none;position: absolute;left: 20px;top: 50%;transform: translateY(-50%)}
    #avatar{
        transition: all 0.4s ease;
    }
    #leftbar_name{vertical-align: middle;margin-left: 70px;position: absolute;top: 50%;transform: translateY(-50%);font-size: 25px;font-weight: bold}
    #avatar:focus{outline: none}
    .left-bar{position: absolute;height: 100%;top: 0;left: 0;z-index: 999;text-align: left}
    .left-bar:not(.el-menu--collapse){width: 210px;height: 100%;position: absolute;top: 0;left: 0;z-index: 999}

    /deep/ .el-menu-item i{color: #fff}
    /deep/ .el-submenu__title i{color: #fff}
    .left-bar /deep/ .el-menu-item{color: white}
    .left-bar /deep/ .el-menu-item.is-active{color: #f5f5f5}
    .left-bar /deep/ .el-submenu__title{color: white}
    .left-bar /deep/ .el-menu-item-group__title{padding: 0;}
    .left-bar /deep/ .el-menu-item-group ul li{background-color: #426ab3!important;}
    /*change user*/
    .dialog /deep/ .el-input{width: 80%}
    /deep/ #input_user{margin-bottom: 10px}
    /deep/ #input_pass{margin: 0 auto}
    /*右侧的操作页面*/
    .area{background-color: #ffffff;height: inherit;margin-left: 210px;}
    #current_user{float: right;
        padding: 0 15px 0 15px;vertical-align: middle;line-height: 2;width:100px;background-color: #fafafa;color: #2c3e50;top:50%;transform: translateY(-50%);position: absolute;right: 0;}
    /*移动适配*/
    /deep/ .el-menu-item{color: #fff}
    /deep/ .el-menu-item-group__title{padding: 0}
    /*对话框属性分组件设计*/
    /*!*@media (max-width: 1600px) and (min-width:1000px){*!*/
    /*!*    .dashboard /deep/ .el-dialog{width: 60%}*!*/
    /*!*}*!*/
    /*@media (max-width: 1000px) and (min-width:600px){*/
    /*    .dashboard /deep/ .el-dialog{width: 75%}*/
    /*}*/
    /*@media (max-width: 600px) and (min-width:200px){*/
    /*    .dashboard /deep/ .el-dialog{width: 98%}*/
    /*}*/
</style>