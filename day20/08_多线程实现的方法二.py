"""
创建子类
"""


from threading import  Thread
class GetHostAliveThread(Thread):
    """
    创建子线程， 执行的任务：判断指定的IP是否存活
    """
    def __init__(self, ip):
        super(GetHostAliveThread, self).__init__()
        self.ip = ip
    def run(self):
        # # 重写run方法: 判断指定的IP是否存活
        # """
        # >>> # os.system()  返回值如果为0， 代表命令正确执行，没有报错; 如果不为0， 执行报错;
        # ...
        # >>> os.system('ping -c1 -w1 172.25.254.49 &> /dev/null')
        # 0
        # >>> os.system('ping -c1 -w1 172.25.254.1 &> /dev/null')
        # 256
        # """
        import os
        # 需要执行的shell命令
        cmd = 'ping -c1 -w1 %s &> /dev/null' %(self.ip)
        result = os.system(cmd)
        #  返回值如果为0， 代表命令正确执行，没有报错; 如果不为0， 执行报错;
        if result != 0:
            print("%s主机没有ping通" %(self.ip))
if __name__ == '__main__':
    print("打印172.25.254.0网段没有使用的IP地址".center(50, '*'))
    for i in range(1, 255):
        ip = '172.25.254.' + str(i)
        thread = GetHostAliveThread(ip)
        thread.start()
