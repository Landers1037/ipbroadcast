<template>
    <div class="taskpanel">
        <p><i class="el-icon-bell" style="margin-bottom: 10px">任务信息</i></p>
        <el-row class="bt-row">
            <el-button type="primary" @click="addVisible = true">添加任务</el-button>
            <el-button type="danger">删除任务</el-button>
        </el-row>
        <p style="padding: 10px"></p>
        <el-table
                :data="tasklist"
                border
                height="550"
                @row-dblclick="get_task"
                style="width: 100%">
            <el-table-column
                    prop="id"
                    label="ID"
                    width="50">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="名称"
                    width="100">
            </el-table-column>
            <el-table-column
                    label="可用"
                    width="60">
                <template slot-scope="scope">
                    <span v-if="scope.row.en === 0" style="color: red">不可用</span>
                    <span v-if="scope.row.en === 1" style="color: green">可用</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="状态"
                    width="100">
                <template slot-scope="scope">
                    <span v-if="scope.row.run === 0" style="color: red">任务未激活</span>
                    <span v-if="scope.row.run === 1" style="color: green">任务已激活</span>
                </template>
            </el-table-column>
            <el-table-column
                    prop="mode"
                    label="播放模式"
                    width="80">
                <template slot-scope="scope">
                    <span v-if="scope.row.exe === 0" style="color: blue">单播</span>
                    <span v-if="scope.row.exe === 1" style="color: green">组播</span>
                </template>
            </el-table-column>
            <el-table-column
                    label="类型"
                    width="80">
                <template slot-scope="scope">
                    <span v-if="scope.row.type === 0">实时任务</span>
                    <span v-if="scope.row.type === 1">定时任务</span>
                </template>
            </el-table-column>
            <el-table-column
                    prop="terminals"
                    :formatter="initTerminals"
                    label="终端">
            </el-table-column>
        </el-table>
<!--        添加新的任务-->
        <el-dialog
                title="添加任务"
                :visible.sync="addVisible"
                class="add-task">
            <el-input placeholder="可用1 不可用0" v-model="new_task.en" style="margin-bottom: 6px">
                <template slot="prepend">任务可用</template>
            </el-input>
            <el-input placeholder="请输入内容" v-model="new_task.name" style="margin-bottom: 6px">
                <template slot="prepend">任务名称</template>
            </el-input>
            <el-input placeholder="单播0 组播1" v-model="new_task.mode" style="margin-bottom: 6px">
                <template slot="prepend">任务模式</template>
            </el-input>
            <el-input placeholder="请输入内容" v-model="new_task.pn" style="margin-bottom: 6px">
                <template slot="prepend">播放次数</template>
            </el-input>
            <el-input placeholder="11-100" v-model="new_task.lv" style="margin-bottom: 6px">
                <template slot="prepend">任务优先级</template>
            </el-input>
            <el-input placeholder="0每天 1每周 2手动" v-model="new_task.rule" style="margin-bottom: 6px">
                <template slot="prepend">执行规则</template>
            </el-input>
            <el-input placeholder="示例2019-01-01" v-model="new_task.bdate" style="margin-bottom: 6px">
                <template slot="prepend">开始日期</template>
            </el-input>
            <el-input placeholder="默认为当天(无需改动)" v-model="new_task.edate" style="margin-bottom: 6px">
                <template slot="prepend">结束日期</template>
            </el-input>
            <el-input placeholder="开始时间HH:MM:SS" v-model="new_task.eb" style="margin-bottom: 6px">
                <template slot="prepend">开始时间</template>
            </el-input>
            <el-input placeholder="结束时间" v-model="new_task.et" style="margin-bottom: 6px">
                <template slot="prepend">结束时间</template>
            </el-input>
            <p>任务音频</p>
            <el-input placeholder="输入音频文件地址" v-model="new_task.file" style="margin-bottom: 6px">
                <template slot="prepend">音频文件</template>
            </el-input>
            <el-input placeholder="输入默认音量0-100" v-model="new_task.vol" style="margin-bottom: 6px">
                <template slot="prepend">终端音量</template>
            </el-input>
            <p>任务终端</p>
            <el-input placeholder="以，隔开" v-model="new_task.terminals">
                <template slot="prepend">终端ID</template>
            </el-input>
            <span slot="footer" class="dialog-footer">
    <el-button @click="addVisible = false">取 消</el-button>
    <el-button type="primary" @click="addTask">确 定</el-button>
  </span>
        </el-dialog>
