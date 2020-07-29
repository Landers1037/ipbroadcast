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

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

CONFIG_NAME_MAPPER = {
    'product': 'app.app_config.ProductionConfig',
    'dev': 'app.app_config.DevelopmentConfig',
    'test': 'app.app_config.TestingConfig'
}

def create_app(flask_config_name=None):
    app = Flask(__name__,static_url_path='')

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'testDB.db')

    env_flask_config_name = os.getenv('FLASK_CONFIG')
    config_mapper_name = flask_config_name or env_flask_config_name or 'dev'
    config_name = CONFIG_NAME_MAPPER[config_mapper_name]
    app.config.from_object(config_name)
    app.jinja_env.auto_reload = True
    app.jinja_env.variable_start_string = '{{{{'
    app.jinja_env.variable_end_string = '}}}}'

    db.init_app(app)

    from .main.auth import auth as auth_blueprint #解决循环导入
    from .main.media import media as media_blueprint
    from .main.user import user as user_blueprint
    from .main.task import task as task_blueprint
    from .main.test import test as test_blueprint
    from .main.sys import sys as sys_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(media_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)
    app.register_blueprint(test_blueprint)
    app.register_blueprint(sys_blueprint)


    return app

