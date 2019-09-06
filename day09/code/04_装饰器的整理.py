"""
1. 闭包：
满足三个条件:
    1). 函数里面嵌套函数
    2). 内部函数调用外部函数的变量;
    3). 外部函数返回内部函数的引用

2. 装饰器
1). 为什么使用装饰器?
有一些场景， 需要频繁更改逻辑， 但是遵循开放封闭原则,
1). 快速的在不改变原有函数的基础上， 添加逻辑信息;
2). 不改变函数的调用方式;

2). 装饰器的语法
装饰器的语法糖: @装饰器名称
@add_info     # add=add_info(add)
def login():
    print('login')

3). 装饰器装饰不同的函数(传递的参数不同)
def desc(fun):
    def wrapper(*args, **kwargs):
        fun(*args, **kwargs)
    return wrapper


4). 装饰器装饰的是有返回值的函数
def desc(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result
    return wrapper


5). 多个装饰器
    5-1). 装饰时， 由下到上；
    5-2). 调用时： 由上到下

6). 带参数的装饰器    




"""