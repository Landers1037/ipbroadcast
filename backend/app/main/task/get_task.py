# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:04
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_task.py

from Util import getConfig,Req_api
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth
from app.models import Task

api_path = getConfig()['Api']['url']

# 定时任务详情
class Get_task(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            id = request.json["id"]
            current_task = Task.query.get(int(id))
            if current_task:
                task_info = current_task.get_task()
                return jsonify(task_info)
            else:
                return jsonify('bad')

        except Exception as e:
            print(e.args)
            return jsonify('bad')