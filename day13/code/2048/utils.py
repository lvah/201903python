"""
分而治之
问题一: 如何让判断棋盘是否可以向左移动?
       只要棋盘的任意一行可以向左移动， 就返回True；

问题二: 如何判断棋盘的一行是否可以向左移动?
        只要这一行的任意两个元素可以向左移动， 则返回True;

问题三: 如何两个元素可以向左移动?
       - 如果第一个数值为0， 第二个数值不为0， 则说明可以向左移动； eg: 0 2  , 0 4 , 0 8
       - 如果第一个数值不为0， 第二个数值与第一个元素相等， 则说明可以向左移动；eg: 4 4, 2 2,


"""


# [0, 2, 0, 2]  ==>01 12 23
def is_row_left(row: list) -> bool:
    """用户传入一行数据， 判断是否可以向左移动， 返回Bool"""

    # 任意两个元素是否可以向左移动?
    def is_item_left(index):  # index指的是索引值
        """判断当前索引值和下一个索引值， 是否可以向左移动"""
        # - 如果第一个数值为0， 第二个数值不为0， 则说明可以向左移动； eg: 0 2  , 0 4 , 0 8
        if row[index] == 0 and row[index + 1] != 0:
            return True
        # - 如果第一个数值不为0， 第二个数值与第一个元素相等， 则说明可以向左移动；eg: 4 4, 2 2,
        if row[index] != 0 and row[index] == row[index + 1]:
            return True
        return False

    # 只要这一行的任意两个元素可以向左移动， 认为这一行可以向左移动， 返回True；
    # any(): 传递可迭代对象， 如果有任意一个为True， 则返回True；
    # all(): 传递可迭代对象， 如果有任意一个为False， 则返回False；
    return any([is_item_left(index) for index in range(3)])


def is_move_left(data):
    """判断棋盘是否可以向左移动"""
    return any([is_row_left(row) for row in data])


def invert(data):
    """
    :param data: 棋盘的数据
    :return: 反转后的棋盘数据
    """
    return [row[::-1] for row in data]


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
    return [list(row) for row in zip(*data)]


def is_move_right(data):
    """
    判断2048能否向右移动
    :param data:
    :return:
    """
    invertData = invert(data)
    return is_move_left(invertData)


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
    return is_move_left(transposeData)


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
    return is_move_right(transposeData)


# 3. 绘制棋盘的分隔符
def draw_sep():
    """+----+----+----+----+"""
    print("+----" * 4 + "+")


# 4. 绘制每一行的数据
def draw_one_row(row):
    # [0, 0, 2, 2], 如果有值， 内容填充
    # |     |     |     2   |   2   |
    for item in row:
        if item == 0:
            print('|    ', end='')
        else:
            print('|' + str(item).center(4), end='')
    print('|')


def draw(data):
    draw_sep()
    for row in data:
        draw_one_row(row)
        draw_sep()


if __name__ == '__main__':
    print(is_row_left([0, 2, 0, 2]) == True)
    print(is_row_left([0, 0, 0, 0]) == False)
    print(is_row_left([2, 2, 2, 2]) == True)
    print(is_row_left([2, 4, 2, 4]) == False)
