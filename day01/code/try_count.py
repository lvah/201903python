#!/home/kiosk/anaconda3/bin/python
#encoding:utf-8

"""
循环语句


%f: 浮点型
%d: 整型
"""
tryCount = 0

while tryCount < 3:   # 0, 1, 2, 3
	name = input("用户名:")
	tryCount += 1
	print("登录第%d次" %(tryCount))


print("已经登录3次， 请稍后再试！！")
