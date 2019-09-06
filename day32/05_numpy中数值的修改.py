
import numpy as np

# 执行行和指定列的修改
t = np.arange(24).reshape((4, 6))
print(t)
#行： all, 列: 3,4
t[:, 2:4] = 0
print(t)

# 布尔索引
print(t < 10)
#
t[t < 10] = 100
print(t)

t[t > 20] = 200
print(t)


# numpy的三元运算符 t<100?0:10
t1  = np.where(t < 100, 0, 10)
print(t)
print(t1)