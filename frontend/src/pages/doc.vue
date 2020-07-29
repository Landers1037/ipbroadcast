<template>
    <div>
        <el-alert style="min-width: 200px;max-width: 940px;margin: 0 auto;font-size: 1.2em;padding: 14px"
                title="现有的api仍处于测试阶段，可能与需求不一致"
                type="error"
                effect="dark"
        >
        </el-alert>
        <div class="markdown-body" v-html="md" style="text-align: left" @click="check"></div>
    </div>

</template>

<script>
    const marked = require('marked');
    import api from "../../public/doc/nmsAPI.md";
    import auth_unit from "../../public/doc/auth_unit.md";
    import user_unit from "../../public/doc/user_unit.md";
    // import media_unit from "../../public/doc/media_unit.md";
    // import task_unit from "../../public/doc/task_unit.md";
    // import sys_unit from "../../public/doc/sys_unit.md";
    // import test_unit from "../../public/doc/test_unit.md";
    export default {
        name: "doc",
        data() {
            return{
                md: "# hello"
            }
        },
        watch: {
            md : function () {
            }
        },
        created() {
            this.md = marked(api);
        },
        methods: {
            check(obj){
                switch (obj.toElement.textContent) {
                    case "首页": this.md = marked(api);break;
                    case "登录接口": this.md = marked(auth_unit);break;
                    case "用户接口": this.md = marked(user_unit);break;
                    case "终端接口": this.md = marked(media_unit);break;
                    case "任务接口": this.md = marked(task_unit);break;
                    case "系统信息接口": this.md = marked(sys_unit);break;
                    case "测试接口": this.md = marked(test_unit);break;
                }
            }
        }
    }
</script>

<style scoped>
    .markdown-body {
        box-sizing: border-box;
        min-width: 200px;
        max-width: 980px;
        margin: 0 auto;
        padding: 45px;
    }
</style>
<style>
    .markdown-body{font-family: 'sh', sans-serif!important;}
    .markdown-body .api{color: #0079ba;cursor: pointer}
    .markdown-body .api:hover{text-decoration: #005cc5;text-decoration-style: solid;text-decoration: underline}
     ul li p:first-child{color: #f28d00;font-weight: bold;font-size: 1.2em}
</style>