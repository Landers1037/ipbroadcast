from app import db
import json

#admin database
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    user = db.Column(db.String(50),unique=True)  # 名字
    password = db.Column(db.String(100),nullable=False)
    access_id = db.Column(db.String(100),default='')
    access_key = db.Column(db.String(100),default='')
    after_pass = db.Column(db.String(100)) #二次加密后的密码使用b64加密
    type = db.Column(db.String(20),nullable=True)
    m = db.Column(db.String(50),nullable=True) #用户全称
    ml = db.Column(db.String(20),nullable=True) #用户权限
    tl = db.Column(db.String(20),nullable=True) #任务级别

    def __init__(self,user,password,after_pass,type,m,ml,tl):
        self.user = user
        self.password = password
        # self.access_id = access_id
        # self.access_key = access_key
        self.after_pass = after_pass
        self.type = type
        self.m = m
        self.ml = ml
        self.tl = tl

    def __repr__(self):
        return '<user {}>'.format(self.user)

    def info(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.user
        data["pw"] = self.password
        data["m"] = self.m
        data["ml"] = self.ml
        data["tl"] = self.tl

        return data

    def access(self):
        data = {}
        data["access_key"] = self.access_key
        data["access_id"] = self.access_id

        return data

# Api追踪的数据表
class Apitrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    login = db.Column(db.Integer)
    user = db.Column(db.Integer)
    media = db.Column(db.Integer)
    task = db.Column(db.Integer)
    sys = db.Column(db.Integer)

    def __init__(self,login,user,media,task,sys):
        self.login = login
        self.user = user
        self.media = media
        self.task = task
        self.sys = sys

    def __repr__(self):
        return '<apitrack immutable>'

# 终端列表数据表
class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True,autoincrement=False)  # 主键
    name = db.Column(db.String(50))  # 名称
    type = db.Column(db.Integer,nullable=False) # 终端类型
    status = db.Column(db.Integer,default=0) # 终端的状态
    volume = db.Column(db.Integer,default=0) # 音量
    defaultvolume = db.Column(db.Integer,default=0) # 默认音量
    power = db.Column(db.Integer,default=0) # 功率大小
    defaultpower = db.Column(db.Integer, default=0)  # 默认功率大小
    ip = db.Column(db.String(20),nullable=False) # IP地址

    def __init__(self,id,name,type,status,volume,power,ip):
        self.id = id
        self.name = name
        self.type = type
        self.status = status
        self.volume = volume
        self.power = power
        self.ip = ip

    def __repr__(self):

        return '<media {}>'.format(self.name)

    def get_media(self):
        data = {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "status": self.status,
            "volume": self.volume,
            "power": self.power,
            "ip": self.ip
        }
        return data


# 任务数据表
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True,autoincrement=False)  #  id主键
    name = db.Column(db.String(50),unique=True)  # 名称
    en = db.Column(db.Integer,default=0) # 任务是否可用
    exe = db.Column(db.Integer, default=0)  # 任务状态
    mode = db.Column(db.Integer,default=0) #任务广播方式
    pn = db.Column(db.Integer,default=1) #任务播放次数
    lv = db.Column(db.Integer,default=100) #任务优先级11-100
    rule = db.Column(db.Integer,default=0) #任务执行规则每天0 每周1
    type = 1 #只能是定时任务
    vol = db.Column(db.Integer,default=-1) #任务默认音量-1为不指定
    terminals = db.Column(db.TEXT,nullable=True) #指定可以使用的终端,解决低版本mysql没有json类型的问题
    file = db.Column(db.String(100))
    bdate = db.Column(db.Integer,nullable=True) #开始日期
    edate = db.Column(db.Integer,nullable=True) #结束日期
    eb = db.Column(db.Integer) #开始时间
    et = db.Column(db.Integer) #结束时间
    run = db.Column(db.Integer,default=0) #执行状态

    def __repr__(self):
        return '<task {}>'.format(self.name)

    def get_task(self):
        data = {
            "id": self.id,
            "name": self.name,
            "en": self.en,
            "exe": self.exe,
            "mode": self.mode,
            "pn": self.pn,
            "lv": self.lv,
            "rule": self.rule,
            "type": self.type,
            "terminals": json.loads(self.terminals,encoding='utf-8'),
            "file": self.file,
            "bdate": self.bdate,
            "edate": self.edate,
            "eb": self.eb,
            "et": self.et,
            "run": self.run
        }

        return data
