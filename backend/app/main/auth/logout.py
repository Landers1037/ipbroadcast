# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:17
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: logout.py
from flask import request,jsonify
from flask_restful import Resource
from app.main.log import api_log,nms_log
from app.main.token import httpauth,verify_auth_token
from app import db

class Logout(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    @nms_log
    @api_log(__file__)
    def post(self):
        #在退出的时候清空验证id和key，保证下次登录时可以更新
        token = request.headers["Authorization"]
        current = verify_auth_token(token)
        current.access_id = ''
        current.access_key = ''
        db.session.commit()
        return jsonify({"islogged":0})