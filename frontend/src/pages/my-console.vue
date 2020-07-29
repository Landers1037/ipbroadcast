<template>
    <div  ref="console_vue" id="console">
        <el-button  style="margin-top:10px;margin-bottom: 10px" @click="get_detail">调试信息</el-button>
        <div id="info-panel">
            <el-input placeholder="后台api接口" v-model="detail[0].api">
                <template slot="prepend">http://</template>
            </el-input>
            <br>
            <p style="padding: 2px 0 2px 0">内存占用：</p><el-progress :text-inside="true" :stroke-width="26" :percentage="detail[1].detail_mem"></el-progress>
            <br>
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>当前用户信息</span>
                    <el-button style="float: right; padding: 3px 0" type="text"><i class="el-icon-user"></i></el-button>
                </div>
                <div v-for="(detail_u,n) in detail[2].detail_user" :key="n" class="text item">
                    {{detail_u}}
                </div>
            </el-card>
            <br>
            <el-card class="box-card">
            <div class="clearfix">
                <span>后台服务器信息</span>
            </div>
            <div v-for="(s,n) in detail[3].detail_sys"  :key="n" class="text item">
                {{ s }}
            </div>
            </el-card>
            <br>
            <el-card class="box-card">
                <div class="clearfix">
                    <span>版权信息</span>
                </div>
                <div v-for="(d,n) in detail[4].copy" :key="n" class="text item">
                    {{ d }}
                </div>
            </el-card>
            <br>
        </div>
    </div>
</template>

<script>
    import {MessageBox} from 'element-ui';
    export default {
        name: "myconsole",
        data() {
            return{
                detail: [
                    {api: '后端api地址'},
                    {detail_mem: 0},
                    {detail_user: ['u1', 'u2']},
                    {detail_sys: ['s1', 's2', 's3','s4']},
                    {copy: ['','','','','']}
                ]
            }
        },
        created() {
            this.$axios.post('/api/sys_detail').then(res => {
                // console.log(res);
                this.$set(this.detail,0,{api: res["data"]["api"]});
                this.$set(this.detail,1,{detail_mem: res["data"]["mem"]});
                this.$set(this.detail,2,{detail_user: res["data"]["userdata"]});
                this.$set(this.detail,3,{detail_sys: res["data"]["sysdata"]});
                this.$set(this.detail,4,{copy: res["data"]["copy"]});
            }).catch(err=>{
                MessageBox.alert("丢失与服务器连接");
            });
        },
        methods: {
            get_detail(){
                this.$axios
                    .post('/api/sys_detail')
                    .then(res => {
                        console.log(res["data"]);
                        this.$set(this.detail,0,{api: res["data"]["api"]});
                        this.$set(this.detail,1,{detail_mem: res["data"]["mem"]});
                        this.$set(this.detail,2,{detail_user: res["data"]["userdata"]});
                        this.$set(this.detail,3,{detail_sys: res["data"]["sysdata"]});
                        this.$set(this.detail,4,{copy: res["data"]["copy"]});
                    }).catch(err=>{
                    MessageBox.alert("丢失与服务器连接");
                });
            }
        }
    }
</script>

<style scoped>
#info-panel{margin: 0 auto;max-width: 576px;padding-top: 20px}
    .text{text-align: left}
</style>