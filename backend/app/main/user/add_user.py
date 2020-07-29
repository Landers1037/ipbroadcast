# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:50
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: add_user.py
from flask import jsonify
from Util import getConfig,Req_api,Second_encrypt
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from app.main.log import nms_log,api_log
from app import db
from app.models import User

api_path = getConfig()['Api']['url']


#添加用户
class Add_user(Resource):
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

            new_user_data = request.json
            new_name = new_user_data["name"]
            new_pass = new_user_data["pw"]
            new_af_pass = Second_encrypt(new_pass) #encrypt
            new_m = new_user_data["m"]
            new_ml = new_user_data["ml"]
            new_tl = new_user_data["tl"]
            new_type = 'admin' if len(new_ml)==3 else 'normal'

            # 在添加前做用户名称的唯一性判断
            p = User.query.filter_by(user=new_name).first()
            if p or new_name == 'root':
                return jsonify('repeat')
            else:
                new_user = User(
                    user=new_name,
                    password=new_pass,
                    after_pass=new_af_pass,
                    type = new_type,
                    m = new_m,
                    ml = new_ml,
                    tl = new_tl
                )
                try:
                    db.session.add(new_user) #事务提交后，进入等待，如果广播返回正确那么执行 否则数据库回滚
                    db.session.commit()
                    return jsonify('ok')
                    # 存储到广播内的用户权限均最高 因为不清楚广播内用户的权限分布

                #修改后用户只在后端添加
                except:
                    #ip广播添加失败就回滚数据库操作
                    db.session.rollback()
                    return jsonify('bad')

        except Exception as e:
            print(e.args)
            return jsonify('bad')