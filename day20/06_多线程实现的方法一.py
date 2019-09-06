"""
通过实例化对象的方式实现多线程
"""
import time
import threading
def task():
    """当前要执行的任务"""
    print("听音乐........")
    time.sleep(1)

if __name__ == '__main__':
    start_time = time.time()
    threads = []
    for  count in range(5):
        t = threading.Thread(target=task)
        # 让线程开始执行任务
        t.start()
        threads.append(t)

    # 等待所有的子线程执行结束， 再执行主线程;
    [thread.join() for thread in threads]
    end_time = time.time()
    print(end_time-start_time)








