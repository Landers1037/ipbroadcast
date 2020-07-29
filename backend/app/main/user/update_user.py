# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:51
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: update_user.py
from flask import jsonify
from Util import getConfig,Req_api,Second_encrypt
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from app.main.log import nms_log,api_log
from app import db
from app.models import User

api_path = getConfig()['Api']['url']


#更新用户信息
class Update_user(Resource):
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
            access_id = int(current.access_id)
            access_key = current.access_key

            # 判断当前用户是否为root 如果是则root可以修改自己的名称为root
            new_data = request.json
            id = new_data["id"]
            new_name = new_data["name"]
            new_pass = new_data["pw"]
            new_af_pass = Second_encrypt(new_pass) #encrypt
            new_m = new_data["m"]
            new_ml = new_data["ml"]
            new_tl = new_data["tl"]

            new_type = 'admin' if len(new_ml) == 3 else 'normal'
            up_user = User.query.filter_by(id=id).first() # 要更新的用户
            p = User.query.filter_by(user=new_name).first() # 是否存在名称为newname的用户

            if up_user.user == 'root':
                # 针对root用户的单独判定,root用户是系统内置用户 不能修改
                return jsonify('repeat')
            else:
                if not p:
                    # 判定当前用户的新名称是否和存在的用户重复
                    up_user.user = new_name
                    up_user.password = new_pass
                    up_user.after_pass = new_af_pass
                    up_user.m = new_m
                    up_user.ml = new_ml
                    up_user.tl = new_tl
                    up_user.type = new_type

                    try:
                        db.session.commit()
                        return jsonify('ok')
                    except:
                        db.session.rollback()
                        return jsonify("bad")

                elif p == up_user:
                    # 要更新的属于同一用户，即用户名没变
                    up_user.user = new_name
                    up_user.password = new_pass
                    up_user.after_pass = new_af_pass
                    up_user.m = new_m
                    up_user.ml = new_ml
                    up_user.tl = new_tl
                    up_user.type = new_type

                    try:
                        db.session.commit()
                        return jsonify('ok')
                    except:
                        db.session.rollback()
                        return jsonify("bad")

                elif p.id != up_user.id:
                    # 新名称存在且不是同一用户
                    return jsonify('repeat')


        except Exception as e:
            print(e.args)
            return jsonify("bad")