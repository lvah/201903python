"""
    reshape	不改变数据的条件下修改形状
         numpy.reshape(arr, newshape, order='C')
         order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
    flat	数组元素迭代器

    flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
    ravel	返回展开数组
"""

import numpy as np

print("****************************************flat********************************")
a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)

# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)

#
print("*********************************flatten**************************************")
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')
# 默认按行

print('展开的数组：')
print(a.flatten())
print('\n')

print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))


print("*********************************ravel*************************************")
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))