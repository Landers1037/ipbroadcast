# -*- coding: utf-8 -*-
# Time: 2020-05-15 10:12
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: sys_log_backup.py

from flask_restful import Resource
from Util import getConfig
from app.main.log import api_log,backup

logpath = getConfig()['Log']['logpath']

class Sys_log_backup(Resource):
    @api_log(__file__)
    def post(self):
        try:
            backup()
            return 'nms.log backup success'
        except:
            return 'bad'