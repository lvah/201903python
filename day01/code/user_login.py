#coding:utf-8
import getpass

# 尝试次数
tryCount = 0

# 循环三次
while tryCount < 3:
	tryCount += 1 

	# 输入用户名和密码
	name = input("UserName:")
	password = getpass.getpass("Password:")

	# 判断用户名和密码是否正确?
	if name=='root' and password=='westos':
		print("Login Success")
		flag = 1
		break
	else:
		print('Login Fail, you try %d' %(tryCount))
# 如果尝试次数tryCount >= 3时， 执行的语句;(python特有的)
else:
	print("尝试超过三次")





