"""
pandas提供了一个灵活高效的groupby功能，
    1). 它使你能以一种自然的方式对数据集进行切片、切块、摘要等操作。
    2). 根据一个或多个键（可以是函数、数组或DataFrame列>名）拆分pandas对象。
    3). 计算分组摘要统计，如计数、平均值、标准差，或用户自定义函数。

"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.DataFrame(
    {'province': ['陕西', '陕西', '四川', '四川', '陕西'],
     'city': ['咸阳', '宝鸡', '成都', '成都', '宝鸡'],
     'count1': [1, 2, 3, 4, 5],
     'count2': [1, 2, 33, 4, 5]
     }
)
# 陕西      咸阳    1
#          宝鸡     1

print(df)
# 根据某一列的key值进行统计分析;
grouped = df['count1'].groupby(df['province'])
print(grouped.describe())
print(grouped.median())

# 根据城市统计分析cpunt1的信息;
grouped = df['count1'].groupby(df['city'])
print(grouped.max())


# 指定多个key值进行分类聚合;
grouped = df['count1'].groupby([df['province'], df['city']])
print(grouped)
print(grouped.max())
print(grouped.sum())
print(grouped.count())

#  通过unstack方法， 实现层次化的索引;
print(grouped.max().unstack())