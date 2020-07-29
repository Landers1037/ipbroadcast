<template>
    <div class="userpanel">
        <p><i class="el-icon-user" style="margin-bottom: 10px">用户信息</i></p>
        <el-input placeholder="用户ID" v-model="user.id" class="user_id" :disabled="true">
            <template slot="prepend">用户ID</template>
        </el-input>
        <span class="gap"></span>
        <el-input placeholder="用户名称" v-model="user.name" class="user_name">
            <template slot="prepend">用户名称</template>
        </el-input>
        <span class="gap"></span>
        <el-input placeholder="用户全称" v-model="user.m" class="user_name">
            <template slot="prepend">用户全称</template>
        </el-input>
        <span class="gap"></span>
        <el-input placeholder="用户密码" v-model="user.pw" class="user_pw">
            <template slot="prepend">用户密码</template>
        </el-input>
        <span class="gap" style="margin-top: 20px"></span>
        <p style="margin-bottom: 10px">用户权限: </p>
        <el-checkbox-group v-model="userAuth">
            <el-checkbox label="t">任务管理</el-checkbox>
            <el-checkbox label="u">用户管理</el-checkbox>
            <el-checkbox label="m">终端管理</el-checkbox>
        </el-checkbox-group>
        <span class="gap"></span>
        <p style="margin-bottom: 10px">任务级别: </p>
        <el-select v-model="user.tl" placeholder="请选择">
            <el-option label="低" value="1" default-first-option></el-option>
            <el-option label="中" value="2"></el-option>
            <el-option label="高" value="3"></el-option>
        </el-select>

        <p style="padding: 40px"></p>
        <el-row class="userpanel-bt">
            <el-button type="primary" @click="update_user">更新用户</el-button>
            <el-button type="info" @click="before_add_user">添加用户</el-button>
            <el-button type="danger" @click="before_del_user">删除用户</el-button>
        </el-row>
<!--        删除用户的模态框-->
        <el-dialog
                title="确认删除吗？"
                :visible.sync="delVisible"
                class="del-dialog">
            <span>你接下来的操作将会删除该用户</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="delVisible = false">取 消</el-button>
                <el-button type="primary" @click="del_user">确 定</el-button>
            </span>
        </el-dialog>
<!--        添加用户的模态框-->
        <el-dialog
                title="添加用户"
                :visible.sync="addVisible"
                class="add-dialog">
            <div class="add-body">
                <el-row :gutter="5" style="align-self: flex-start;width: 50%">
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="用户名称" v-model="newuser.name">
                            <template slot="prepend">用户名称</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="用户名称" v-model="newuser.m">
                            <template slot="prepend">用户全称</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="密码" type="password" show-password v-model="newuser.pw">
                            <template slot="prepend">密码</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="密码" type="password" show-password v-model="newuser.pw2">
                            <template slot="prepend">重复密码</template>
                        </el-input>
                    </el-col>
                </el-row>

                <el-row :gutter="5" style="align-self: flex-start;width: 50%">
                    <el-col :span="24">
                        <el-badge>权限分配</el-badge>
                        <el-checkbox-group v-model="checkList">
                            <el-checkbox label="t">任务管理</el-checkbox>
                            <el-checkbox label="u">用户管理</el-checkbox>
                            <el-checkbox label="m">终端管理</el-checkbox>
                        </el-checkbox-group>
                        <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">超级用户</el-checkbox>
                    </el-col>
                    <el-col>
                        <span style="margin-right: 6px">任务级别</span>
                        <el-select v-model="newuser.tl" placeholder="请选择" id="task-select">
                            <el-option label="低" value="1" default-first-option></el-option>
                            <el-option label="中" value="2"></el-option>
                            <el-option label="高" value="3"></el-option>
                        </el-select>
                    </el-col>
                </el-row>
            </div>
            <div style="display: flex">
                <el-row style="width: 100%">
                    <el-col :span="24">
                        <el-badge>终端控制</el-badge>
                        <el-table
                                :data="medialist"
                                border
                                height="250"
                                @selection-change="handleSelectionChange"
                                style="width: 100%">
                            <el-table-column
                                    prop="id"
                                    type="selection"
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
                                    prop="ip"
                                    label="地址">
                            </el-table-column>
                        </el-table>
                    </el-col>
                </el-row>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="add_user">添 加</el-button>
            </span>
        </el-dialog>

    </div>
</template>

