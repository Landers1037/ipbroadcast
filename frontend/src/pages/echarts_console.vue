<template>
    <div class="echarts">
        <h3><i class="el-icon-back back" @click="back_to_dash"></i>后台监控数据</h3>
        <div class="datas">
            <div id="mychart1">

            </div>
            <div id="mychart2">

            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import {MessageBox}from 'element-ui';
    export default {
        name: "echarts_console",
        data(){
            return{
                myChart1: null,
                myChart2: null,
                sysdata: [{"name":"data1","value":10},{"name":"data2","value":20},{"name":"data3","value":30}],
                trackdata: [100,100,100,100]
            }
        },
        watch: {
            sysdata: function () {
            },
            trackdata: function () {
            }
        },
        created(){
            let _this = this;
            window.onresize = function () {
                _this.myChart1 = _this.$echarts.init(document.getElementById('mychart1'),'light');
                _this.myChart1.resize();
                _this.myChart2.resize();
            }

        },
        mounted() {
            let that = this;
            axios
                .post('/api/echarts_data')
                .then(res => {
                    that.sysdata = res.data[0];
                    that.trackdata = res.data[1];
                    that.drawsysdata();
                    that.drawtrack();
                }).catch(err=>{
                console.log(err);
                MessageBox.alert("服务器未响应");
                that.drawsysdata();
                that.drawtrack();
            });

            let _this = this;
            window.onresize = function () {
                _this.myChart1 = _this.$echarts.init(document.getElementById('mychart1'),'light');
                _this.myChart1.resize();
                _this.myChart2.resize();
            }
        },
        methods: {
            drawsysdata(){
                let that = this;
                this.myChart1 = this.$echarts.init(document.getElementById('mychart1'),'light');
                let sysdata = this.sysdata;
                this.myChart1.setOption({
                    title: {text: "后端服务占用"},
                    series: {
                        type: 'pie',
                        radius: '90%',
                        center: ['50%', '50%'],
                        data: sysdata,
                        animation: true,
                        label: {
                            position: 'inner',
                            alignTo: 'none',
                            bleedMargin: 5
                        },
                        left: 0,
                        right: 100,
                        top: 0,
                        bottom: 0
                    }
                });
                window.onresize = function () {
                    that.myChart1.resize();
                }

            },
            drawtrack(){
                let that = this;
                let trackdata = that.trackdata;
                that.myChart2 = that.$echarts.init(document.getElementById('mychart2'),'light');
                that.myChart2.setOption({
                    title: {text: "api请求次数"},
                    xAxis: {
                        type: 'category',
                        data: ['Login', 'User', 'Task', 'Media', 'Sys']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: trackdata,
                        type: 'line'
                    }]
                })
            },
            back_to_dash(){
                this.$router.push('/dashboard');
            }
        }
    }
</script>

<style scoped>
    .echarts{padding: 20px 10px}
    .echarts .datas{margin: 0 auto;max-width: 900px;padding: 30px;position: relative}
    .echarts #mychart1{width: 400px;height: 400px;float: left;margin-right: 50px}
    .echarts .back{cursor: pointer;float: left;position: fixed;left: 60px;font-weight: bold}
    .echarts .back:hover{color: #005cc5}
    .echarts #mychart2{width: 400px;height: 400px;float: left}
</style>