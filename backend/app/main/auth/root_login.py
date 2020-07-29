# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:15
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: root_login.py
from flask import request,jsonify
from flask_restful import Resource
from app.main.token import generate_token
from app.main.log import api_log,nms_log
from Util import Req_api,getConfig,Second_decode,Second_encrypt
from app import db
from app.models import User

api_path = getConfig()['Api']['url']
# root_name = getConfig()['Admin']['rootname']
root_name = 'root'
root_password = getConfig()['Admin']['password']

class Root_login(Resource):
    @nms_log
    @api_log(__file__)
    def post(self):
        if request.json:
            try:
                detail = request.json
                if detail["user"] == 'root' and Second_decode(detail["pass"]) == root_password:
                    #因为root是系统内定的所以不存在时先创建
                    loguser = User.query.filter_by(user='root').first()
                    # 如果密码更改则更新密码
                    if not loguser:
                        root_user = User(
                            user='root',
                            password=root_password,
                            after_pass=Second_encrypt(root_password),
                            type='admin',
                            m='root',
                            ml='utm',
                            tl='3'
                        )
                        db.session.add(root_user)
                        db.session.commit()

                    if loguser.password != root_password:
                        loguser.password = root_password
                        db.session.commit()

                    token = generate_token(loguser.id)
                    # #测试验证
                    # root超级管理员账户无需在广播的数据库里进行认证，简化步骤
                    # 获取广播access权限
                    try:
                        data = {"user": "admin", "password": "admin"}
                        res = Req_api(api_path + '/login', data)
                        access_id = res["access_id"]
                        access_key = res["access_key"]
                        loguser.access_id = access_id #更新数据库的access权限
                        loguser.access_key = access_key
                        db.session.commit()

                        return jsonify({"status": 1, "user": "root", "token": token})

                    except Exception as e:
                        print(e.args)
                        # 广播的用户认证失败，无法登录
                        # 测试时暂时允许可以使用root认证登录
                        # return jsonify({"status": 0, "user": None, "token": ''})
                        return jsonify({"status": 1, "user": 'TEST', "token": token})

                else:
                    return jsonify({"status": 0, "user": detail["user"],"token":""})
            except Exception as e:
                print(e.args)
                return jsonify({"status": 0, "user": None, "token": ""})
        else:
            return jsonify({"status":0,"user":None,"token":''})