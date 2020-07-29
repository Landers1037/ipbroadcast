# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:30
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: update_terminal.py
#更新媒体设备信息
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from Util import Req_api,getConfig
from app import db
from app.models import Media

api_path = getConfig()['Api']['url']


class Update_terminal(Resource):
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

            id = int(request.json["id"])
            name = request.json["name"]
            power = request.json["power"]
            media = Media.query.get(id)
            media.name = name
            media.power = power
            new_data = request.json
            db.session.commit()

            data = {"access_id":access_id,"access_key":access_key,"id":id,"data":new_data}
            res = Req_api(api_path+'/update_terminal',data)
            if res["msg"] == 'ok':
                return jsonify('ok')
            else:
                db.session.rollback()
                return jsonify('bad')

        except:
            return jsonify('bad')