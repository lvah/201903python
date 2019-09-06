from itertools import chain
# 1. 何时用户游戏胜利?(当棋盘中出现num=2048时， 则代表用户胜利)
from utils import is_move_left, is_move_right, is_move_up, is_move_down


def is_win(data):
    """
    2048里面有一个数字大于或者等于2048， 游戏胜利
    :param data:
    :return:
    """

    # 思路一:
    # for row in data:
    #     for item in row:
    #         if item >= 2048:
    #             return  True
    # else:
    #     return  False

    # 思路2： 将嵌套的元素连成一个列表
    # print(*data)  # 解包
    # print(list(chain(*data)))
    # maxNum = max(chain(*data))
    # print(maxNum)
    return max(chain(*data)) >= 2048


# 2. 何时game over?(当用户在任何方向都不能移动时， 则代表游戏结束， 用户失败)
# 只要有任意一个方向可以移动， 那就没有结束
def is_gameover(data):
    return  not any([is_move_left(data), is_move_right(data),
                     is_move_up(data), is_move_down(data)])


if __name__ == '__main__':
    data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    print(is_win(data))
    print(is_gameover(data))  # 游戏未结束