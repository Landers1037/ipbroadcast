"""
华中科技大学
毕业设计：智能IP广播系统设计
指导老师：罗杰
设计者：廖仁杰 U201613543
在线文档：http://mgek.cc/app/ipbroadcast
Github仓库：https://github.com/landers1037/nms
时间：2019年12月23日

author: Landers
email: liaorenj@gmail.com
school: Huazhong University of S&T
github: https://github.com/landers1037/nms
"""

import yaml,json
import requests,base64,psutil

def getConfig():
    file = open('config.yaml','r',encoding='utf-8')
    configs = file.read()
    loader = yaml.load(configs,Loader=yaml.FullLoader)

    return loader

def Req_api(url,data):
    try:
        Poster = requests.post(url=url,json=data)
        result = Poster.json()
        Poster.close()
        return result
    #添加状态码判断，离线时返回统一的返回码做判断
    except:
        return {"msg": "offline"}

def Second_encrypt(code):
    en_code = base64.b64encode(code.encode('utf-8'))
    r = en_code.decode('utf-8')
    return r

def Second_decode(code):
    decode = base64.b64decode(code.encode('utf-8'))
    r = decode.decode('utf-8')
    return r


def Get_mem(exe):
    mem = psutil.virtual_memory().percent
    pids = psutil.pids()
    exe_mem = 0
    try:
        for pid in pids:
            p = psutil.Process(pid)
            if exe in p.name():
                exe_mem = exe_mem + p.memory_percent()

        exe_mem = int(exe_mem*mem)
        return exe_mem

    except:
        return 0

def Get_sys():
    #监视系统状态
    sys_cpu = psutil.cpu_percent(interval=1)
    sys_mem = psutil.virtual_memory().percent
    py_mem = Get_mem('python')
    sys_status = ["系统cpu占用: "+str(sys_cpu)+'%',"系统内存占用: "+str(sys_mem)+'%',"后端服务占用: "+str(py_mem)+'%']
    return sys_status

def Get_copy():
    Con = getConfig()
    author = Con['Copyright']['author']
    usercode = Con['Copyright']['usercode']
    school = Con['Copyright']['school']
    github = Con['Copyright']['github']
    email = Con['Copyright']['email']

    copydata = ['作者: '+author,'学号: '+usercode,'学校: '+school,'Github: '+github,'邮箱: '+email]
    return copydata


# print(Second_encrypt('Landers HUST final project'))
# print(Get_mem())
# print(Get_sys())