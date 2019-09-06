# coding:utf-8
"""
Name: base_user_login.py
User: lvah
Date: 2019-05-11 17：09
Email: 976131979@qq.com
Desc:
	防止黑客暴力破解的用户登录程序

PEP8
"""

# 用户获取密码
import getpass
# 用于密码加密
import base64

# 尝试次数
tryCount = 0
# 加密的密码
dbPassword = b'd2VzdG9z\n'
# 对于加密的密码进行解码成明文字符串;默认返回bytes类型;
dbPassword = base64.decodebytes(dbPassword).decode('utf-8')
# 循环三次
while tryCount < 3:
    tryCount += 1

    # 输入用户名和密码
    name = input("UserName:")
    password = getpass.getpass("Password:")

    # 判断用户名和密码是否正确?
    if name == 'root' and password == dbPassword:
        print("Login Success")
        flag = 1
        break
    else:
        print('Login Fail, you try %d' % (tryCount))
# 如果尝试次数tryCount >= 3时， 执行的语句;(python特有的)
else:
    print("尝试超过三次")
