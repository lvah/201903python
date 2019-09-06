"""
    resize	返回指定形状的新数组
    append	将值添加到数组末尾
    insert	沿指定轴将值插入到指定下标之前
    delete	删掉某个轴的子数组，并返回删除后的新数组
    unique 	查找数组内的唯一元素
            arr：输入数组，如果不是一维数组则会展开
            return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
            return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数

"""
import numpy as np

print('***************append****************')
a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('向数组添加元素：')
print(np.append(a, [7, 8, 9]))
print('\n')

print('沿轴 0 添加元素：')
print(np.append(a, [[7, 8, 9]], axis=0))
print('\n')

print('沿轴 1 添加元素：')
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

print('******************************insert****************************************')
a = np.array([[1, 2], [3, 4], [5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print('\n')

print('传递了 Axis 参数。 会广播值数组来配输入数组。')
print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print('\n')

print('沿轴 1 广播：')
print(np.insert(a, 1, 11, axis=1))

print('***********************delete******************************************')
a = np.arange(12).reshape(3, 4)

print('第一个数组：')
print(a)
print('\n')

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('\n')

print('删除第二列：')   # axis=1, 水平方向， 将每一行的第1个索引元素删除;
print(np.delete(a, 1, axis=1))
print('\n')

print('删除第二行：')     # axis=0, 竖直方向, 将每一列的第第一个索引删除'
print(np.delete(a, 1, axis=0))
print('\n')

print('包含从数组中删除的替代值的切片：')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""
np.s_ 为阵列建立索引元组的一种更好的方法。 返回的时slice对象;
也可以使用`Slice()‘加上一些特殊的对象来完成所有这些操作但这个版本更简单，因为它使用了标准的数组索引语法。
"""
print(np.delete(a, np.s_[::2]))


print("删除二维数组")
data = np.arange(12).reshape((3, 4))
print("数组元素:")
print(data)
# 行：  列: 2列开始
print(np.delete(data, np.s_[::2], axis=0))
print(np.delete(data, np.s_[::2], axis=1))


#
#
# print('****************************unique**********************************************')
#
# a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
# #
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('第一个数组的去重值：')
# u = np.unique(a)
# print(u)
# print('\n')
#
# print('去重数组的索引数组：')
# u, indices = np.unique(a, return_index=True)
# print(indices)
# print('\n')
#
# print('返回去重元素的重复数量：')
# u, indices = np.unique(a, return_counts=True)
# print(u)
# print(indices)