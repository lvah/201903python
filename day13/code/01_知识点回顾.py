"""
property属性:
    1. 对象的属性只允许查看， 不允许修改时， 建议使用;
    2. 对象的属性可以修改(setter)， 但不能随便修改;
@classmethod:
@staticmethod
"""

from datetime import date
# from  datetime import  time
import time
class Date(object):

    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return '%s-%s-%s' % (self.__year, self.__month, self.__day)

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    @month.setter
    def month(self, item):
        if 0 < item <= 12:
            self.__month = item
        else:
            raise Exception("月份%s错误" % (item))

    @classmethod
    def fromtimestamp(cls, t):
        """根据时间戳获取日期"""
        t = time.localtime(t)
        year, month, day = t.tm_year, t.tm_mon, t.tm_mday
        return cls(year, month, day)

    def replace(self, year=None, month=None, day=None):
        """返回的是一个对象"""
        # 修改年/月/日
        if year is None:
            year = self.__year
        if month is None:
            month = self.__month
        if day is None:
            day = self.__day
        # type(self), 返回的是self对象的类名
        return type(self)(year, month, day)


d = Date.fromtimestamp(time.time())
print(d)

# print(d.year)
# d.year=2020
# print(d.year)


# 测试修改年/月/日
d1 = d.replace(month=12, day=1)
print(d)
print(d1)

# setter装饰器， 可以实现对月份的修改
d.month = 12
print(d)

# class Counter(object):
#     @property
#     def count1(self):
#         pass
#
#
#     def most_common(self):
#         pass
#
#     @classmethod
#     def fun1(cls):
#         pass
#
#
#     @staticmethod
#     def fun2():
#         pass
