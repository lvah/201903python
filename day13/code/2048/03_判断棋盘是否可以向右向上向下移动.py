# 判断棋盘是否可以向右移动?
#       对于棋盘的每一行元素进行反转， 判断反转后的棋盘能否向左移动.

from utils import  is_move_left

def invert(data):
    """
    :param data: 棋盘的数据
    :return: 反转后的棋盘数据
    """
    return  [row[::-1] for row in data]


def transpose(data):
    """
    实现矩阵的转置
    :param data:
    :return:
    li = [[2, 0, 4, 2],
        [4, 0, 2, 2],
        [0, 0, 4, 2],
        [0, 0, 4, 2]]
    *li = [2, 0, 4, 2]  [4, 0, 2, 2] [0, 0, 4, 2] [0, 0, 4, 2]
    zip(*li) = [(2, 4, 0, 0), (0, 0, 0, 0), (4, 2, 4, 4), (2, 2, 2, 2)]
    2048里面的数据需要修改, 希望列表里面嵌套列表
    最终希望的结果: [[2, 4, 0, 0], [0, 0, 0, 0], [4, 2, 4, 4], [2, 2, 2, 2]]
    """
    return  [list(row) for row in  zip(*data)]


def is_move_right(data):
    """
    判断2048能否向右移动
    :param data:
    :return:
    """
    invertData = invert(data)
    return  is_move_left(invertData)



def is_move_up(data):
    """
    判断2048能否向上移动
    :param data:
    :return:
    源数据:
        [2, 0, 4, 2],
        [4, 0, 2, 2],
        [0, 0, 4, 2],
        [0, 0, 4, 2],

    处理之后: 判断是否可以向左移动, 也就是判断源数据是否可以向上移动.
        [2, 4, 0, 0],
        [0, 0, 0, 0],
        [4, 2, 4, 4],
        [2, 2, 2, 2]

    这个过程叫做转置(原先的行编程现在的列);
    """
    transposeData = transpose(data)
    return  is_move_left(transposeData)



def is_move_down(data):
    """
    判断2048能否向下移动
    :param data:
    :return:

    源数据:
        [2, 0, 4, 2],
        [4, 0, 2, 2],
        [0, 0, 4, 2],
        [0, 0, 4, 2],


    处理之后: 判断是否可以向右移动, 也就是判断源数据是否可以向下移动.
        [2, 4, 0, 0],
        [0, 0, 0, 0],
        [4, 2, 4, 4],
        [2, 2, 2, 2]
    """
    transposeData = transpose(data)
    return  is_move_right(transposeData)



if __name__ == '__main__':
    data1 = [
        [0, 0, 4, 2],
        [0, 0, 4, 2],
        [0, 0, 4, 2],
        [0, 0, 4, 2],
    ]
    data2 = [
        [0, 2, 0, 4],
        [0, 0, 0, 2],
        [0, 0, 0, 4],
        [0, 0, 0, 0],
    ]
    print("data1能否向右移动? ", is_move_right(data1))  # 不可以
    print("data2能否向右移动? ", is_move_right(data2))  # 可以
    print("data1转置的结果:", transpose(data1))
    print("data2转置的结果:", transpose(data2))
    print("data1能否向上移动? ", is_move_up(data1))     # 可以
    print("data2能否向上移动? ", is_move_up(data2))     # 不可以
    print("data1能否向下移动? ", is_move_down(data1))   # 可以
    print("data2能否向下移动? ", is_move_down(data2))   # 可以