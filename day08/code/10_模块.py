"""

"""

# 模块实质上就是一个python文件;
import time
import random
import math
import string
import functools
import prettytable
import pprint
import os
import pickle

import json
import itchat

# 1. 如何让自己编写模块(自己编写的文件千万不要和常见的模块名冲突)-----直接导入
# import  myitchat
# # 可以调用变量名
# print(myitchat.a)
# print(myitchat.b)
# # 可以调用函数
# print(myitchat.sleep())


# 2.
# from myitchat import  sleep
# from myos import  sleep
# sleep()


# import  myitchat
# import  myos
#
#
# myitchat.sleep()
# myos.sleep()


# import  myitchat as mt
# import  pandas as pd
# import  matplotlib.pyplot as plt
# import  numpy as np
# import  os.path as path
# print(path.exists('/etc/passwd'))


# from random import *
#
# print(random())
# print(randint(1, 10))
# print(choice([1, 2, 3, 4]))
# print(sample([1, 2, 3, 4, 5], 2))
# li = list(range(10))
# shuffle(li)
# print(li)



from myitchat import  *
print(a)
print(b)
# print(sleep())
import  sys
print(sys.path)

