# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:03
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_task_list.py

from Util import getConfig,Req_api
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from app.models import Task

api_path = getConfig()['Api']['url']

#得到任务列表
#为简化获取的请求，仅从数据库中生成任务信息
class Get_task_list(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            task_list = []
            T = Task.query.all()
            if T:
                for t in T:
                    task_list.append(t.get_task())

                return jsonify(task_list)
            else:
                return jsonify([])

        except:
            return jsonify('bad')