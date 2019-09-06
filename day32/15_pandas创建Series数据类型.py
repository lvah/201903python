"""
Pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。
利器之一：Series
    类似于一维数组的对象，是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成。仅由一组数据也可产生简单的Series对象。
利器之二：DataFrame
    是Pandas中的一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔型等)，DataFrame即有行索引也有列索引，可以被看做是由Series组成的字典。

常见的数据类型:
    - 一维: Series
    - 二维: DataFrame
    - 三维: Panel  ....
    - 四维: Panel4D  .....
    - N维: PanelND  ....


Series是Pandas中的一维数据结构，类似于Python中的列表和Numpy中的Ndarray，不同之处在于：Series是一维的，能存储不同类型的数据，有一组索引与元素对应。
"""

import pandas as pd
import numpy as np
import  string


# 查看pandas版本信息
print(pd.__version__)

# ********************创建Series对象

#  1). 通过列表创建Series对象
array = ["粉条", "粉丝", "粉带"]
# 如果不指定索引， 默认从0开始;
s1 = pd.Series(data=array)
print(s1)
# 如果不指定索引， 默认从0开始;
ss1 = pd.Series(data=array, index=['A', 'B', 'C'])
print(ss1)

# 2). 通过numpy的对象Ndarray创建Series；
n = np.random.randn(5)   # 随机创建一个ndarray对象;
s2 = pd.Series(data=n)
print(s2)
# 修改元素的数据类型;
ss2 = s2.astype(np.int)
print(ss2)

# 3). 通过字典创建Series对象;
dict = {string.ascii_lowercase[i]:i for i in range(10)}
# print(dict)
s3 = pd.Series(dict)
print(s3)