<script>
    import {MessageBox} from 'element-ui';

    export default {
        name: "user_panel",
        data(){
            return{
                delVisible: false,
                addVisible: false,
                user: {"id": 0,"name": "","pw":"","m":"","ml":"","tl":""}, //当前用户
                userAuth: [], //当前用户权限
                newuser: {"name": "","pw":"","pw2":"","ml":"","tl":"1"}, //新用户
                isIndeterminate: true, //全选状态
                checkAll: false, //新权限全选
                checkList: [], //新权限复选
                medialist: [], //终端列表
                mediaSelect: [], //新用户被选择的终端设备
            }
        },
        watch: {
            user: function () {},
        },
        mounted() {
            let _this = this;
            _this.$axios.post('/api/get_user_info').then(res=>{
                _this.user = res.data;
                _this.userAuth =  _this.user.ml.split(""); //计算用户权限
            });
            _this.$axios.post("/api/get_terminal_list").then(res=>{
                _this.medialist = res.data;
            }).catch(()=>{
                _this.$message.error('丢失与服务器连接');
            });
        },
        methods: {
            //更新用户信息
            update_user(){
                let _this = this;
                let update_json = _this.user;
                update_json.m = _this.user.m?_this.user.m:"";
                update_json.ml = _this.userAuth.join("");
                if(update_json.name === 'root'){
                    _this.$message.error('root内置用户不能修改')
                } else if(update_json.name && update_json.pw){
                    _this.$axios.post('/api/update_user',update_json).then(res =>{
                        if(res.data === 'ok'){
                            _this.$message({type: 'success',message: '用户更新成功'});
                        }else if(res.data === 'repeat'){
                            _this.$message.error('用户名重复，请重试')
                        } else {_this.$message.error('用户更新失败')}
                    }).catch(()=>{
                        MessageBox.alert("丢失与后端服务器连接");
                    });
                }else{
                    _this.$message.error('请输入用户名和密码')
                }
            },
            //权限判断
            before_del_user(){
                let _this = this;
                if(_this.checkUser('user',_this.user.ml)){
                    _this.delVisible = true;
                }
            },
            //删除用户信息，特殊在个人信息页面可以删除自己
            del_user(){
                let del_id = this.user.id;
                let that = this;
                that.$axios.post('/api/delete_myself',{"id": del_id}).then(res =>{
                    if(res.data === 'ok'){
                        setTimeout(()=>{
                            that.delVisible = false;
                            that.$message({type: 'success',message: '删除成功，即将返回主页'})
                        },500);
                        //注意如果是非root用户删除完成后应该token失效 重新登录
                        that.redirect_user();
                    }else {
                        that.delVisible = false;
                        setTimeout(()=>{
                            that.$message.error('删除失败，注意root用户不能删除');
                        },500);
                    }
                }).catch(err=>{
                    console.log(err);
                    MessageBox.alert("丢失与后端服务器连接");
                });
            },
            //用户失效后返回主页
            redirect_user(){
                localStorage.removeItem('Authorization');
                console.log(localStorage.getItem('Authorization'));
                setTimeout(()=>{
                    this.$router.push('/'); //返回登录页面
                },1000);
            },
            before_add_user(){
                //权限判断，清空输入
                let _this = this;
                _this.newuser = {};
                if(_this.checkUser('user',_this.user.ml)){
                    _this.addVisible = true;
                }
            },
            //添加用户信息
            add_user(){
                let _this = this;
                let new_json = _this.newuser;
                new_json.m = _this.newuser.m?_this.newuser.m:"";
                new_json.ml = _this.checkList.join("");
                new_json.tl = _this.newuser.tl?_this.newuser.tl:"1";
                if(_this.newuser.name && _this.newuser.pw && _this.newuser.pw === _this.newuser.pw2){
                    _this.$axios.post('/api/add_user',new_json).then(res =>{
                        //用户有三种响应 成功 失败 用户重复
                        if(res.data === 'ok'){
                            _this.$message({type: 'success',message: '用户添加成功'});
                            _this.addVisible = false;
                        }else if(res.data === 'repeat'){
                            _this.$message.error('用户名重复，请重试');
                        }else {_this.$message.error('用户添加失败')}
                    }).catch(()=>{
                        MessageBox.alert("丢失与后端服务器连接");
                        _this.addVisible = false;
                    });
                }else {
                    _this.$message.error('用户名和密码不能为空')
                }
            },
            //处理添加用户终端多选操作
            //实际用户并不会被分配终端设备
            handleSelectionChange(val) {
                this.mediaSelect= val;
                console.log(val);
            },
            //处理添加用户权限全选
            handleCheckAllChange(val){
                this.checkList = val?["u","t","m"]:[];
                this.isIndeterminate = false;
            },
            //用户权限校验
            //用户管理u 任务管理t 终端管理m
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
            }
        }
    }
</script>

<style scoped>
.userpanel{text-align: left;padding: 20px 30px;}
/*默认间隔*/
.gap{padding: 5px 4px;display: block}
.user_id,.user_name,.user_pw{max-width: 460px}
.userpanel-bt /deep/ .el-button{margin-bottom: 10px}
/*用户框内部按钮和输入框样式*/
.userpanel /deep/ .add-dialog .el-dialog{width: 98%;max-width: 800px}
.userpanel /deep/ .add-body .el-input-group__append, .userpanel /deep/ .add-dialog .el-input-group__prepend{
    padding: 0 8px;
}
.userpanel /deep/ .add-body .el-input{
    margin-bottom: 6px;
}
.userpanel /deep/ .add-body .el-input__inner{
    padding: 0 6px;
}
.userpanel /deep/ .add-body .el-input{font-size: 12px}
.userpanel .add-body{
    display: flex;
    display: -webkit-flex;
    justify-content: space-between;
    align-items: flex-start;
}
/*任务复选框*/
.userpanel /deep/ .add-body #task-select.el-input__inner{height: 30px;line-height: 30px}
/*移动适配*/
@media (max-width: 1600px) and (min-width: 600px){
    .userpanel{text-align: left;padding: 20px 30px;}
    .userpanel /deep/ .el-dialog{max-width: 70%;}
}
@media (max-width: 600px) and (min-width:200px){
    .userpanel{text-align: left;padding: 20px 10px;}
    .userpanel /deep/ .el-dialog{width: 98%;}
    .userpanel .userpanel-bt /deep/ .el-button{padding: 10px 10px;font-size: 13px}
}
</style>