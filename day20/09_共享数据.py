money = 0


def add():
    for i in range(1000000):
        global money
        lock.acquire()
        money += 1
        lock.release()
def reduce():
    for i in range(1000000):
        global money
        lock.acquire()
        money -= 1
        lock.release()
if __name__ == '__main__':
          from threading import  Thread, Lock
          # 创建线程锁
          lock = Lock()
          t1 = Thread(target=add)
          t2 = Thread(target=reduce)
          t1.start()
          t2.start()
          t1.join()
          t2.join()
          print(money)