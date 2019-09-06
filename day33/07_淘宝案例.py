"""
导入相关模块并读取数据库数据
"""
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="westos", db="taobao")
sql = "select price,comment from taob"
data = pd.read_sql(sql, conn)
print(data.head(5))


"""
离差标准化: 消除大单位和小单位的影响（消除量纲）变异大小的差异影响；
"""
# 离差标准化（最小-最大标准化 ） data.max()/min每一列的最大最小值
data2 = (data - data.min()) / (data.max() - data.min())
print(data2.head(5))

"""
标准差标准化: 消除单位影响及自身变量的差异
"""
# 标准差标准化(零-均值标准化)
data3 = (data - data.mean()) / data.std()
print(data3.head(5))

"""
小数定标标准化: 消除单位影响及自身变量的差异
"""
# npy.ceil（）方法：进一取整，如3.1取整为4,3.0取整为3,3.6取整为4
k = np.ceil(np.log10(data.abs().max()))
data4 = data / 10 ** k
print(data4.head(5))

"""
# 1. 什么是离散化： 
    连续属性的离散化就是将连续属性的值域上，将值域划分为若干个离散的区间，最后用不同的符号或整数
    值代表落在每个子区间中的属性值。

# 2. 为什么要离散化
    连续属性离散化的目的是为了简化数据结构，数据离散化技术可以用来减少给定连续属性值的个数。离散化方法经常作为数据挖掘的工具。
    常见的正态假设是连续变量，离散化减少了对于分布假设的依赖性，因此离散数据有时更有效。

# 3. 如何实现离散化?
    数据离散化: 主要使用pandas.cut方法，参数为：数据、区间信息（可以是个数也可以是具体的区间数组）、区间标签（注意数量与前对应）。
"""



"""
等宽离散化
"""
#等宽离散化
data5=data["price"].copy()
# print(data5.head(5))
data6=data5.T
data7=data6.values
k=3 #区间个数
c1=pd.cut(data7,k,labels=["便宜","适中","贵"]) #labels：标签
print("等宽离散化图形绘制: ", c1.describe())



"""
非等宽离散化
"""
k=[0,50,100,300,500,2000,data7.max()] #数组中的数组成了区间，0到50、50到100.....2000到最大值。
c2=pd.cut(data7,k,labels=["非常便宜","便宜","适中","有点贵","很贵","非常贵"])
print(c2.describe())
