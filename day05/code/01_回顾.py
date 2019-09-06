"""
# python内置的数据结构:
    数值: int, （long）, float, bool, complex
    非数值类型(for循环):
        分类1：
            有序：str, list, tuple
            无序:set, dict
        分类2：
            可变:list, set, dict
            不可变:str, tuple
    ****字典的for循环:
    d = {'a':'value1'}
    for key, value in d.items(): # [(key, value), ()]
        print(key, value)

# python封装的数据结构:
    tuple ----> namedtuple
    dict ------>  defaultdict


# 函数：
    - 定义函数:
        def 函数名:
            函数体
    - 调用函数
        函数名()
    - 形参: 定义函数里面的参数
    - 实参: 调用函数里面的参数
    - 必选参数: 必须要传递的参数
    - 默认参数： 形参会给一个默认值， 如果不传值，使用默认值， 如果传值， 使用传的值;
    - 可变参数: 传入的参数个数是可变的。 *args =====> *a    args是元组
    - 关键字参数： 传入的参数包含两部分， 键值(key-value)     。 **kwargs  =====> **a   kwargs是个字典
        fun(city="西安")
    - 局部变量和全局变量



"""

from collections import  namedtuple
from collections import  defaultdict
# user = namedtuple('User', ['name', 'age', 'gender'])
# user = user('粉条', 10, 'male')
# print(user.name, user.age)
#


# s = """
# hello world
# hello westos
# """
# words = s.split()
# count_dict = defaultdict(int)
# for word in words:
#     count_dict[word] += 1


