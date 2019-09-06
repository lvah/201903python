"""
# 2048游戏向左移动:
#   1). 让2048的每一行数据都向左移动?
#   2). 如何让每一行数据向左移动?

eg: [2 2 2 2]  ====== [4 4 0 0]
    2-1). 先把这一行所有的非0数字向前放， 0向后放. [2 2 2 2]
    2-2). 依次循环判断两个数是否相等， 如果相等， 第一个元素*2， 第二个元素归0；   [4 0 4 0]
    [2 2 2 2] --->判断前两个元素   [4 0 2 2]  ----> 第2和3元素   [4 0 2 2]  -->  第3个和4个元素 [4 0 4 0]
    2-3). 这一行所有的非0数字向前放， 0向后放.   [4 4 0 0]

"""
from utils import invert
from utils import transpose
from utils import draw
def tight(row):
    """将这一行所有的非0数字向前放， 0向后放."""
    return sorted(row, key=lambda x: 1 if x == 0 else 0)


def merge(row):
    """
    [2, 0, 2, 0]
     2-2). 依次循环判断两个数是否相等， 如果相等， 第一个元素*2， 第二个元素归0；   [4 0 4 0]
    :param row:
    :return:
    """
    # 比较的次数
    for index in range(3):
        # 如果相等， 第一个元素*2， 第二个元素归0；
        if row[index] == row[index + 1]:
            # row[index] = row[index] * 2
            row[index] *= 2
            row[index + 1] = 0
    return row


def row_left(row):
    """将某一行数据向左移动"""
    # 三部曲
    # print(tight(merge(tight([2, 2, 4, 0]))))
    # print(tight(merge(tight([4, 0, 2, 4]))))
    return tight(merge(tight(row)))


def move_left(data):
    """2048整体向左移动"""
    return [row_left(row) for row in data]


def move_right(data):  # 反转====反转回来
    """
    2048整体向右移动
    源数据:
        [2 0 2 0]
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]


    反转
        [0 2 0 2]
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]

    向左移动
        [4 0 0 0]
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]


    反转:
        [0 0 0 4]
        [0 0 0 0]
        [0 0 0 0]
        [0 0 0 0]

    """
    invertData = invert(data)
    return invert(move_left(invertData))


def move_up(data):
    """2048整体向上移动"""
    transposeData = transpose(data)
    return transpose(move_left(transposeData))


def move_down(data):
    """2048整体向下移动"""
    transposeData = transpose(data)
    return transpose(move_right(transposeData))


if __name__ == '__main__':
    data1 = [2, 2, 4, 4]
    data2 = [2, 0, 4, 0]
    print("data1向左移动: ", row_left(data1))
    print("data2向左移动: ", row_left(data2))

    data3 = [
        [0, 2, 8, 2],
        [2, 2, 4, 4],
        [0, 2, 0, 2],
        [0, 0, 0, 0]
    ]
    print("data3向左移动:")
    draw(move_left(data3))
    print("data3向右移动:")
    draw(move_right(data3))
    print("data3向上移动:")
    draw(move_up(data3))
    print("data3向下移动:", )
    draw(move_down(data3))