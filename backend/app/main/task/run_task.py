# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: run_task.py
from Util import getConfig,Req_api
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from app.models import Task
from app import db

api_path = getConfig()['Api']['url']


#执行定时任务
#假设exe是任务的运行状态
class Run_task(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            token = request.headers["Authorization"]
            current = verify_auth_token(token)
            access_id = int(current.access_id)
            access_key = current.access_key

            id = request.json["id"]
            run_task = Task.query.get(int(id))
            if run_task:
                data = {"access_id":access_id,"access_key":access_key,"id":int(id)}
                res = Req_api(api_path+'/run_task',data)
                if res["msg"] == "ok":
                    try:
                        run_task.run = 1
                        db.session.commit()
                    except:
                        db.session.rollback()
                    return jsonify("ok")
                else:
                    db.session.rollback()
                    return jsonify("bad")
            else:
                return jsonify("bad")

        except:
            return jsonify("bad")