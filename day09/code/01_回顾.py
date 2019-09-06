"""
# 装饰器

1. 闭包：
满足三个条件:
    1). 函数里面嵌套函数
    2). 内部函数调用外部函数的变量;
    3). 外部函数返回内部函数的引用

    def line_conf(a, b):
        def line(num):
            return a * num + b
        return line

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



*****案例代码
def add_info(fun):
    def wrapper():
        print('高考顺利')
        fun()
        print("欢迎再来")
    return  wrapper
@add_info     # add=add_info(add)
def login():
    print('login')
@add_info   # logout = add_info(logout)
def logout():
    print('logout')

# login = add_info(login)   # login = wrapper
# login()                   # login()
#
# logout = add_info(logout)
# logout()
# 此处省略1000个函数


#
# login()
# logout()


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


******案例代码:
import  time

def desc(fun):
    def wrapper(*args, **kwargs):    # *args， **kwargs ===形参   ===> args(元组)， kwargs(字典)
        start_time = time.time()
        fun(*args, **kwargs)         #  *args， **kwargs === 实参   ====>   *args, **kwargs解包
        end_time = time.time()
        print('run %s' %(end_time-start_time))
    return  wrapper

# # ************当调用被装饰的函数时， 实质上执行的是装饰器内部的函数;
# @desc     # fun1=desc(fun1)  ===> fun1 = wrapper
# def fun1():
#     print("没有参数的函数装饰")
#
# fun1()    # wrapper()
@desc
def fun2(a, b=2):
    print("有必选参数的函数:", a+b)
fun2(1, 3)   # wrapper()



"""



import  time
def desc(fun):
    def wrapper(*args, **kwargs):    # *args， **kwargs ===形参   ===> args(元组)， kwargs(字典)
        start_time = time.time()
        fun( *args,**kwargs)         #  *args， **kwargs === 实参   ====>   *args, **kwargs解包
        end_time = time.time()
        print('run %s' %(end_time-start_time))
    return  wrapper

@desc   # roll=desc(roll)     # roll = wrapper
def roll(name, age, country='china', **kwargs):
    print(name, age, country, kwargs)

roll("粉条", 10, 'china', province="陕西")


# 1). @desc: roll = desc(roll)   ====> roll = wrapper
# 2). roll("粉条", 10, 'china', province="陕西")   ====> wrapper("粉条", 10, 'china', province="陕西")
#     args = ("粉条", 10, 'china')   kwargs={'province': '陕西'}
# 3). 开始时间计算
# 4). *args =>  "粉条"  10  'china'   **kwargs => province "陕西"
#     roll("粉条", 10, 'china', province="陕西")
# 5). 计算结束时间
# 6). 打印运行时间




