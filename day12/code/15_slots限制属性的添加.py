from collections import  Counter



class MyCounter(object):
    # 限制属性的添加, 只能添加count和age;
    __slots__ = ('count', 'a')



print(hasattr(MyCounter, 'a'))

counter = MyCounter()
counter.a = 1
print(counter.a)
# counter.b = 2
# print(counter.b)

