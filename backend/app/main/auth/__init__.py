# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:03
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: __init__.py
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

auth = Blueprint('auth',__name__)

api = Api(auth)
cors = CORS(auth)

from .login import Login
from .root_login import Root_login
from .logout import Logout
from .keepalive import Keepalive

api.add_resource(Root_login,'/api/root_login')
api.add_resource(Login,'/api/login')
api.add_resource(Logout,'/api/logout')
api.add_resource(Keepalive,'/api/keepalive')