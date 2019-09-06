"""

Python中至少有三种比较常见的方法类型，即实例方法，类方法、静态方法。它们是如何定义的呢？
如何调用的呢？它们又有何区别和作用呢？

首先，这三种方法都定义在类中。
实例方法
    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    调用：只能由实例对象调用。

类方法
    定义：使用装饰器@classmethod。第一个参数必须是当前类，该参数名一般约定为“cls”class的缩写，
         通过它来传递类的属性和方法（不能传实例的属性和方法）；
    调用：实例对象和类对象都可以调用。

静态方法
    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    调用：实例对象和类对象都可以调用。


# 源代码:
    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        y, m, d = _ord2ymd(n)
        return cls(y, m, d)
"""

# 查看时间的模块
import  time
print(time.time())  # 返回的是时间戳1560671036.7327375
print(time.ctime())  # 返回字符串的时间Sun Jun 16 15:43:56 2019
print(time.localtime()) # 返回的是一个命名元组
time_tuple = time.localtime()
print(time_tuple.tm_year)



# 查看时间的模块
from datetime import  date
from datetime import  time
from datetime import  datetime
from datetime import  timedelta

class Student(object):
    def __init__(self, name):
        self.name = name
    # 实例方法： 函数默认传递一个参数， self==对象本身(实例)
    def get_name(self):
        return  self.name










