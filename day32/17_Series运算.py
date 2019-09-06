import pandas as pd
import numpy as np
import  string

s1  = pd.Series(np.arange(5), index=list(string.ascii_lowercase[:5]))  # s1.index=[a, b, c, d, e]   s1.value=[0 1 2 3 4]
s2  = pd.Series(np.arange(2, 8), index=list(string.ascii_lowercase[2:8]))  # s2.index = [c,d,e,f]

print(s1)
print(s2)

# *****************按照对应的索引进行计算， 如果索引不同，则填充为Nan;
# 加法, 缺失值+ 真实值===缺失值
print(s1 + s2)
print(s1.add(s2))


# -
print(s1 - s2)
print(s1.sub(s2))


# *
print(s1 * s2)
print(s1.mul(s2))


# /
print(s1 / s2)
print(s1.div(s2))



# 求中位数
print(s1)
print(s1.median())


# 求和
print(s1.sum())


# max
print(s1.max())

# min
print(s1.min())