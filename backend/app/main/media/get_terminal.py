# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:27
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_terminal.py
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth
from Util import Req_api,getConfig
from app.models import Media

api_path = getConfig()['Api']['url']


#得到终端信息
class Get_terminal(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            id = request.json["id"]
            m = Media.query.get(int(id))
            if m:
                return jsonify(m.get_meida())
            else:
                return jsonify("bad")

        except:
            return jsonify("bad")