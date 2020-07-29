# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:23
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

"""
终端api模块部分
实现的功能：
终端设备的添加删除，更新
"""

from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS


media = Blueprint('media',__name__)

api = Api(media)
cors = CORS(media)

from .get_terminal_list import Get_terminal_list
from .get_terminal import Get_terminal
from .delete_terminal import Delete_terminal
from .update_terminal import Update_terminal
from .media_root import Get_media_root

api.add_resource(Get_terminal_list,'/api/get_terminal_list')
api.add_resource(Get_terminal,'/api/get_terminal+<id>')
api.add_resource(Get_media_root,'/api/get_media_root')
api.add_resource(Update_terminal,'/api/update_terminal')
api.add_resource(Delete_terminal,'/api/delete_terminal+<id>')