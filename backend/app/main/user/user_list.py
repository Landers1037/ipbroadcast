# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:46
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: user_list.py
from flask import jsonify
from Util import getConfig,Req_api
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from app.main.log import nms_log,api_log
from app.models import User

api_path = getConfig()['Api']['url']

#得到用户列表
class Get_user_list(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    @nms_log
    @api_log(__file__)
    def post(self):
        try:
            userlist = User.query.all()
            if userlist:
                tmp = []
                for u in userlist:
                    tmp.append(u.info())

                return jsonify(tmp)
            else:
                return jsonify('bad')

        except:
            return jsonify('bad')