# -*- coding: utf-8 -*-
# Time: 2020-03-31 19:20
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: api_log.py
from app.models import Apitrack
from app import db
from Util import getConfig


def api_log(file):
    def check_api(func):
        def api_logging(*args,**kwargs):
            if_apilog = getConfig()['Log']['apilog']
            if if_apilog:
                try:
                    if 'auth_unit' in file:
                        this = Apitrack.query.get(1)
                        this.login = this.login + 1
                        db.session.commit()
                    elif 'user_unit' in file:
                        this = Apitrack.query.get(1)
                        this.user = this.user + 1
                        db.session.commit()
                    elif 'media_unit' in file:
                        this = Apitrack.query.get(1)
                        this.media = this.media + 1
                        db.session.commit()
                    elif 'task_unit' in file:
                        this = Apitrack.query.get(1)
                        this.task = this.task + 1
                        db.session.commit()
                    elif 'sys_unit' in file:
                        this = Apitrack.query.get(1)
                        this.sys = this.sys + 1
                        db.session.commit()
                    else:
                        pass
                except Exception as e:
                    pass
            else:
                pass
            return func(*args,**kwargs)

        return api_logging

    return check_api