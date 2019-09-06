"""
多进程中，每个进程中所有数据（包括全局变量）都各有拥有⼀份，互 不影响
"""


import os
import time

# 定义一个全局变量money
money = 100
print("当前进程的pid:", os.getpid())
print("当前进程的父进程pid:", os.getppid())
# time.sleep(115)


p = os.fork()
# 子进程返回的是0
if p == 0:
    money = 200
    print("子进程返回的信息, money=%d" %(money))
# 父进程返回的是子进程的pid
else:
    print("创建子进程%s, 父进程是%d" %(p,  os.getppid()))
    print(money)





