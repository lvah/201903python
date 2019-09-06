"""

# *****************一定要熟记**************
def decorator(fun):
    def wrapper(*args, **kwargs):  # args, kwargs是形参
        # 在函数之前做的操作
        res = fun(*args, **kwargs)       # *args, **kwargs是实参, *args, **kwargs是在解包
        # 在函数之后添加操作
        return res
    return wrapper



@装饰器的名字
@add_log     ======> add=add_log(add)
def add():
    pass


add()

"""