<template>
    <div class="userlist">
        <el-input
                placeholder="请输入ID"
                v-model="search_id"
                clearable
                prefix-icon="el-icon-search"
                class="search">
        </el-input><span style="padding: 4px"> </span>
        <el-button type="primary" icon="el-icon-search" @click="search"></el-button>
        <p class="gap" style="margin-bottom: 20px"></p>

        <el-table
                :data="userList"
                border
                height="550"
                @row-dblclick="open_user_more"
                style="width: 100%">
            <el-table-column
                    label="ID"
                    min-width="50">
                <template slot-scope="scope">
                    <span>{{ scope.row.id }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="用户名"
                    min-width="90">
                <template slot-scope="scope">
                    <span>{{ scope.row.name }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="用户权限"
                    min-width="40">
                <template slot-scope="scope">
                    <span>{{ scope.row.ml }}</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="任务级别"
                    min-width="40">
                <template slot-scope="scope">
                    <span>{{ scope.row.tl }}</span>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button
                            size="mini"
                            type="primary"
                            @click="open_user_more(scope.row)">
                        查看
                    </el-button>
                    <el-button
                            size="mini"
                            type="danger"
                            @click="del_user(scope.$index, scope.row)">
                        删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
<!--        更新框-->
        <el-dialog
                title="更新用户"
                :visible.sync="moreVisible"
                class="update-dialog">
            <div class="update-body">
                <el-row :gutter="5" style="align-self: flex-start;width: 50%">
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="用户名称" v-model="user_more.name">
                            <template slot="prepend">用户名称</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="用户名称" v-model="user_more.m">
                            <template slot="prepend">用户全称</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="密码" type="password" show-password v-model="user_more.pw">
                            <template slot="prepend">密码</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="密码" type="password" show-password v-model="user_more.pw2">
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
                        <el-select v-model="user_more.tl" placeholder="请选择" id="task-select">
                            <el-option label="低" value="1" default-first-option ></el-option>
                            <el-option label="中" value="2"></el-option>
                            <el-option label="高" value="3"></el-option>
                        </el-select>
                    </el-col>
                </el-row>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="update_user">更 新</el-button>
            </span>
        </el-dialog>
<!--        搜索结果-->
        <el-dialog
                title="用户信息"
                :visible.sync="userVisible"
                class="update-dialog">
            <div class="update-body">
                <el-row :gutter="5" style="align-self: flex-start;width: 50%">
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="用户名称" v-model="user.name">
                            <template slot="prepend">用户名称</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="用户名称" v-model="user.m">
                            <template slot="prepend">用户全称</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="密码" type="password" show-password v-model="user.pw">
                            <template slot="prepend">密码</template>
                        </el-input>
                    </el-col>
                    <el-col :span="12" :xs="24">
                        <el-input placeholder="密码" type="password" show-password v-model="user.pw2">
                            <template slot="prepend">重复密码</template>
                        </el-input>
                    </el-col>
                </el-row>

                <el-row :gutter="5" style="align-self: flex-start;width: 50%">
                    <el-col :span="24">
                        <el-badge>权限分配</el-badge>
                        <el-checkbox-group v-model="searchcheckList">
                            <el-checkbox label="t">任务管理</el-checkbox>
                            <el-checkbox label="u">用户管理</el-checkbox>
                            <el-checkbox label="m">终端管理</el-checkbox>
                        </el-checkbox-group>
                        <el-checkbox :indeterminate="searchisIndeterminate" v-model="searchcheckAll" @change="handleCheckAllChange_serach">超级用户</el-checkbox>
                    </el-col>
                    <el-col>
                        <span style="margin-right: 6px">任务级别</span>
                        <el-select v-model="user.tl" placeholder="请选择" id="task-select">
                            <el-option label="低" value="1" default-first-option ></el-option>
                            <el-option label="中" value="2"></el-option>
                            <el-option label="高" value="3"></el-option>
                        </el-select>
                    </el-col>
                </el-row>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button type="danger" @click="del_user_search">删 除</el-button>
                <el-button type="primary" @click="update_user_search">更 新</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import {MessageBox} from 'element-ui';
    export default {
        name: "user_list",
        data(){
            return{
                search_id: '',
                user: {}, //搜索得到的用户信息
                userVisible: false, //搜索是否可见
                searchcheckList: [], //搜索的权限复选
                searchisIndeterminate: true, //搜索的全选状态
                searchcheckAll: false, //搜索的全选

                userList: [], //用户列表
                user_more: {}, //选择的用户的信息
                moreVisible: false, //选择用户是否可见
                isIndeterminate: true, //全选状态
                checkAll: false, //权限全选
                checkList: [], //权限复选
            }
        },
        mounted(){
            this.get_user_list();
        },
        methods: {
            get_user_list(){
                let _this = this;
                _this.$axios.post('/api/get_user_list').then(res=>{
                    _this.userList = res.data;
                }).catch(()=>{
                    MessageBox.alert("丢失与服务器连接");
                });
            },
            search(){
                let _this = this;
                let id = _this.search_id;
                _this.user = {};
                if(id.length>0){
                    _this.$axios.post('/api/get_user',{"id": id}).then(res=>{
                        if(res.data!=='bad'){
                            _this.userVisible = true;
                            _this.user = res.data;
                            _this.searchcheckList = _this.user.ml.split("");
                        }else {
                            _this.$message('找不到此用户');
                        }
                    })
                }else{_this.$message.error('请输入要搜索的ID');}

            },
            open_user_more(row){
                let id = row.id;
                let _this = this;
                _this.moreVisible = true;
                _this.user_more = {};
                _this.$axios.post('/api/get_user',{"id":id}).then(res=>{
                    _this.user_more = res.data;
                    _this.checkList = _this.user_more.ml.split("");
                })
            },
            //更新用户 搜索
            update_user_search(){
                let _this = this;
                let update_json = _this.user;
                update_json.m = _this.user.m?_this.user.m:"";
                update_json.ml = _this.searchcheckList.join("");
                this.$axios.post('/api/update_user',update_json).then(res =>{
                    if(res.data === 'ok'){
                        _this.$message({type: 'success',message: '用户更新成功'});
                    }else if(res.data === 'repeat'){
                        _this.$message.error('用户名重复，请重试')
                    } else {_this.$message.error('用户更新失败')}
                }).catch(err=>{
                    MessageBox.alert("丢失与服务器连接");
                });
            },
            //更新用户 列表
            update_user(){
                let _this =this;
                let update_json = _this.user_more;
                update_json.m = _this.user_more.m?_this.user_more.m:"";
                update_json.ml = _this.checkList.join("");
                this.$axios.post('/api/update_user',update_json).then(res =>{
                    if(res.data === 'ok'){
                        _this.$message({type: 'success',message: '用户更新成功'});
                    }else if(res.data === 'repeat'){
                        _this.$message.error('用户名重复，请重试')
                    } else {_this.$message.error('用户更新失败')}
                }).catch(err=>{
                    MessageBox.alert("丢失与服务器连接");
                });
            },
            //删除用户 搜索
            del_user_search(){
                let _this = this;
                let del_id = _this.user.id;
                this.$axios.post('/api/delete_user',{"id": del_id}).then(res =>{
                    if(res.data==='ok'){
                        _this.$message({type: 'success',message: '用户删除成功请刷新'});
                        _this.userVisible = false;
                        _this.get_user_list();
                    }else{
                        _this.$message.error('用户删除失败,当前登录的用户无法删除');
                        _this.userVisible = false;
                    }
                }).catch(err=>{
                    MessageBox.alert("丢失与服务器连接");
                    _this.userVisible = false;
                });
            },
            //删除用户 列表里
            del_user(index,row){
                let _this = this;
                let del_id = row.id;
                this.$axios.post('/api/delete_user',{"id": del_id}).then(res =>{
                    if(res.data==='ok'){
                        _this.$message({type: 'success',message: '用户删除成功请刷新'});
                        //删除完成后刷新列表
                        _this.get_user_list();
                    }else{
                        _this.$message.error('用户删除失败');
                    }
                }).catch(err=>{
                    MessageBox.alert("丢失与服务器连接");
                });
            },
            //处理终端多选操作
            handleSelectionChange(val) {
                this.mediaSelect= val;
                console.log(val);
            },
            //处理普通权限多选
            handleCheckAllChange(val){
                this.checkList = val?["u","t","m"]:[];
                this.isIndeterminate = false;
            },
            //处理搜索的权限多选
            handleCheckAllChange_serach(val){
                this.searchcheckList= val?["u","t","m"]:[];
                this.isIndeterminate = false;
            },
        }
    }
</script>

<style scoped>
    .userlist{text-align: left;padding: 30px 30px;}
    .gap{padding: 4px;display: block}
    .search{max-width: 400px}
    /*更新框的样式*/
    .userlist /deep/ .update-dialog .el-dialog{width: 98%;max-width: 800px}
    .userlist /deep/ .update-body .el-input-group__append, .userlist /deep/ .update-dialog .el-input-group__prepend{
        padding: 0 8px;
    }
    .userlist /deep/ .update-body .el-input{
        margin-bottom: 6px;
    }
    .userlist /deep/ .update-body .el-input__inner{
        padding: 0 6px;
    }
    .userlist /deep/ .update-body .el-input{font-size: 12px}
    .userlist .update-body{
        display: flex;
        display: -webkit-flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    /*任务复选框*/
    .userlist /deep/ .update-body #task-select.el-input__inner{height: 30px;line-height: 30px}
    /*移动适配*/
    @media (max-width: 1600px) and (min-width: 600px){
        .userlist{text-align: left;padding: 20px 30px;}
    }
    @media (max-width: 600px) and (min-width:200px){
        .userlist{text-align: left;padding: 20px 10px;}
        .userlist  /deep/ .el-button{padding: 10px 10px;font-size: 13px}
        .search{max-width: 220px}
    }
</style>