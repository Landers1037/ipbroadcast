# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: stayalive.py

from flask import request,jsonify
from flask_restful import Resource
from app.main.token import httpauth
from app.main.log import api_log,nms_log
from Util import Req_api,getConfig
from app.main.token import verify_auth_token
from app.models import User
from app import db

api_path = getConfig()['Api']['url']

'''
每一个登录函数都在每次请求api的时候把id和key重新保存到数据库里刷新使用，写入isactive的值判断是否掉线。
在前端每一次读取isactive的值如果返回值为0表示已经掉线需要重新登录
这里注意flask的登录和硬件的登录是两套系统，所以在flask登录时，硬件的登录可以单独写，保证无需重新登录flask
'''


class Keepalive(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    @nms_log
    @api_log(__file__)
    def post(self):
        #发送状态码请求
        try:
            token = request.headers["Authorization"]
            current = verify_auth_token(token)
            access_id = int(current.access_id) #注意格式是int
            access_key = current.access_key
            data = {"access_id":access_id,"access_key":access_key}
            p = Req_api(api_path+'/online',data)
            #验证是否能发送在线
            if p["msg"] == 'ok':
                print('连接状态:alive')

                return jsonify({"status":True})
            else:
                #清空access
                current.access_id = ''
                current.access_key = ''
                db.session.commit()
                return jsonify({"status":False})

        except:

            return jsonify({"status":False})