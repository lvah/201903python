"""
文件名: .py
创建时间: 2019-01-17 11:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""

import numpy as np


# 1). 创建数组: a, b, c创建的数组相同， 任选一种;
a = np.array([1, 2, 3, 4, 5])
b = np.array(range(1, 6))
c = np.arange(1, 6)

print(a, b, c)
#
# # 2). 查看numpy创建的数组类型
print(type(a))
print(type(b))
print(type(c))

#
# 3). 查看数组存储的数据类型, 常见的数据类型还有哪些?
print(a.dtype)   # 为什么是int64？ 因为硬件架构是64位;


# 4). 制定创建的数组的数据类型
d = np.array([1.9, 0, 1.3, 0], dtype=float)
print(d, d.dtype)
#
# 5). 修改数组的数据类型
e = d.astype('int64')   # 里面可以是数据类型， 也可以是数据代码;int64---i1
print(e, e.dtype)

# 6). 修改浮点数的小数点位数
# 随机创建一个三行四列的数组;
f = np.random.random((3, 4))
print(f)

# 修改浮点书的小数位数为3位
g = np.round(f, 3)
print(g)









