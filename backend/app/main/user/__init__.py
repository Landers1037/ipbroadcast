# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:44
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py
"""
用户api模块部分
实现的功能：
用户的添加，删除，修改，统计
"""
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

user = Blueprint('user',__name__)

api = Api(user)
cors = CORS(user)

from .user_list import Get_user_list
from .get_user import Get_user
from .current_user_info import Get_user_info
from .add_user import Add_user
from .update_user import Update_user
from .delete_user import Delete_user
from .delete_myself import Delete_myself

api.add_resource(Get_user_list,'/api/get_user_list')
api.add_resource(Get_user,'/api/get_user')
api.add_resource(Get_user_info,'/api/get_user_info')
api.add_resource(Add_user,'/api/add_user')
api.add_resource(Update_user,'/api/update_user')
api.add_resource(Delete_user,'/api/delete_user')
api.add_resource(Delete_myself,'/api/delete_myself')