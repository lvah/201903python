import random
import curses
from itertools import chain


class GameField(object):
    """游戏类"""

    # 初始化信息
    def __init__(self, width=4, height=4, win_value=2048):
        self.width = width  # 棋盘的宽度
        self.height = height
        self.win_value = win_value
        self.score = 0  # 当前得分， 默认为0
        self.highscore = 0  # 最高分
        self.is_moves = {
            'Up': self.is_move_up,
            'Down': self.is_move_down,
            'Left': self.is_move_left,
            'Right': self.is_move_right
        }

        self.moves = {
            'Up': self.move_up,
            'Down': self.move_down,
            'Left': self.move_left,
            'Right': self.move_right
        }

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

        # *** 晴空窗口绘制的图形信息
        stdscr.clear()
        stdscr.addstr("2048游戏".center(40, '*') + '\n')

        # 绘制棋盘
        draw_sep()
        for row in self.data:
            draw_one_row(row)
            draw_sep()

        # 游戏的相关信息
        stdscr.addstr("\n当前分数: %s" % (self.score))
        stdscr.addstr("\n当前最高分数: %s" % (self.highscore))
        stdscr.addstr("\n游戏帮助:  上下左右键  E(xit)  R(estart)")

    def is_win(self):
        """
        2048里面有一个数字大于或者等于2048， 游戏胜利
        :param data:
        :return:
        """
        return max(chain(*self.data)) >= 2048

    def is_gameover(self):
        return not any([self.is_move_left(self.data), self.is_move_right(self.data),
                        self.is_move_up(self.data), self.is_move_down(self.data)])

    # [0, 2, 0, 2]  ==>01 12 23
    @staticmethod
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

    def is_move_left(self, data):
        """判断棋盘是否可以向左移动"""
        return any([self.is_row_left(row) for row in data])

    @staticmethod
    def invert(data):
        """
        :param data: 棋盘的数据
        :return: 反转后的棋盘数据
        """
        return [row[::-1] for row in data]

    @staticmethod
    def transpose(data):
        """
        实现矩阵的转置
        :param data:
        :return:
        """
        return [list(row) for row in zip(*data)]

    def is_move_right(self, data):
        """
        判断2048能否向右移动
        :param data:
        :return:
        """
        invertData = self.invert(data)
        return self.is_move_left(invertData)

    def is_move_up(self, data):
        """
        判断2048能否向上移动
        :param data:
        :return:

        """
        transposeData = self.transpose(data)
        return self.is_move_left(transposeData)

    def is_move_down(self, data):
        """
        判断2048能否向下移动
        :param data:
        :return:
        """
        transposeData = self.transpose(data)
        return self.is_move_right(transposeData)

    def move_left(self, data):
        # 判断是否可以移动
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
                    self.score += row[index]  #
            return row

        def row_left(row):
            """将某一行数据向左移动"""
            # 三部曲
            # print(tight(merge(tight([2, 2, 4, 0]))))
            # print(tight(merge(tight([4, 0, 2, 4]))))
            return tight(merge(tight(row)))

        return [row_left(row) for row in data]

    def move_right(self, data):  # 反转====反转回来
        invertData = self.invert(data)
        return self.invert(self.move_left(invertData))

    def move_up(self, data):
        """2048整体向上移动"""
        transposeData = self.transpose(data)
        return self.transpose(self.move_left(transposeData))

    def move_down(self, data):
        """2048整体向下移动"""
        transposeData = self.transpose(data)
        return self.transpose(self.move_right(transposeData))

    def move(self, direction):
        """
        1. 判断这个方向是否可以移动？
        2. 执行移动操作；
        3. 再随机生成一个2或者4
        :param direction:
        :return:
        """
        if direction in self.moves:
            if self.is_moves[direction](self.data):
                self.data = self.moves[direction](self.data)
                self.random_create()


# PEP8
def main(stdscr):
    gameObj = GameField(win_value=32)

    def get_user_action(stdscr):
        """获取用户输入的函数封装"""
        action = stdscr.getch()
        if action == curses.KEY_UP:
            return 'Up'
        elif action == curses.KEY_DOWN:
            return 'Down'
        elif action == curses.KEY_LEFT:
            return 'Left'
        elif action == curses.KEY_RIGHT:
            return 'Right'
        # ord方法查看字母对应的ACII
        elif action == ord('r'):
            return 'Restart'
        elif action == ord('e'):
            return 'Exit'

    def init():
        """初始化函数， 初始化结束后， 游戏进入‘Game’状态"""
        gameObj.reset()
        gameObj.draw(stdscr)
        return 'Game'

    def game():
        gameObj.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        elif action == 'Exit':
            return 'Exit'
        else:
            if gameObj.move(action):
                # 判断win or gameover?
                if gameObj.is_win():
                    return 'Win'
                elif gameObj.is_gameover():
                    return 'GameOver'
            return 'Game'

    def not_game():
        """当游戏状态为Win或者GameOver时执行的逻辑"""
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        elif action == 'Exit':
            return 'Exit'

    state_dict = {
        'Init': init,
        'Game': game,
        'Win': not_game,
        'GameOver': not_game,
        'Exit': exit
    }
    state = 'Init'  # 刚开始玩游戏， 游戏状态为Init
    while True:
        state = state_dict.get(state)()


curses.wrapper(main)


# pygame