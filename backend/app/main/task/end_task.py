# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:07
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: end_task.py
from Util import getConfig,Req_api
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from app import db
from app.models import Task

api_path = getConfig()['Api']['url']

#结束任务
class End_task(Resource):
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
            end_task = Task.query.get(int(id))
            if end_task:
                data = {"access_id":access_id,"access_key":access_key,"id":int(id)}
                res = Req_api(api_path+'/end_task',data)
                if res["msg"] == "ok":
                    try:
                        end_task.run = 0
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