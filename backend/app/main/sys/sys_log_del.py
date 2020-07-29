# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:41
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: sys_log_del.py
from flask_restful import Resource
from Util import getConfig
from app.main.log import nms_log,dellog,api_log

logpath = getConfig()['Log']['logpath']

class Sys_log_del(Resource):
    @api_log(__file__)
    def post(self):
        dellog()
        return 'nms.log is clean'