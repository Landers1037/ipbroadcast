# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:57
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: del_all_user.py

from flask_restful import Resource
from app import db
from app.models import User

class Delete_all(Resource):
    def get(self):
        all = User.query.all()
        db.session.remove(all)
        db.session.commit()
        return 'delete all users'