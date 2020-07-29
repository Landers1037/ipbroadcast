# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:58
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: if_login.py
from flask_restful import Resource,request
from app.main.token import verify_token

class If_login(Resource):
    def get(self):
        try:
            token = request.headers["Authorization"]
            rs = verify_token(token)
            if rs:
                return 'login'

            else:
                return 'not logged'
        except:
            return 'get status error'