# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:52
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: delete_user.py
from flask import jsonify
from Util import getConfig,Req_api
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from app.main.log import nms_log,api_log
from app.models import User
from app import db

api_path = getConfig()['Api']['url']


#删除指定用户
class Delete_user(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }

    @nms_log
    @api_log(__file__)
    def post(self):
        try:
            #数据库同步删除
            #保证root管理员不会被删除
            # 保证当前登录用户不会被删除
            id = int(request.json['id'])
            d_user = User.query.get(id)
            token = request.headers["Authorization"]
            current = verify_auth_token(token)
            access_id = int(current.access_id)
            access_key = current.access_key
            if current.id == id:
                return jsonify('bad')

            elif d_user and d_user.user != 'root':
                try:
                    db.session.delete(d_user)
                    db.session.commit()
                    return jsonify('ok')
                except:
                    db.session.rollback()
                    return jsonify('bad')
            else:

                return jsonify('bad')

        except:
            return jsonify('bad')