"""

在线程间共享多个资源的时候，如果两个线程分别占有⼀部分资源并且同时 等待对⽅的资源，就会造成死锁。


"""

import time
import threading


class Account(object):
    def __init__(self, id, money, lock):
        self.id = id
        self.money = money
        self.lock = lock

    def reduce(self, money):
        self.money -= money

    def add(self, money):
        self.money += money


def transfer(_from, to, money):
    if _from.lock.acquire():
        _from.reduce(money)

        time.sleep(1)
        if to.lock.acquire():
            to.add(money)
            to.lock.release()
        _from.lock.release()


if __name__ == '__main__':
    a = Account('a', 1000, threading.Lock())  # 900
    b = Account('b', 1000, threading.Lock())  # 1100

    t1 = threading.Thread(target=transfer, args=(a, b, 200))
    t2 = threading.Thread(target=transfer, args=(b, a, 100))
    t1.start()
    t2.start()
    print(a.money)
    print(b.money)
