import random
import pprint

# 1.生成4*4的棋盘数据ss
""",
data =  [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
"""
# 棋盘宽度的变量值
width = 4
# 循环width(4)次， 生成列表， 列表元素为width(4)个
data = [[0 for j in range(width)] for i in range(width)]
pprint.pprint(data)


# 2. 开始游戏时，随机生成2或者4, 2出现的几率比较大
def random_create():
    while True:
        # 获取随机修改信息的行数；
        row = random.randint(0, 3)
        # 获取随机修改信息的列数
        column = random.randint(0, 3)
        # 生成随机填充的值;2出现的几率比较大
        value = random.choice([2, 2, 2, 2, 2, 4])

        # 判断棋盘指定位置原先是否有数据， 如果有， 则继续随机获取行或者列； 如果没有， 填充信息;
        if data[row][column] == 0:
            data[row][column] = value
            break


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

if __name__ == '__main__':
    random_create()
    random_create()
    print("开始游戏时， 棋盘的数据显示:")
    draw_sep()
    for row in data:
        draw_one_row(row)
        draw_sep()


