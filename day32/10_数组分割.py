"""
    split	将一个数组分割为多个子数组
        numpy.split(ary, indices_or_sections, axis)
    hsplit	将一个数组水平分割为多个子数组（按列）
    vsplit 	将一个数组垂直分割为多个子数组（按行）
"""

import numpy as np


print("**********************split******************************")
a = np.arange(9)
print('第一个数组：')
print(a)
print('\n')

print('将数组分为三个大小相等的子数组：')
b = np.split(a, 3)
print(b)
print('\n')

print('将数组在一维数组中表明的位置分割：')
b = np.split(a, [3, 7])
print(b)



print('******************hsplit*****************')
harr = np.arange(12).reshape((3, 4))
print('原array：')
print(harr)

print('横向拆分后：')
print(np.hsplit(harr, 2))



print("***************************vsplit****************************")

a = np.arange(12).reshape(4, 3)

print('第一个数组：')
print(a)
print('\n')

print('竖直分割：')
b = np.vsplit(a, 2)
print(b)
