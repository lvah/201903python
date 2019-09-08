# 获取当前绝对路径
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI: 用于连接数据的数据库。
# sqlite:////home/kiosk/Desktop/201905python/day36-1/01_Flask与数据库操作的整合/data.sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#  sqlchemy将会追踪对象的修改并且发送信号
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 每次请求结束之后都会提交数据库的变动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True