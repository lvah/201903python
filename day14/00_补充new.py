# class Student(object):
#     # new方法和init方法的区别
#     #   new：python解释器默认会传递cls, 必须返回一个对象
#     def __new__(cls):
#         print('new')
#         return  object.__new__(cls)
#
#     def __init__(self):
#         print("init")
#
#
#
# s = Student()
from datetime import  date
d = date.today()
d.country = 'china'
print(d.country)