# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:32
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py

"""
系统信息api模块部分
实现的功能：
统计系统信息，后端服务状态
"""

from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

sys = Blueprint('sys',__name__)

api = Api(sys)
cors = CORS(sys)

from .system_info import Sys_detail
from .sys_log import Sys_log
from .sys_log_del import Sys_log_del
from .echart import Echarts_data
from .sys_log_backup import Sys_log_backup

api.add_resource(Sys_detail,'/api/sys_detail')
api.add_resource(Sys_log,'/api/sys_log')
api.add_resource(Sys_log_del,'/api/sys_log_del')
api.add_resource(Sys_log_backup,'/api/sys_log_backup')
api.add_resource(Echarts_data,'/api/echarts_data')
