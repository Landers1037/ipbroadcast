<template>
    <div class="mediapanel">
        <p><i class="el-icon-s-platform" style="margin-bottom: 10px">终端信息</i></p>
        <el-table
                :data="medialist"
                border
                height="550"
                @row-dblclick="open_media"
                style="width: 100%">
            <el-table-column
                    prop="id"
                    label="编号"
                    min-width="50">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="名称"
                    min-width="50">
            </el-table-column>
            <el-table-column
                    label="状态"
                    min-width="60">
                <template slot-scope="scope">
                    <p v-if="scope.row.status===0">断线</p>
                    <p v-else-if="scope.row.status===1">在线</p>
                </template>
            </el-table-column>
            <el-table-column
                    align="center"
                    prop="volume"
                    label="音量"
                    min-width="60">
            </el-table-column>
            <el-table-column
                    align="center"
                    label="功放"
                    min-width="60">
                <template slot-scope="scope">
                    <p v-if="scope.row.power===0">关</p>
                    <p v-else-if="scope.row.power===1">开</p>
                </template>
            </el-table-column>
            <el-table-column
                    prop="ip"
                    label="地址">
            </el-table-column>
        </el-table>
        <el-row style="margin-top: 20px">
            <el-button @click="update_media_list" type="primary">更新终端列表</el-button>
        </el-row>
        <el-dialog
                title="更新终端"
                :visible.sync="show"
                class="update-media">
            <p style="padding: 10px 5px">要更新的终端ID: <span style="font-weight: bold;color: red">{{media_id}}</span></p>
            <el-input placeholder="请输入内容" v-model="media_name">
                <template slot="prepend">终端名称</template>
            </el-input>
            <div style="width: 100%" >
                <span style="width: 40px;display: inline-block;height: 40px;line-height: 40px">音量</span><el-slider style="display: inline-block;width: calc(100% - 40px);vertical-align: middle" v-model="media_volume"></el-slider>
            </div>
            <div>
                <span style="padding-right: 6px">功放开关</span>
                <el-switch
                        v-model="media_power"
                        active-color="#13ce66"
                        inactive-color="#ff4949">
                </el-switch>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button type="danger" >删除终端</el-button>
                <el-button type="primary" @click="update_media">确定修改</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import axios from 'axios';
    import {MessageBox} from 'element-ui';
    export default {
        name: "media_panel",
        data(){
            return{
                show: false,
                media_name: '', //终端名称
                media_id: '', //终端id
                media_volume: 0, //终端音量
                media_power: false, //终端功放状态
                medialist: [{'id': 108, 'type': 13, 'name': '108', 'status': 0, 'context': '', 'volume': 70, 'defaultVolumn': 70, 'power': 0, 'defaultPower': 0, 'isDefault': 0, 'ip': '192.168.1.108', 'last': 0, 'taskType': 0, 'taskID': 0}]
            }
        },
        mounted() {
            this.get_media_list();
        },
        methods:{
            get_media_list(){
                let _this = this;
                this.$axios.post("/api/get_terminal_list").then(res=>{
                    if(res.data === 'bad'){
                        _this.$message.error('获取终端列表失败')
                    }else {
                        _this.medialist = res.data;
                    }
                }).catch(()=>{
                    _this.$message.error('丢失与服务器连接');
                });
            },
            //更新终端列表信息
            update_media_list(){
                let _this = this;
                this.$axios.post("/api/get_terminal_list",{"update": "yes"}).then(res=>{
                   if(res.data === 'bad'){
                       _this.$message.error('获取终端列表失败')
                   } else{
                       _this.medialist = res.data;
                   }
                }).catch(()=>{
                    _this.$message.error('丢失与服务器连接');
                });
            },
            //显示某个终端信息
            open_media(row){
                let _this = this;
                _this.media_name = row.name;
                _this.media_id = row.id;
                _this.media_power = row.power !== 0;
                _this.show = true;
            },
            //更新终端名称
            update_media(){
                let _this = this;
                //每次执行完毕后name和id都会清空
                let data = {
                    "id": _this.media_id,
                    "name": _this.media_name,
                    "power": _this.media_power?1:0,
                };
                _this.$axios.post('/api/update_terminal',data).then(res=>{
                    if(res.data === 'bad'){
                        _this.show = false;
                        _this.$message.error('更新失败');
                        _this.media_name = '';
                        _this.media_id = '';
                        _this.media_power = false;
                    }else {
                        _this.show = false;
                        _this.$message({type: 'success',message: '更新成功'});
                        _this.get_media_list(); //刷新列表
                        _this.media_name = '';
                        _this.media_id = '';
                        _this.media_power = false;
                    }
                }).catch(()=>{
                    _this.show = false;
                    _this.media_name = '';
                    _this.media_id = '';
                    _this.media_power = false;
                    _this.$message.error('丢失与服务器连接');
                });
            }
        }
    }
</script>

<style scoped>
    .mediapanel{text-align: left;padding: 20px 30px;user-select: none}
    .gap{padding: 4px;display: block}
    .update-media /deep/ .el-dialog {
        width: 60%;
    }
    @media (max-width: 600px) and (min-width:200px){
        .mediapanel{padding: 10px}
        .update-media /deep/ .el-dialog{width: 96%}
    }
</style>