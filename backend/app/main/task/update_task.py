# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:06
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: update_task.py
from Util import getConfig,Req_api
from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from app import db
from app.models import Task
import json,time

api_path = getConfig()['Api']['url']


#更新任务信息
class Update_task(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            token = request.headers["Authorization"]
            current = verify_auth_token(token)
            access_id = int(current.access_id)
            access_key = current.access_key

            id = request.json["id"]
            term = []
            if request.json["terminals"]:
                t =request.json["terminals"].replace("，",",")
                ts = t.split(",")
                for ti in ts:
                    term.append({"i": int(ti)})
            term_to_json = json.dumps(term, ensure_ascii=False)

            update_task = Task.query.get(int(id))
            if update_task:
                update_task.name = request.json["name"]
                update_task.en = request.json["en"]
                update_task.mode = request.json["mode"]
                update_task.pn = request.json["pn"]
                update_task.lv = request.json["lv"]
                update_task.rule = 0
                update_task.vol = request.json["vol"]
                update_task.terminals = term_to_json


                task_time_eb = request.json["eb"].split(':')
                task_time_et = request.json["et"].split(':')
                eb = int(task_time_eb[0]) * 60 * 60 + int(task_time_eb[1]) * 60 + int(task_time_eb[2])
                et = int(task_time_et[0]) * 60 * 60 + int(task_time_et[1]) * 60 + int(task_time_et[2])
                update_task.eb = eb
                update_task.et = et
                update_task.file = request.json["file"] if request.json["file"] else "C:\\Program Files (x86)\\DBBSystem\\DBBServer\\alarm.mp3",

                ip_task = {
                    "id": int(id),
                    "en": int(request.json["en"]),
                    "exe": 0,
                    "name": request.json["name"],
                    "mode": int(request.json["mode"]),
                    "pn": int(request.json["pn"]),
                    "dur": 4294967295,
                    "power": 0,
                    "user": 1,
                    "lv": request.json["lv"],
                    "btime": 4294967295,
                    "rule": 0,
                    "bdate": int(time.time()),  # 默认为添加时间
                    "edate": int(time.time()),  # 仅供测试结束时间为当天
                    "week": 0,
                    "type": 1,
                    "src_type": 0,
                    "em": 52685,
                    "emv": 205,
                    "elm": 52685,
                    "elv": 205,
                    "ei": 0,
                    "echannel": 0,
                    "SchemeID": 0,
                    "prule": 0,
                    "mgr": 52685,
                    "sample": 0,
                    "vioce": 0,
                    "instime": 1,
                    "isins": 0,
                    "ps": 52685,
                    "exec": [
                        {
                            "eb": eb,
                            "et": et,
                            "n": "task_name",
                            "rule": 0
                        }
                    ],
                    "i": 52685,
                    "files": [{
                        "i": 1,
                        "n": request.json["file"] if request.json["file"] else "C:\\Program Files (x86)\\DBBSystem\\DBBServer\\alarm.mp3",
                        "t": 180,
                        "rule": 4319669
                    }],
                    "vol": int(request.json["vol"]),
                    "terminals": term
                }
                data = {"access_id":access_id,"access_key":access_key,"id":int(id),"data":ip_task}
                res = Req_api(api_path+'/update_task',data)
                print(res)
                if res["msg"] == "ok":
                    try:
                        db.session.commit()
                    except:
                        db.session.rollback()
                    return jsonify("ok")
                else:

                    return jsonify("bad")
            else:
                return jsonify("bad")

        except Exception as e:
            print(e.args)
            return jsonify("bad")