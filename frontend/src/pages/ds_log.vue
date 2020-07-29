<template>
    <div class="log">
        <el-button @click="back" type="primary">返回面板</el-button>
        <el-button @click="del" type="danger">清空日志</el-button>
        <el-button @click="backup" type="success">备份日志</el-button>
        <div v-html="log" class="log_panel"></div>
    </div>
</template>

<script>
    import {MessageBox} from 'element-ui';
    export default {
        name: "ds_log",
        data(){
            return {
                log: 'this is server log'
            }
        },
        watch: {
            log: function () {
                // console.log(this.log);
            }
        },
        created() {
            this.$axios
            .post('/api/sys_log')
                .then(res => {
                    // console.log(res.data);
                    this.log = res.data;
                }).catch(err=>{
                MessageBox.alert("丢失与服务器连接");
            });
        },
        methods: {
            back(){
                this.$router.push('/dashboard');
            },
            del(){
                this.$axios
                    .post('/api/sys_log_del')
                    .then(res =>{
                        this.log = res.data;
                    }).catch(err=>{
                    MessageBox.alert("丢失与服务器连接");
                });
            },
            backup(){
                this.$axios.post('/api/sys_log_backup')
                    .then(res=>{
                        if(res.data==='bad'){
                            this.$message.error('日志备份失败')
                        }else {
                            this.$message({type: 'success',message: '日志备份成功'})
                        }
                    })
            }
        }
    }
</script>

<style scoped>
.log{padding: 20px}
.log_panel{margin: 0 auto;padding: 20px;background-color: #f5f5f5;max-width: 980px;border-radius: 10px;margin-top: 30px;text-align: left;font-size: 0.8em}
.log_panel{max-height: 600px;overflow-y: auto}
</style>