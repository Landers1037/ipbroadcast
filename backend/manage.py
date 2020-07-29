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

import os,Util
from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

#配置
Con = Util.getConfig()
port = Con['Server']['port']

app = create_app(flask_config_name="dev")
migrate = Migrate(app,db)
#command
Manager = Manager(app)
Manager.add_command("run", Server(port=port))
Manager.add_command('db',MigrateCommand)

if __name__ == '__main__':

    Manager.run()
