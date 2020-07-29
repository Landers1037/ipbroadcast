"""
华中科技大学
毕业设计：智能IP广播系统设计
指导老师：罗杰
设计者：廖仁杰 U201613543
在线文档：http://mgek.cc/app/ipbroadcast
Github仓库：https://github.com/landers1037/nms
时间：2019年12月23日

author: Landers
email: liaorenj@gmail.com
school: Huazhong University of S&T
github: https://github.com/landers1037/nms
"""
import webbrowser
import os,sys
import Util
import subprocess
'''
启动浏览器预览页面
基于命令行的启动方式
仅适用于linux服务器

'''
# 配置
Con = Util.getConfig()
# 输出项目的认证信息
author = Con['Copyright']['author']
usercode = Con['Copyright']['usercode']
school = Con['Copyright']['school']
github = Con['Copyright']['github']
email = Con['Copyright']['email']
project = Con['Copyright']['project']

message = '---项目信息---\n[{}]\n作者:{} 学号:{}\n学校:{}\nGithub地址:{}\n邮箱:{}\n'.format(project,author,usercode,school,github,email)
print(message)

url = Con['Server']['url']
webbrowser.open(url)
subprocess.run('python ./app/keepalive.py')
subprocess.run('gunicorn -w 1 -b 127.0.0.1:5000 manage:app')
