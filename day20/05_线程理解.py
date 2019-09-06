import threading

if __name__ == '__main__':
    # 一个进程里面一定有一个线程， 叫主线程.
    print("当前线程个数:", threading.active_count())
    print("当前线程信息:", threading.current_thread())