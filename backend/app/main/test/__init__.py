# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:54
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py
"""
无需验证的测试api模块部分
实现的功能：
api的测试
"""

from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

test = Blueprint('test',__name__)

api = Api(test)
cors = CORS(test)

from .all_user import All_user
from .del_all_user import Delete_all
from .create_root import Create_root
from .if_login import If_login
from .first_user import First_user
from .init_db import initDB

api.add_resource(All_user,'/test/all_user')
api.add_resource(Delete_all,'/test/delete_all')
api.add_resource(Create_root,'/test/cr')
api.add_resource(initDB,'/test/initdb')
api.add_resource(If_login,'/test/if_login')
api.add_resource(First_user,'/test/first')
