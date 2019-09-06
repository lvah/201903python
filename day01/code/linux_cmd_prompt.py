#encoding:utf-8
import os

while True:
	cmd = input("[命令行提示符]>> ")
	if cmd == 'quit':
		print("正在退出程序......")
		# 跳出循环， 程序结束;
		break
	else:
		print("%s命令的执行结果:" %(cmd))
		# 执行linux命令的方法
		os.system(cmd)
		# os.popen


