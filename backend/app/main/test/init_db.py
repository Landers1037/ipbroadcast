# -*- coding: utf-8 -*-
# Time: 2020-04-28 14:43
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: init_db.py

from flask import jsonify
from flask_restful import Resource
from app import db


class initDB(Resource):
    def post(self):
        try:
            db.create_all()
            from app.models import Apitrack
            a = Apitrack(login=0,user=0,task=0,sys=0,media=0)
            db.session.add(a)
            db.session.commit()
            return jsonify("database created")
        finally:
            db.drop_all()
            db.create_all()
            return jsonify("database created")