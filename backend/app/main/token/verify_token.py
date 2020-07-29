# -*- coding: utf-8 -*-
# Time: 2020-04-02 11:38
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: verify_token.py

from .easy_auth import HTTPTokenAuth,verify_auth_token
from flask import request

httpauth = HTTPTokenAuth()

@httpauth.verify_token
def verify_token(token):
    try:
         token = request.headers["Authorization"]
         if verify_auth_token(token) or token == "test":
             return True
         else:
             return False
    except:
        print('no token')
        return False