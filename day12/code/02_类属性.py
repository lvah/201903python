from collections import Counter


class A(object):
    pass


class C(object):
    pass


class Date(A, C):
    """
    时间类的封装
    """
    country = 'china'

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # def __dir__(self):
    #     return  {'country': self.country}


print(Date.__name__)

# 类定义所在的模块, 如果在当前脚本， 返回__main__, 否则， 返回真实的模块名eg: collections
print(Date.__module__)
print(Counter.__module__)

# 对象或类所属的类: 是由哪个类实例化出来的；
d = Date(2019, 10, 10)
print(d.__class__)  # d对象是由Date类实例化出来的；
print(Date.__class__)  # type(1)Date类是由type类实例化出来的；  Python中一切皆对象； 看到的类实质上也是对象；

# 当前类的基类(父类)
print(Date.__bases__)
print(A.__bases__)
print(object.__bases__)  # object没有父类;

# 类、函数的文档帮助，没有定义为None
print(Counter.__doc__)
print(Date.__doc__)

# Method Resolution Order 方法解析顺序, 实质上是显示类的继承顺序; python3中多继承的算法是广度优先
print(Date.__mro__)
# 类或实例的属性，可写的字典
print(Date.__dict__)

# dir
print(dir(Date))

print(dir())


def add(x, y):
    print(dir())
    return x + y

add(1, 2)
