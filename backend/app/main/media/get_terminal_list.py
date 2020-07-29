# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:25
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: get_terminal_list.py

from flask_restful import Resource,request
from flask import jsonify
from app.main.token import httpauth,verify_auth_token
from Util import Req_api,getConfig
from app import db
from app.models import Media

api_path = getConfig()['Api']['url']

#得到终端列表
class Get_terminal_list(Resource):
    method_decorators = {
        'get':[httpauth.login_required],
        'post':[httpauth.login_required]
    }
    def post(self):
        try:
            update = request.json
            if update:
                # 更新终端
                medialist = Media.query.all()
                for m in medialist:
                    db.session.delete(m)
                db.session.commit()
                mlist = update_media_list()

                for m in mlist:
                    media = Media(
                        id=m["id"],
                        type=m["type"],
                        name=m["name"],
                        status=m["status"],
                        volume=m["volume"],
                        power=m["power"],
                        ip=m["ip"]
                    )
                    db.session.add(media)
                db.session.commit()
                list = []
                for m in medialist:
                    list.append(m.get_media())

                return jsonify(list)

            else:
            # 如果终端是空的就更新一次列表
                medialist = Media.query.all()
                if not medialist:
                    # 如果m不存在就更新终端列表
                    list = update_media_list()
                    for m in list:
                        media = Media(
                            id = m["id"],
                            type = m["type"],
                            name = m["name"],
                            status = m["status"],
                            volume = m["volume"],
                            power = m["power"],
                            ip = m["ip"]
                        )
                        db.session.add(media)
                    db.session.commit()

                    list = []
                    for m in medialist:
                        list.append(m.get_media())

                    return jsonify(list)

                else:
                    list = []
                    for m in medialist:
                        list.append(m.get_media())

                    return jsonify(list)

        except Exception as e:
            print(e.args)
            return jsonify('bad')

# 和广播交互并更新列表的方法
def update_media_list():
    media_list = []
    # 首先清空终端表 或者直接更新？
    try:
        token = request.headers["Authorization"]
        current = verify_auth_token(token)
        access_id = int(current.access_id)
        access_key = current.access_key

        data = {"access_id": access_id, "access_key": access_key}
        res = Req_api(api_path + '/get_terminal_list', data)
        #print('广播返回信息',res)
        for d in res["data"]:
            media_list.append(d)

        return media_list

    except Exception as e:
        print(e.args)
        return media_list