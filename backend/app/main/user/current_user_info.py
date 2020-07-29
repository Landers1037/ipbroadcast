# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:49
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: current_user_info.py
from flask import jsonify
from Util import getConfig,Req_api
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from app.main.log import nms_log,api_log

api_path = getConfig()['Api']['url']


#得到当前登录用户信息
class Get_user_info(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    @nms_log
    @api_log(__file__)
    def post(self):
        try:
            token = request.headers["Authorization"]
            current = verify_auth_token(token)

            data = current.info()
            return jsonify(data)

        except:

            return jsonify('bad')