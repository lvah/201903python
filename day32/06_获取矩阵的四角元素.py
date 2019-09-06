"""
获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。
"""

import numpy as np


def get_edge(data):
    """获取了数组中的四个角的元素"""
    row, column = data.shape
    rows = np.array([[0, 0], [row - 1, row - 1]])
    cols = np.array([[0, column - 1], [0, column - 1]])
    return  data[rows, cols]



if __name__ == '__main__':
    x = np.arange(30).reshape((5, 6))
    print("data：", x)
    print("result: ", get_edge(x))

# x = np.arange(12).reshape((4, 3))
# print('我们的数组是：')
# print(x)
#
#
#
# row, column = x.shape  # row=4 column=3
# # rows = np.array([[0, 0], [3, 3]])
# # cols = np.array([[0, 2], [0, 2]])
#
# rows = np.array([[0, 0], [row-1, row-1]])
# cols = np.array([[0, column-1], [0, column-1]])
# y = x[rows, cols]
# print('这个数组的四个角元素是：')
# print(y)
