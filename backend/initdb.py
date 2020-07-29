# -*- coding: utf-8 -*-
# Time: 2020-04-20 19:15
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: initdb.py

import requests
from Util import getConfig

port = getConfig()['Server']['port']

if __name__ == '__main__':
    try:
        res = requests.post('http://127.0.0.1:{}/test/initdb'.format(port))
        print(res.json())

    except:
        print('failed to init database\nplease ensure that app is running\n')