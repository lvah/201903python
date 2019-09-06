MAIL_SERVER = 'smtp.qq.com'
# 指定端口， 默认25， 但qq邮箱默认为 端口号465或587；
MAIL_PORT = 465

"""
由于QQ邮箱不支持非加密的协议，那么使用加密协议, 分为两种加密协议，选择其中之一即可
"""
MAIL_USE_SSL = True
MAIL_USERNAME = '976131979'
# 此处的密码并非邮箱登录密码， 而是开启pop3
MAIL_PASSWORD = "sdjuoeyoxjoubedb"
# 条是模式打开
DEBUG = True
SECRET_KEY = 'westos'