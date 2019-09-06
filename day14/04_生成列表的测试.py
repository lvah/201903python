def list_create1():
    """通过连接操作符创建"""
    li = []
    for i in range(0, 1000):
        li = li + [i]


def list_create2():
    """通过append方法"""
    li = []
    for i in range(0, 1000):
        li.append(i)


def list_create3():
    """通过列表生成式创建"""
    li = [i for i in range(1000)]


def list_create4():
    """range创建"""
    list(range(1000))



if __name__ == '__main__':
    import timeit
    t1 = timeit.Timer('list_create1()',"from __main__ import list_create1 ")
    print(t1.timeit(number=1000))
    t2 = timeit.Timer('list_create2()',"from __main__ import list_create2 ")
    print(t2.timeit(number=1000))
    t3 = timeit.Timer('list_create3()',"from __main__ import list_create3 ")
    print(t3.timeit(number=1000))
    t4 = timeit.Timer('list_create4()',"from __main__ import list_create4 ")
    print(t4.timeit(number=1000))
