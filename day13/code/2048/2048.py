import random
import  curses

class GameField(object):
    """游戏类"""

    # 初始化信息
    def __init__(self, width=4, height=4, win_value=2048):
        self.width = width  # 棋盘的宽度
        self.height = height
        self.win_value = win_value
        self.score = 0  # 当前得分， 默认为0
        self.highscore = 0  # 最高分

    def random_create(self):
        """在随机位置生成2或者4"""
        while True:
            # 获取随机修改信息的行数；
            row = random.randint(0, self.height - 1)
            # 获取随机修改信息的列数
            column = random.randint(0, self.width - 1)
            # 生成随机填充的值;2出现的几率比较大
            value = random.choice([2, 2, 2, 2, 2, 4])

            # 判断棋盘指定位置原先是否有数据， 如果有， 则继续随机获取行或者列； 如果没有， 填充信息;
            if self.data[row][column] == 0:
                self.data[row][column] = value
                break

    def reset(self):  # 重新开始2048游戏
        # 更新最高分
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.data = [[0 for j in range(self.width)] for i in range(self.height)]
        self.random_create()
        self.random_create()

    def draw(self, stdscr):
        """接收一个参数stdscr， 标准屏幕， 将来在该屏幕上绘制数据"""

        # . 绘制棋盘的分隔符
        def draw_sep():
            """+----+----+----+----+"""
            stdscr.addstr("+----" * 4 + "+" + '\n')

        # . 绘制每一行的数据
        def draw_one_row(row):
            # [0, 0, 2, 2], 如果有值， 内容填充
            # |     |     |     2   |   2   |
            for item in row:
                if item == 0:
                    stdscr.addstr('|    ')
                else:
                    stdscr.addstr('|' + str(item).center(4))
            stdscr.addstr('|\n')

        stdscr.addstr("2048游戏".center(40, '*') + '\n')

        # 绘制棋盘
        draw_sep()
        for row in self.data:
            draw_one_row(row)
            draw_sep()

        # 游戏的相关信息
        stdscr.addstr("\n当前分数: %s" % (self.score))
        stdscr.addstr("\n当前最高分数: %s" % (self.highscore))
        stdscr.addstr("\n游戏帮助:  上下左右键  Q(uit)  R(estart)")



    # 判断是否可以移动


# PEP8
def main(stdscr):
    game = GameField(win_value=32)
    game.reset()
    game.draw(stdscr)
    while True:
        action = stdscr.getch()
        stdscr.addstr(str(action))


curses.wrapper(main)