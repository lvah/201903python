"""
Process([group [, target [, name [, args [, kwargs]]]]])
	target：表示这个进程实例所调⽤对象；
	args：表示调⽤对象的位置参数元组；
	kwargs：表示调⽤对象的关键字参数字典；
	name：为当前进程实例的别名；
	group：⼤多数情况下⽤不到；


Process类常⽤⽅法：
	is_alive()：	判断进程实例是否还在执⾏；
	join([timeout])：	是否等待进程实例执⾏结束，或等待多少秒；
	start()：		启动进程实例（创建⼦进程）；
	run()：		如果没有给定target参数，对这个对象调⽤start()⽅法时，
	           		就将执 ⾏对象中的run()⽅法；
	terminate()：	不管任务是否完成，⽴即终⽌；

"""

from multiprocessing import Process
import time


def task1():
    print("正在听音乐")
    time.sleep(1)


def task2():
    print("正在编程......")
    time.sleep(0.5)


def no_multi():
    task1()
    task2()

def use_multi():
    p1 = Process(target=task1)
    p2 = Process(target=task2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # p.join()  阻塞当前进程， 当p1.start()之后， p1就提示主进程， 需要等待p1进程执行结束才能向下执行， 那么主进程就乖乖等着， 自然不会执行p2.start()
    # [process.join() for process in processes]

if __name__ == '__main__':
    # 主进程
    start_time= time.time()
    # no_multi()
    use_multi()
    end_time = time.time()
    print(end_time-start_time)