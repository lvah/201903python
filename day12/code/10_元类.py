"""

类的本质是对象, 于是可以对类做如下的操作:
1.	 你可以将它赋值给一个变量
2.	 你可以拷⻉它
3.	 你可以为它增加属性
4.	 你可以将它作为函数参数进行传递

"""

import itchat

class Date(object):
    pass


# 1. 你可以将它赋值给一个变量
date = Date
print(date)

# 2.你可以拷⻉它
import  copy
date2 = copy.deepcopy(Date)
print(id(Date))
print(id(date2))


# 3.	 你可以为它增加属性
Date.year = 2019
print(Date.year)


# 4.	 你可以将它作为函数参数进行传递
def fun(cls):
    print(cls)

fun(Date)