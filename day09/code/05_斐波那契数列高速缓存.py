"""

1, 1, 2, 3, 5, 8......
F(n) = F(n-1) + F(n-2)
"""
import os
import time


def timmer(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        print("%s run %.5f" % (fun.__name__, end_time - start_time))
        # wrapper需要返回的是被装饰函数的返回值；
        return result

    return wrapper


def num_cache(fun):
    """
    添加高速缓存的装饰器 num_cache
    如果第一次计算 F(5) = F(4) + F(3) = 5
    第二次计算 F(6) = F(5) + F(4)
    显然 F(5)已经计算过了, F(4)也已经计算了, 我们可否添加一个装饰器, 专门用
    来存储 费波那契数列已经计算过的缓存, 后期计算时, 判断缓存中是否已经计算过了, 如
    果计算过,直接用缓存中的计算结果. 如果没有计算过, 则开始计算并将计算的结果保存在缓存中
    :param fun:
    :return:
    """
    import json
    # 如果放到内部函数里面， 每次执行会clear
    # 读取缓存文件中的缓存;
    cache_filename = 'cache.txt'
    if os.path.exists(cache_filename):
        with open(cache_filename) as f:
            try:
                cache = json.load(f)
                # print(cache)
            except:
                cache = {}
    # else:
        # Linux创建文件, Windows不支持该方法。 f = open(filename, 'w')   f.close()
        # os.mknod(cache_filename)

    def wrapper(num):

        if num in cache:
            result = cache.get(num)
            return result
        else:
            # 如果求的num不在缓存里面， 手动求Fib结果
            result = fun(num)
            # 将求出来的结果存储到缓存中;
            cache[num] = result
            return result
    return wrapper


@num_cache
def fib(num):
    if num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


@timmer
def fun1():
    result = fib(200)
    print('F(200)=', result)


@timmer
def fun2():
    result = fib(109)
    print('F(109)=', result)


fun1()
fun2()
