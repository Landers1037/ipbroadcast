# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:03
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: login.py
from flask import request,jsonify
from flask_restful import Resource
from app.main.token import generate_token,check_password
from app.main.log import api_log,nms_log
from Util import Req_api,getConfig
from app import db
from app.models import User

api_path = getConfig()['Api']['url']

class Login(Resource):
    @nms_log
    @api_log(__file__)
    def post(self):
        #管理员的登录
        #所有登录使用flask做代理
        try:
            user = request.json["user"]
            password = request.json["pass"]
            loguser = User.query.filter_by(user=user).first()

            if check_password(password,loguser.after_pass): #密文
                token = generate_token(loguser.id)
                print(loguser.user) #测试输出当前登录的用户
                data = {"user":'admin',"password":'admin'} #明文
                p = Req_api(api_path+'/login',data)
                if p["msg"] == "ok":
                    access_id = p["access_id"]
                    access_key = p["access_key"]
                    loguser.access_id = access_id
                    loguser.access_key = access_key
                    db.session.commit()
                    # 更新密钥
                    return jsonify({"status":1,"user":"admin","token":token})
                else:
                    return jsonify({"status": 0, "user": None, "token": ""})

            else:
                return jsonify({"status":0,"user":user["user"],"token":""})

        except Exception as e:
            return jsonify({"status":0,"user":None,"token":""})