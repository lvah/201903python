"""
1. 创建一个三*三*三的随机矩阵/Create a 3x3x3 array with random values (★☆☆)
   很多场景需要随机值，用来测定方法或者模拟实际。numpy.random模块给出了这样功能。在随机值的安排上，
   (b – a) * random_sample() + a，random产生的值只是[0,1)，所以用上面的公式设定最低值。

2. 产生一个十乘十随机数组，并且找出最大和最小值/Create a 10×10 array with random values and find the minimum and maximum values (★☆☆)


3.创建一个中心是边界值为1而内部都是0的数组(10*10)/Create a 2d array with 1 on the border and 0 inside (★☆☆)

4.创建一个8×8的棋盘格/Create a 8×8 matrix and fill it with a checkerboard pattern (★☆☆)

5. 归一化一个随机的5*5矩阵/Normalize a 5×5 random matrix (★☆☆)

归一化就是要把需要处理的数据经过处理后（通过某种算法）限制在你需要的一定范围内。我们这里选用的方法，是把这些随机值找出最大值和最小值，然后把最大值和最小值分别用1和0表示，其他值则反映在0和1中间。



"""
import numpy as np


def task1():
    data = np.random.random((3, 3, 3))
    print("task1: \n", data)


def task2():
    data = np.random.random((10, 10))
    print("task2: \n", data.max(), data.min())


def task3():
    """
    [
        [0 0 0]
        [0 0 0]
        [0 0 0]
    ]

    :return:
    """
    # 方法一:
    # data = np.zeros((10, 10))
    # data[0, :] = 1
    # data[:, 0] = 1
    # data[-1, :] = 1
    # data[:, -1] = 1
    # print("task3: \n", data)

    #     方法二:
    data = np.ones((10, 10))
    data[1:-1, 1:-1] = 0
    print('task3: \n', data)


def task4():
    """
    [
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]
    ]

    :return:
    """
    # 第一设置一个8*8的空值
    data = np.zeros((3, 3))
    # 第二步把第一行隔一列设置1，每两行两列同样
    data[::2, ::2] = 1
    # 第三步类似第二部，不过是从第二行开始，错开
    data[1::2, 1::2] = 1
    print("task4: \n", data)


if __name__ == '__main__':
    task4()
