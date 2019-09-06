"""


总结：
    1). Python内置的@property装饰器就是负责把一个方法变成属性调用的;
    2). @property本身又创建了另一个装饰器@state.setter，负责把一个
        setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作.
    3). @property广泛应用在类的定义中，可以让调用者写出简短的代码，
        同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

源代码应用范例: 让属性只读：
    from datetime import  date

    # Read-only field accessors
    @property
    def year(self):
        # year (1-9999)
        return self._year

    @property
    def month(self):
        # month (1-12)
        return self._month

    @property
    def day(self):
        # day (1-31)
        return self._day


from datetime import  date

# 获取当前的日期， 直接打印对象名， 返回的是年-月-日
d1 = date.today()
# print(d1)

# date类里面有三个方法: year(), month(), day()
print(d1.year)
print(d1.month)
print(d1.day)

"""

import time


class Date(object):
    def __init__(self, year=None, month=None, day=None):
        self.__year = year
        self.__month = month
        self.__day = day

    @property # 类属性, 获取属性名时简洁: 对象名.属性名
    def month(self):
        if 0 < self.__month <= 12:
            return self.__month

    @month.setter # 设置属性装饰器， 当设置属性时简洁： 对象名.属性名=新的值
    def month(self, month):
        if 0 < self.__month <= 12:
            self.__month = month
            return  True

    @month.deleter # 删除属性装饰器， 当删除属性时简洁： del 对象名.属性名
    def month(self):
        del self.__month


d = Date(2019, 10, 10)


print(d.month)
d.month = 12
print("正在修改月份....")
print(d.month)

del d.month
print("正在删除月份....")
print(d.month)




# 不简洁的方式： 不太建议
# # 获取月份====print(d.month)
# print(d.month())
#
# # 设置月份======d.month = 12
# d.set_month(12)
# print(d.month())
#
# # 删除月份信息 ===== del d
# d.del_year()
# print("正在删除月份信息.....")
# print(d.month())
