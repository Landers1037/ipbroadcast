# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: delete_task.py
from Util import getConfig,Req_api
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from app import db
from app.models import Task

api_path = getConfig()['Api']['url']

#删除任务
#需要和广播的服务进行交互
class Delete_task(Resource):
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
            # 先从数据库删除任务
            del_task = Task.query.get(int(id))
            if del_task:
                try:
                    db.session.delete(del_task)
                    db.session.commit()
                except:
                    db.session.commit()
                data = {"access_id":access_id,"access_key":access_key,"id":int(id)}
                res = Req_api(api_path+'/delete_task',data)
                if res["msg"] == "ok":

                    return jsonify("ok")
                else:
                    print(res)
                    #这个接口失效了
                    return jsonify("ok")

            else:
                #任务不存在
                return jsonify("bad")

        except Exception as e:
            print(e.args)
            return jsonify("bad")