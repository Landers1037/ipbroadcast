/*
vue主页路由
*/
<template>
    <div class="index">
        <h1>Network Management Sys</h1>
        <span><img src="../assets/nms.jpg"></span>
        <div style="width: 200px;text-align: center;margin: 0 auto">
            <el-input v-model="input1" placeholder="请输入账户" class="input-user" autocomplete="off"></el-input>
            <el-input placeholder="请输入密码" v-model="input2" show-password required class="input-pass"></el-input>
            <br>
            <el-button type="primary" class="login" @click="login">登录</el-button>
        </div>
    </div>

</template>
<script>
    import { Base64 } from 'js-base64';
    import { mapMutations } from 'vuex';
    import {MessageBox} from 'element-ui'
    export default {
        name: "index",
        data() {
        return {
            input1: '',
            input2: ''
            }
        },
        methods: {
            ...mapMutations(['changeLogin']),
            login() {
                let _this = this;
                //使用加密的密码校验方式
                var after_pass = Base64.encode(this.input2);
                var user = this.input1;
                //判断登录用户
                if (after_pass === '' || user === '') {
                    MessageBox.alert("请输入完整的用户名和密码");
                } else {
                    if (user === 'root') {
                        let user_data = {"user": user, "pass": after_pass};
                        console.log(user_data);
                        _this.$axios
                            .post('/api/root_login', user_data)
                            .then(res => {
                                console.log(res);
                                var userToken = res.data.token;
                                if(userToken){
                                    sessionStorage.setItem('accessToken', res.data.token);
                                    _this.changeLogin({Authorization: userToken});
                                    _this.$router.push({path: '/dashboard'});
                                }else {
                                    MessageBox.alert("用户名或密码错误！");
                                }
                            }).catch(error => {
                            _this.$message.error('登录失败，后端离线');
                            console.log(error);
                        });

                    } else {
                        let user_data = {"user": user, "pass": after_pass};
                        // console.log(user_data);
                        _this.$axios
                            .post('/api/login', user_data)
                            .then(res => {
                                // console.log(res)
                                var userToken = res.data.token;
                                if(userToken){
                                    sessionStorage.setItem('accessToken', res.data.token);
                                    _this.changeLogin({Authorization: userToken});
                                    _this.$router.push({path: '/dashboard'});
                                }else {
                                    MessageBox.alert("用户名或密码错误！");
                                }
                            }).catch(error => {
                            _this.$message.error('登录失败，后端离线');
                            console.log(error);
                        });
                    }
                }
            },
        }

    }
</script>

<style scoped>
    .index{padding: 40px 10px}
    .index h1{font-family: 'sh',sans-serif;font-size: 2.5em}
    .index span{display: block;}
    .index span img{width: 250px;height: auto;border-radius: 20px}
    .index input{padding: 6px 0 6px 0;margin-top: 10px}
    .index .input-user,.input-pass{margin-top: 10px}
    .index .login{margin-top: 20px;padding-left: 20px;padding-right: 20px}
</style>