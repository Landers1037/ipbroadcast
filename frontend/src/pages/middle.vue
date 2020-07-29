<template>
<!--    中间件跳转路由使用-->
    <div class="middle">
        <h1>跳转中...</h1>
    </div>
</template>

<script>
    export default {
        name: "middle",
        mounted() {
            let url = this.$route.params.url;
            if(url === ""){
                setTimeout(()=>{
                    this.$router.push("/")
                },1000);

            }else{
                setTimeout(()=>{
                    this.$router.push(url)
                },1000);
            }
        }
    }
</script>

<style scoped>
    .middle{padding: 30px}
</style>