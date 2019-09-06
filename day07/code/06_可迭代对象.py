"""




"""
#
# str = 'hello'
# list = [0, 1, 2, 3, 4]
# set = {1, 2, 3, 4}
# d = dict(a=1, b=2)
#
#
#
# # for i in str:
# #     print(i)
#
#
# # 1). 将字符串转成迭代器(可以调用next方法的对象)
# str_iter = iter(str)
# # print(str_iter)
# # print(type(str_iter))
#
#
# # 2). 可以调用next方法的;
# loop0 = str_iter.__next__()
# print(loop0)
# loop1 = str_iter.__next__()
# print(loop1)
#
#
# # 3). 字符串如何实现for‘循环?
# while True:
#     try:
#         loop = str_iter.__next__()
#         print(loop)
#     except:
#         print("字符串遍历结束")
#         break
#
#
# # 为什么第二次遍历字符串没有内容呢? 因为next方法从上一次停止的地方继续执行,只能向后算；
# str_iter = iter(str)
# while True:
#     try:
#         loop = str_iter.__next__()
#         print(loop)
#     except:
#         print("字符串遍历结束")
#         break




# 4). 如何判断一个对象是不是可迭代对象？
# py2： from collections import Iterable
# py3： from collections.abc import Iterable
from collections.abc import Iterable

print(type('hello') == str)
print(isinstance('hello', str))

print(isinstance(1, Iterable))
print(isinstance('hello', Iterable))

# 文件对象是不是可迭代对象?
with open('./doc/passwd.txt', 'r') as f:
    print(isinstance(f, Iterable))
    # 读取大文件的方式: > 4G
    # enumerate: 枚举, 返回元素索引和元素值
    for number, line in enumerate(f):
        print("第%d行:" %(number+1), line, end='')