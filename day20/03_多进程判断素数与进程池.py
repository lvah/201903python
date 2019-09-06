def is_prime(num):
    """判断素数"""
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def task(num):
    if is_prime(num):
        print("%d是素数" % (num))


from multiprocessing import Process


# 判断1000-1200之间所有的素数
def use_mutli():
    ps = []
    # 不要开启太多进程， 创建子进程会耗费时间和空间(内存);
    for num in range(1, 10000):
        # 实例化子进程对象
        p = Process(target=task, args=(num,))
        # 开启子进程
        p.start()
        # 存储所有的子进程对象
        ps.append(p)

    # 阻塞子进程， 等待所有的子进程执行结束， 再执行主进程;
    [p.join() for p in ps]


# 判断1000-1200之间所有的素数
def no_mutli():
    for num in range(1, 100000):
        task(num)

def use_pool():
    """使用进程池"""
    from multiprocessing import Pool
    from multiprocessing import  cpu_count  # 4个
    p = Pool(cpu_count())
    p.map(task, list(range(1, 100000)))
    p.close()  # 关闭进程池
    p.join()  # 阻塞， 等待所有的子进程执行结束， 再执行主进程;

if __name__ == '__main__':
    import time

    start_time = time.time()
    # 数据量大小          # 1000-1200             # 1-10000                 # 1-100000
    # no_mutli()        # 0.0077722072601       # 1.7887046337127686      # 90.75180315971375
    # use_mutli()       # 1.806459665298462
    use_pool()          # 0.15455389022827148   # 1.2682361602783203      # 35.63375639915466
    end_time = time.time()
    print(end_time - start_time)
