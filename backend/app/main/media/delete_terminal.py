# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:28
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: delete_terminal.py
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from flask import jsonify
from Util import Req_api,getConfig
from app import db
from app.models import Media

api_path = getConfig()['Api']['url']


#删除终端设备信息
class Delete_terminal(Resource):
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
            #先删除数据库数据
            del_term = Media.query.get(int(id))
            if del_term:
                db.session.delete(del_term)
                db.session.commit()
                data = {"access_id":access_id,"access_key":access_key,"id":int(id)}
                res = Req_api(api_path+'/delete_terminal',data)
                if res["msg"] == "ok":
                    return jsonify("ok")
                else:
                    db.session.rollback()
                    return jsonify("bad")

            else:
                return jsonify("bad")

        except:
            return jsonify("bad")