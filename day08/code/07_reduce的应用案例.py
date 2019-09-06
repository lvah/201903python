# py2直接可以使用reduce， py3
from functools import reduce

# 求两个数值和的匿名函数定义;
add = lambda x, y: x + y
# reduce的工作机制： result=add(add(add(1, 2), 3), 4)
result = reduce(add, [1, 2, 3, 4])
print(result)

# 求10的阶乘
result = reduce(lambda  x, y:x*y, range(1, 10))
print(result)
