"""
不同开发环境配置

"""
from Util import getConfig
import os

__author__ = "Landers/liaorenj@gmail.com"
__prj__ = "NMS"

SECRET_KEY = getConfig()['Server']['secret_key']
SQLALCHEMY_DATABASE_URI = getConfig()['Server']['db']
USER = getConfig()['Server']['dbuser']
PASS = getConfig()['Server']['dbpass']
ADDRESS = getConfig()['Server']['dbaddress']
PORT = getConfig()['Server']['dbport']
DATABASE = getConfig()['Server']['dbbase']

class ProductionConfig():
    DEBUG = False
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USER,PASS,ADDRESS,PORT,DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig():
    DEBUG = True
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.getcwd()+"/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False

class TestingConfig():
    DEBUG = True