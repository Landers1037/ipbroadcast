# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:30
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: media_root.py
from flask_restful import Resource
from app.main.token import httpauth
from Util import Req_api,getConfig

api_path = getConfig()['Api']['url']

#得到media文件根目录
class Get_media_root(Resource):
    def post(self):
        try:
            access_id = ''
            access_key = ''
            data = {"access_id":access_id,"access_key":access_key}
            p = Req_api(api_path+'/get_media_root',data)
            return p

        except:
            return False