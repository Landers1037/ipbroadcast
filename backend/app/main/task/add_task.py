# -*- coding: utf-8 -*-
# Time: 2020-03-31 20:05
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: add_task.py
from Util import getConfig,Req_api
from flask_restful import Resource,request
from app.main.token import httpauth,verify_auth_token
from flask import jsonify
from app import db
from app.models import Task
import json,time

api_path = getConfig()['Api']['url']


#添加定时任务
class Add_task(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            task_data = request.json
            token = request.headers["Authorization"]
            current = verify_auth_token(token)
            access_id = int(current.access_id)
            access_key = current.access_key

            term = []
            if task_data["terminals"]:
                t =task_data["terminals"].replace("，",",")
                ts = t.split(",")
                for ti in ts:
                    term.append({"i": int(ti)})

            term_to_json = json.dumps(term,ensure_ascii=False)
            # 由于添加任务的特殊性，由广播返回的ID最终提交记录

            if task_data["eb"] and task_data["et"]:
                task_time_eb = task_data["eb"].split(':')
                task_time_et = task_data["et"].split(':')
                eb = int(task_time_eb[0])*60*60 + int(task_time_eb[1])*60 + int(task_time_eb[2])
                et = int(task_time_et[0])*60*60 + int(task_time_et[1])*60 + int(task_time_et[2])
            else:
                local = time.localtime(time.time())
                now = time.strftime('%H:%M:%S', local).split(':')
                eb = int(now[0])*60*60 + int(now[1])*60 + int(now[2])
                et = eb

            ip_task = {
                "id": 0,
                "en": int(request.json["en"]),
                "exe": 0,
                "name": request.json["name"],
                "mode": 0,
                "pn": int(request.json["pn"]),
                "dur": 4294967295,
                "power": 0,
                "user": 1,
                "lv": 11,
                "btime": 4294967295,
                "rule": 0,
                "bdate": int(time.time()), #默认为添加时间
                "edate": int(time.time()), #仅供测试结束时间为当天
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
                    "n": task_data["file"] if task_data["file"] else "C:\\Program Files (x86)\\DBBSystem\\DBBServer\\alarm.mp3",
                    "t": 180,
                    "rule": 4319669
                }],
                "vol": int(request.json["vol"]),
                "terminals": term
            }
            data = {"access_id":access_id,"access_key":access_key,"data":ip_task}
            res = Req_api(api_path+'/add_task',data)
            if res["msg"] == 'ok':
                #完成数据库的提交工作
                id = int(res["id"])
                task = Task(
                    id=id,
                    name=task_data["name"],
                    en=int(task_data["en"]),
                    exe=0,
                    mode=int(task_data["mode"]),
                    pn=int(task_data["pn"]),
                    lv=int(task_data["lv"]),
                    rule=0,
                    type=1,
                    vol=int(task_data["vol"]),
                    terminals=term_to_json,
                    #额外参数
                    file=task_data["file"] if task_data["file"] else "C:\\Program Files (x86)\\DBBSystem\\DBBServer\\alarm.mp3",
                    bdate=int(time.time()),
                    edate=int(time.time()),
                    eb=task_data["eb"], #开始时间
                    et=task_data["et"], #结束时间
                    run=0
                )
                db.session.add(task)
                db.session.commit()

                return jsonify('ok')
            else:

                db.session.rollback()
                return jsonify('bad')

        except Exception as e:
            print(e.args)
            return jsonify('bad')