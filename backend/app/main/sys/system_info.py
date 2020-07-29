# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:35
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: system_info.py
from flask_restful import Resource,request
from flask import jsonify
from Util import getConfig,Get_mem,Get_sys,Get_copy,Req_api
from app.main.log import nms_log,dellog,api_log
from app.main.token import verify_auth_token

logpath = getConfig()['Log']['logpath']
api_path = getConfig()['Api']['url']

#系统信息
class Sys_detail(Resource):
    data = {"api":api_path,"mem": 100,"userdata":[],"sysdata":[],"copy":[]}
    @nms_log
    @api_log(__file__)
    def post(self):
        try:
            token = request.headers["Authorization"]
            current_user = verify_auth_token(token) #返回token认证的用户

            if current_user.user:
                #用户登录状态
                #获取后台连接状态
                access_data = {"access_id":int(current_user.access_id),"access_key":current_user.access_key}
                is_online = "硬件服务器: "
                try:
                    s = Req_api(api_path + '/online',access_data)
                    if s["msg"] == "ok":
                        is_online = "硬件服务器: 在线"
                    else:
                        is_online = "硬件服务器: 离线"
                except:
                    is_online = "硬件服务器 :离线"
                user_detail = ["name:"+current_user.user,"type:"+current_user.type]
                data = self.data
                data["mem"] = Get_mem('python')
                data["userdata"] = user_detail
                data["sysdata"] = Get_sys()
                data["sysdata"].append(is_online)
                data["copy"] = Get_copy()
                return jsonify(data)

        except:
            data = self.data
            data["mem"] = Get_mem('python')
            data["userdata"] =  ['no-login','type:none']
            data["sysdata"] = Get_sys()
            data["sysdata"].append("硬件服务器: 离线")
            data["copy"] = Get_copy()
            return jsonify(data)