# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:02
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py.py
"""
任务api模块部分
实现的功能：
任务的添加，删除，修改，统计
"""

from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

task = Blueprint('task',__name__)

api = Api(task)
cors = CORS(task)

from .get_task_list import Get_task_list
from .get_task import Get_task
from .add_task import Add_task
from .delete_task import Delete_task
from .update_task import Update_task
from .run_task import Run_task
from .end_task import End_task


api.add_resource(Get_task_list,'/api/get_task_list')
api.add_resource(Get_task,'/api/get_task')
api.add_resource(Add_task,'/api/add_task')
api.add_resource(Update_task,'/api/update_task')
api.add_resource(Delete_task,'/api/delete_task')
api.add_resource(Run_task,'/api/run_task')
api.add_resource(End_task,'/api/end_task')