<!--        任务详情-->
        <el-dialog
                title="任务信息"
                :visible.sync="task_show"
                class="add-task">
            <el-input placeholder="可用1 不可用0" v-model="task_info.en" style="margin-bottom: 6px">
                <template slot="prepend">任务可用</template>
            </el-input>
            <el-input placeholder="请输入内容" v-model="task_info.name" style="margin-bottom: 6px">
                <template slot="prepend">任务名称</template>
            </el-input>
            <el-input placeholder="单播0 组播1" v-model="task_info.mode" style="margin-bottom: 6px">
                <template slot="prepend">任务模式</template>
            </el-input>
            <el-input placeholder="请输入内容" v-model="task_info.pn" style="margin-bottom: 6px">
                <template slot="prepend">播放次数</template>
            </el-input>
            <el-input placeholder="11-100" v-model="task_info.lv" style="margin-bottom: 6px">
                <template slot="prepend">任务优先级</template>
            </el-input>
            <el-input placeholder="请输入内容" v-model="task_info.bdate" style="margin-bottom: 6px">
                <template slot="prepend">执行日期</template>
            </el-input>
            <el-input placeholder="开始时间HH:MM:SS" v-model="task_info.eb" style="margin-bottom: 6px">
                <template slot="prepend">开始时间</template>
            </el-input>
            <el-input placeholder="结束时间" v-model="task_info.et" style="margin-bottom: 6px">
                <template slot="prepend">结束时间</template>
            </el-input>
            <p>任务音频</p>
            <el-input placeholder="输入音频文件地址" v-model="task_info.file" style="margin-bottom: 6px">
                <template slot="prepend">音频文件</template>
            </el-input>
            <el-input placeholder="输入默认音量0-100" v-model="task_info.vol" style="margin-bottom: 6px">
                <template slot="prepend">终端音量</template>
            </el-input>
            <p>任务终端</p>
            <el-input placeholder="以，隔开" v-model="task_info.terminals">
                <template slot="prepend">终端ID</template>
            </el-input>
            <span slot="footer" class="dialog-footer">
                <el-button @click="start_task">启动</el-button>
                <el-button @click="end_task">停止</el-button>
                <el-button @click="delete_task" type="danger">删除</el-button>
                <el-button type="primary" @click="update_task">更新</el-button>
  </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "task_panel",
        data(){
            return{
                tasklist: [],
                addVisible: false, //添加框
                task_show: false, //任务详情
                new_task: {}, //新任务
                task_info: {}, //任务详情
            }
        },
        mounted(){
            this.get_tasklist();
        },
        methods:{
            //add tasks
            addTask(){
                let _this = this;
                //数据为空判定
                if(_this.new_task.name && _this.new_task.terminals && _this.new_task.vol){
                    let data = {
                        en: _this.new_task.en?_this.new_task.en:1,
                        exe: _this.new_task.exe?_this.new_task.exe:0,
                        name: _this.new_task.name?_this.new_task.name:'new',
                        mode: _this.new_task.mode?_this.new_task.mode:0,
                        pn: _this.new_task.pn?_this.new_task.pn:1,
                        lv: _this.new_task.lv?_this.new_task.lv:99,
                        rule: _this.new_task.rule?_this.new_task.rule:0,
                        file: _this.new_task.file?_this.new_task.file:'',
                        eb: _this.new_task.eb?_this.new_task.eb:null,
                        et: _this.new_task.et?_this.new_task.et:null,
                        vol: _this.new_task.vol?_this.new_task.vol:50,
                        terminals: _this.new_task.terminals?_this.new_task.terminals:''
                    };

                    _this.$axios.post('/api/add_task',data).then(res=>{
                        if(res.data === 'bad'){
                            _this.$message.error('任务添加失败')
                        }else{
                            _this.$message({type: 'success', message: '任务添加成功'});
                            //刷新任务列表
                            _this.addVisible = false;
                            _this.new_task = {};
                            _this.get_tasklist();
                        }
                    })
                }else{
                    _this.$message.error('请完善任务信息');
                }
            },
            //get list
            get_tasklist(){
                let _this = this;
                _this.$axios.post('/api/get_task_list').then(res=>{
                    if(res.data === 'bad'){
                        _this.$message.error('任务列表获取失败')
                    }else{
                        _this.tasklist = res.data;
                    }
                }).catch(()=>{
                    _this.$message.error('丢失与服务器连接');
                })
            },
            //终端信息初始化
            initTerminals(row){
                let list = row.terminals;
                let res = [];
                for(var i=0;i<list.length;i++){
                    res.push(list[i].i)
                }
                return res.join(",");
            },
            //get task
            get_task(row){
                this.task_show = true;
                this.get_task_info(row.id);
            },
            get_task_info(id){
                let _this = this;
                _this.$axios.post('/api/get_task',{"id": id}).then(res=>{
                    if(res.data === 'bad'){
                        _this.$message.error('获取任务信息失败');
                        _this.task_show = false;
                    }else{
                        _this.task_info = res.data;
                        console.log(res.data);
                        //需要对终端进行处理
                        let result = [];
                        for(var i=0;i<_this.task_info.terminals.length;i++){
                            result.push(_this.task_info.terminals[i].i)
                        }
                        _this.task_info.terminals = result.join(",");
                    }
                });
            },
            //update task
            update_task(){
                let _this = this;
                let data = this.task_info;
                let id = data.id;
                let udata = {
                    id: id,
                    en: data.en?data.en:1,
                    exe: data.exe?data.exe:0,
                    name: data.name?data.name:'new',
                    mode: data.mode?data.mode:0,
                    pn: data.pn?data.pn:1,
                    lv: data.lv?data.lv:11,
                    rule: data.rule?data.rule:0,
                    file: data.file?data.file:'',
                    eb: data.eb?data.eb:null,
                    et: data.et?data.et:null,
                    vol: data.vol?data.vol:50,
                    terminals: data.terminals?data.terminals:''
                };
                _this.$axios.post('/api/update_task', udata).then(res=>{
                    if(res.data === 'bad'){
                        _this.$message.error('任务更新失败')
                    }else{
                        _this.$message({type: 'success', message: '任务更新成功'});
                        //清空缓存
                        _this.get_tasklist();
                        _this.task_show = false;
                        _this.task_info = {};
                    }
                })
            },
            //delete task
            delete_task(){
                let id = this.task_info.id;
                let _this = this;
                if(id){
                    _this.$axios.post('/api/delete_task',{"id": id}).then(res=>{
                        if(res.data === 'bad'){
                            _this.$message.error('任务删除失败')
                        }else{
                            _this.$message({type: 'success',message: '任务删除成功'});
                            _this.task_show = false;
                            _this.task_info = {};
                            _this.get_tasklist(); //刷新列表
                        }
                    })
                }
            },
            //start task
            start_task(){
                let id = this.task_info.id;
                let _this = this;
                _this.$axios.post('/api/run_task',{"id": id}).then(res=>{
                    if(res.data === 'bad'){
                        _this.$message.error('任务启动失败')
                    }else{
                        _this.get_tasklist(); //更新任务信息
                        _this.$message({type: 'success',message: '任务启动成功'});
                        _this.task_show = false;
                        _this.task_info = {};
                    }
                });
            },
            //end task
            end_task(){
                let id = this.task_info.id;
                let _this = this;
                _this.$axios.post('/api/end_task',{"id": id}).then(res=>{
                    if(res.data === 'bad'){
                        _this.$message.error('任务停止失败')
                    }else{
                        _this.get_tasklist(); //更新任务信息
                        _this.$message({type: 'success',message: '任务停止成功'});
                        _this.task_show = false;
                        _this.task_info = {};
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .taskpanel{text-align: left;padding: 20px 30px;}
    .gap{padding: 4px;display: block}
    /*任务添加框*/
    .add-task /deep/ .el-dialog{
        width: 70%;
    }
    .bt-row /deep/ .el-button{
        margin-bottom: 10px;
    }
    @media (max-width: 600px) and (min-width:200px){
        .taskpanel{padding: 10px}
        .bt-row /deep/ .el-button{padding: 8px 10px;font-size: 13px}
        .add-task /deep/ .el-dialog{
            width: 96%;
        }
    }
</style>