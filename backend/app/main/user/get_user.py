# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:47
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_user.py
from flask import jsonify
from Util import getConfig,Req_api
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from app.main.log import nms_log,api_log
from app.models import User

api_path = getConfig()['Api']['url']


#得到用户信息
class Get_user(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    @nms_log
    @api_log(__file__)
    def post(self):
        try:
            id = int(request.json["id"])


            want_user = User.query.filter_by(id=id).first()
            # 用户由数据库中读取和后台保持一致
            if want_user:
                userdata = want_user.info()
                return jsonify(userdata)
            else:
                return jsonify('bad')

        except Exception as e:
            print(e.args)
            return jsonify("bad")