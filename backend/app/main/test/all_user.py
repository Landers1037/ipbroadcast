# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:56
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: all_user.py
from flask import jsonify
from flask_restful import Resource
from app import db
from app.models import User
from app.main.token import httpauth

class All_user(Resource):
    # method_decorators = {
    #     'get':[httpauth.login_required],
    #     'post':[httpauth.login_required]
    # }
    def get(self):
        all = User.query.all()
        userlist = []
        for u in all:
            userlist.append([u.id,u.user,u.password,u.ml,u.tl])
        return jsonify({"userlist":userlist})