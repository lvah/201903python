"""
Series 基本操作:
编号      属性或方法           描述
1       axes                返回行轴标签列表。
2       dtype               返回对象的数据类型(dtype)。
3       empty               如果系列为空，则返回True。
4       ndim                返回底层数据的维数，默认定义：1。
5       size                返回基础数据中的元素数。
6       values              将系列作为ndarray返回。
7       head()              返回前n行。
8       tail()              返回最后n行。


"""

import pandas as pd
import numpy as np
import  string

array = ["粉条", "粉丝", "粉带"]
s1 = pd.Series(data=array)
print(s1)
print(s1.axes)
print(s1.dtype)
print(s1.empty)
print(s1.ndim )
print(s1.size)
print(s1.values)

#
# 1). 修改Series索引
print(s1.index)
s1.index = ['A', 'B', 'C']
print(s1)


# 2). Series纵向拼接;
array = ["粉条", "粉丝", "westos"]
# 如果不指定索引， 默认从0开始;
s2 = pd.Series(data=array)
s3 = s1.append(s2)
print(s3)
#
# 3). 删除指定索引对应的元素;
s3 = s3.drop('C')  # 删除索引为‘C’对应的值;
print(s3)


# 4). 根据指定的索引查找元素
print(s3['B'])
s3['B'] = np.nan  # None, null, pandas数据为空, 或者数据缺失, np.nan
print(s3)


# 5). 切片操作  --- 同列表
print(s3[:2])
print(s3[::-1])
print(s3[-2:])  # 显示最后两个元素