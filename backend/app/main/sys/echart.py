# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:42
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: echart.py
from flask_restful import Resource
from flask import jsonify
from Util import getConfig,Get_mem
import psutil
from app.models import User,Apitrack
from app.main.log import api_log,nms_log
from app import db

logpath = getConfig()['Log']['logpath']


class Echarts_data(Resource):
    @api_log(__file__)
    def post(self):
        #为防止没有初始化数据库 先初始化
        this = Apitrack.query.get(1)
        if this:
            pass
        else:
            a = Apitrack(0,0,0,0,0)
            db.session.add(a)
            db.session.commit()

        sysdata = []
        trackdata = []
        sysdata.append({"name": "Others","value":psutil.virtual_memory().percent})
        sysdata.append({"name": "Nginx","value": Get_mem('nginx')})
        sysdata.append({"name": "Flask","value": Get_mem('python')})

        trackdata.append(this.login)
        trackdata.append(this.user)
        trackdata.append(this.media)
        trackdata.append(this.media)
        trackdata.append(this.sys)

        return jsonify([sysdata,trackdata])