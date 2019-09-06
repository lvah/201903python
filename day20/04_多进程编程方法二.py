"""
创建子类， 继承的方式
"""
from multiprocessing import  Process
import time
class MyProcess(Process):
    """
    创建自己的进程， 父类是Process
    """
    def __init__(self, music_name):
        super(MyProcess, self).__init__()
        self.music_name = music_name

    def run(self):
        """重写run方法， 内容是你要执行的任务"""

        print("听音乐%s" %(self.music_name))
        time.sleep(1)

# 开启进程： p.start()  ====== p.run()
if __name__ == '__main__':
    for i in range(10):
        p = MyProcess("音乐%d" %(i))
        p.start()
        