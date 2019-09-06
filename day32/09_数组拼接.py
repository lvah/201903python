"""
concatenate	连接沿现有轴的数组序列
stack	沿着新的轴加入一系列数组。
hstack	水平堆叠序列中的数组（列方向）
vstack	竖直堆叠序列中的数组（行方向）

"""

import numpy as np


print("******************** concatenate ****************")
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')

b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')

# 两个数组的维度相同
# x轴和y轴， 1轴和0轴
print('沿轴 0 连接两个数组：')
print(np.concatenate((a, b)))
print('\n')

print('沿轴 1 连接两个数组：')
print(np.concatenate((a, b), axis=1))




print("*************************stack*********************************")
a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')

print('沿轴 0 堆叠两个数组：')
print(np.stack((a, b), axis=0))
print('\n')

print('沿轴 1 堆叠两个数组：')
print(np.stack((a, b), axis=1))



#
#

print("**************************************hstack + vstack*************************************")
a = np.array([[1, 2], [3, 4]])

print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])

print('第二个数组：')
print(b)
print('\n')

print('水平堆叠：')
c = np.hstack((a, b))
print(c)
print('\n')


print('竖直堆叠：')
c = np.vstack((a, b))
print(c)
print('\n')