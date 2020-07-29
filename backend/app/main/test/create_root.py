# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:57
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: create_root.py
from Util import Second_encrypt
from flask_restful import Resource
from app import db
from app.models import User

#create root
class Create_root(Resource):
    def get(self):
        af = Second_encrypt('123456')
        root = User(user='root',password='123456',after_pass=af,type='root')
        db.session.add(root)
        db.session.commit()
        return 'successfully create root'