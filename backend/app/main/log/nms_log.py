'''
log日志记录模块
用于记载服务器运行时出现的错误并且写入到本地日志里
'''

import time,os,sys
import json
from Util import getConfig
from functools import wraps
from flask import request
import logging


logpath = getConfig()['Log']['logpath']  #log文件路径

#初始化logger
logger = logging.getLogger('func_log')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(logpath+'nms.log',encoding='utf-8')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][%(levelname)s] --> %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def gettime():
    #时间校准函数
    t = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime())
    return t

def addlog(data):
    #日志记录模块
    with open(logpath+'nms.log','a',encoding='utf-8') as f:
        f.write(gettime() + "\n")
        f.write(data + "\n")

        f.close()

def dellog():
    #删除日志
    # os.remove(logpath+'nms.log')
    with open(logpath + 'nms.log','w',encoding='utf-8')as f:
        f.write('')
        f.close()

def backup():
    #备份日志
    back_time = time.strftime('%Y-%m-%d',time.localtime())
    print(back_time)
    with open(logpath + 'nms.log','r',encoding='utf-8')as f:
        data = f.read()
        with open(logpath + 'nms-{}.log'.format(back_time),'w',encoding='utf-8')as bf:
            bf.write(data)
            bf.close()
        f.close()



def request_url():
    url = request.url
    r_data = request.data.decode('utf-8')
    try:
        token = request.headers["Authorization"]
    except:
        token = "no token yet"
    data = "请求地址: " + url + '\n' + "请求数据: " +json.dumps(r_data) +  "\n" + "用户令牌: " + token + "\n"
    return data

def nms_log(func):
    @wraps(func)
    def logging(*args,**kwargs):
        iflog = getConfig()['Log']['logger']  # 是否开启log
        if iflog:
            logger.debug("方式:"+func.__name__+ "@"+request_url())
            return func(*args,**kwargs)
        else:
            return func(*args,**kwargs)
    return logging


