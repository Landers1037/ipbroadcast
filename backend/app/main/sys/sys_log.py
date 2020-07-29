# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:40
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: sys_log.py
from flask_restful import Resource
from Util import getConfig
from app.main.log import nms_log,dellog,api_log

logpath = getConfig()['Log']['logpath']

#log
class Sys_log(Resource):
    #日志路由无需记录log
    @api_log(__file__)
    def post(self):
        log = '<p style="color: #e8251e;font-size: 1.2em">nms.log powered by NMS</p>'
        with open(logpath + 'nms.log','r',encoding='utf-8')as f:
           lines = f.readlines()
           for l in lines:
               log = log + l + '<br>'

        return log