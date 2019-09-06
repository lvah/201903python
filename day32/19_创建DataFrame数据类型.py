"""


Series只有行索引，而DataFrame对象既有行索引，也有列索引
    行索引，表明不同行，横向索引，叫index，
    列索引，表明不同列，纵向索引，叫columns，

"""


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 方法1： 通过列表创建
li = [
    [1, 2, 3, 4],
    [2, 3, 4, 5]
]

# DataFRame对象里面包含两个索引， 行索引(0轴， axis=0)， 列索引(1轴， axis=1)
d1 = pd.DataFrame(data=li, index=['A', 'B'], columns=['views', 'loves', 'comments', 'tranfers'])
print(d1)

# 方法2： 通过numpy对象创建
narr = np.arange(8).reshape(2, 4)
# DataFRame对象里面包含两个索引， 行索引(0轴， axis=0)， 列索引(1轴， axis=1)
d2 = pd.DataFrame(data=narr, index=['A', 'B'], columns=['views', 'loves', 'comments', 'tranfers'])
print(d2)

# 方法三: 通过字典的方式创建;
dict = {
    'views': [1, 2, ],
    'loves': [2, 3, ],
    'comments': [3, 4, ]

}
d3 = pd.DataFrame(data=dict, index=['粉条', "粉丝"])
print(d3)


# 日期操作的特例:
# pd.date_range()
dates = pd.date_range(start='1/1/2019', end='1/08/2019')
print(dates)


# 行索引
dates = pd.date_range(start='today', periods=6, freq='2D' ) # periods=6从今天开始向后产生6个日期
print(dates)

# 数据
data_arr = np.random.randn(6, 4)
# print(data_arr)
# 列索引
columns = ['A', 'B', 'C', 'D']
d4 = pd.DataFrame(data_arr, index=dates, columns=columns)
print(d4)



# 一维对象: 建立一个以2019年每一天作为索引， 值为随机数；
dates = pd.date_range(start='1/1/2019', end='12/31/2019', freq='D')
datas = np.random.randn(len(dates))
s1 = pd.Series(datas, index=dates)
print(s1[:3])