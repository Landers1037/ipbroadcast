# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:59
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: first_user.py
from flask import jsonify
from flask_restful import Resource
from app.models import User
from app.main.log import nms_log,api_log

class First_user(Resource):
    @nms_log
    @api_log(__file__)
    def post(self):
        m = User.query.first()

        return jsonify({"user":m.user,"pass":m.password})