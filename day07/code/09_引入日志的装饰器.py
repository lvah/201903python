import os
import time
import  sys
# 装饰器: 用来添加日志信息的
def add_log(fun):
    """
    May 26 09:50:14 foundation0 systemd: Removed slice user-0.slice.*args
ar
    """
    def wrapper(*args, **kwargs):  # args=(1, 2) =====> *args=1 2    #
        # 获取被装饰的函数的返回值
        result = fun(*args, **kwargs)      # add(*args)    ====> add(1, 2)
        # 返回当前的字符串格式时间
        now_time = time.ctime()
        # 获取主机名 nodename='foundation0.ilt.example.com'
        hostname = os.uname().nodename.split('.')[0]
        # 运行的程序
        process_full_name = sys.argv[0]
        process_name = os.path.split(process_full_name)[-1]
        # 日志内容
        # info = "正在运行程序: " + str(fun)
        # 获取函数名: 函数名.__name__
        info ="函数[%s]的运行结果为%s" %(fun.__name__, result)
        log = " ".join([now_time, hostname, process_name, info])
        print(log)
        return  result
    return  wrapper

@add_log  # 语法糖====music = add_log(music)
def music():
    time.sleep(1)
    print("正在听音乐.....")

@add_log
def add(x, y):
    return  x+y

@add_log
def roll(name, age, **kwargs):
    print(name, age, kwargs)

# res =add(1, 2)
# print(res)
# music()


roll(name='fentiao', age=10, province='陕西', gender='男')