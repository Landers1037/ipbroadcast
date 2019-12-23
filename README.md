# ipbroadcast
基于web设计的智能ip广播系统

# 设计要求

设计一个IP广播系统应采用集中式管理模式，在校园设立广播系统集成服务器，充分利用校园网络将各个区域的广播音频终端连接起来，组成一套数字化的网络广播系统。在系统服务器统一控制IP广播的播放内容，播放时间，定时上电及下电 。

# 需求环境

- Flask构造的web后端服务，实现底层的api需求
- 使用vue进行前端界面设计
- 使用PCBA提供的javascript SDK进行功能设计，完成整个管理系统的设计
- 对前后端合并完成总体设计
- Jquery，bootstrap等前端技术

# 目标

（1）研究提供的IP广播PCBA控制板及其配套的SDK包解读，实现HTML/JavaScript对SDK包的API函数调用。

（2）研究Python、Node.js、HTML5/JavaScript/CSS、vue.js及MySql数据库等，实现一个基于智慧教室的IP广播管理系统。

（3）设计本课题的教室IP广播网络管理系统中，管理员通过自己的学号或者工号登录系统，并实现权限的分离和管理。

（4）IP广播网络管理系统，支持系统定时播放，临时插播、实时监控音频终端的系统情况。

（5）建立实时数据同步的监控机制，及时发现数据传输中存在的问题，并通过技术手段将告警知会管理人员。

（6）设计为web网站形式，实现前后端分离，前端用vue.js框架，后端实现对数据库的操作并暴露相关的API。

（7）广播网络管理系统具有日志功能，可以记录数据推送的时间等信息。

# 设计思路

1. 使用Flask完成整个后端的设计，设计需求的api与SDK进行对接。使用Flask-Script进行项目控制，使用Flask-migrate进行数据库迁移工作，使用Flask-Restful完成api的设计，对于vue前端的调用使用flask-cors完成跨域需求
2. 对于登录需求使用Flask-Login进行用户登录的控制
3. 使用Postgresql数据库完成数据的保存
4. 建立全局的Debug函数，对出现的错误进行统计，并且按照时间保存为本地的.log文件以供分析
5. 前端使用vue2.0开发，使用bootstrap完成css样式的美化
6. 定时系统使用flask-apscheduler进行定时任务操作

# 参考资料

- Flask-Restful[文档](http://www.pythondoc.com/Flask-RESTful/quickstart.html)
- Flask-Cors [文档](https://flask-cors.readthedocs.io/en/latest/)
- VUE [文档](https://cn.vuejs.org/)
- vue-cli [文档](https://cli.vuejs.org/zh/guide/cli-service.html)
- bootstrap [文档](https://www.bootcss.com/)