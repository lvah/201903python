"""
1. 生成器  --(都是)--->     迭代器(next)  ----(都是)---> <--(不一定是iter)----     可迭代对象(for)
2. 闭包: 1). 2). 3).
        def line_conf(a, b):
            def line(n):
                return a*n+b
            return line


3. 装饰器------
def decorate(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        # 返回被装饰函数的返回值;
        return result
    return wrapper
@decorate    ===> add=decorate(add)  ---> add指向wrapper函数位置
def add():
    return 'ok'

add()

"""