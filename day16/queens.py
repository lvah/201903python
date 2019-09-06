def conflict(state, nextColumn):
    """
	state: (7, 4, 6, 0, 2)   标记已经排好的每个皇后的位置，(0,7), (1, 4), (2,6),(3,0),(4,2)
	nextColumn:  2		 下一行八皇后准备要放置的列索引位置
	利用回溯法判断是否可以在第6行的第3列放置皇后， 如果可以，返回True， 如果不可以，返回False;
    """
    nextRow = rows = len(state)  # 5
    for row in range(rows):  # row = 0 1 2 3 4
        column = state[row]
        if abs(column - nextColumn) in (0, nextRow - row):
            """
            i=0:
                state[0]=7,  nextColumn=2      
                如果差值等于0，两个皇后在同一列， 则代表冲突， 返回True;
                如果列的差值等与行的差， 两个皇后在对角线上， 则代表冲突， 返回True;
            """
            return True
    return False

# nums = 8  pos=()
def queens(num, state=()):
    """
    采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
    num: 皇后的数量
    state: 标记已经排好的每个皇后的位置
    """
    for pos in range(num):  # 八皇后的数量N=0, 1, 2, 3, 4, 5, 6 , 7 你要在哪一列放置皇后
        # 如果不冲突，则递归构造棋盘。
        if not conflict(state, pos):  # 回溯法的体现
            # 如果棋盘状态state已经等于num-1，即到达倒数第二行，而这时最后一行皇后又没冲突，直接yield，打出其位置(pos, )
            if len(state) == num - 1:  # state=()
                yield (pos,)
            else:  # (0, )
                for result in queens(num, state + (pos,)):
                    """
                    pos = 0 
                        (0, )  (0, 2), (0, 2, 4), ()
                    1). pos=0，第一行放在第一列，这时不会冲突，但是不会进入if，因为还没到达倒数第二行，   (0)
                    2). 进入else后，再调用queens(num, state+(pos,),这时进入第二行，再次递归展开则是queens(num,state+(pos, )+(pos, ) )
                    2). 进入else后，再调用queens(num, state+(pos,),这时进入第三行，再次递归展开则是queens(num,state+(pos, )+(pos, ) +(pos, ) )
                    3). 到达最后一行时返回(pos, )，再返回倒数第二行，再返回倒数第三行，最后到达最开始那层(pos, )+result, pos为第一行皇后所在列，
                    """
                    yield (pos,) + result



def prettyprint(solution):  # (6, 1, 5, 2, 0, 3, 7, 4)
    """
    友好展示: 为了直观表现棋盘，用X表示每个皇后的位置
    :param solution:
    :return:
    """

    def line(pos, length=len(solution)):  # pos为6，即绘制在第7列  . . . . . . X .
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    solutions = queens(8)
    for index, solution in enumerate(solutions):
        print("第%d种解决方案:" % (index + 1), solution)
        prettyprint(solution)
        print('*' * 100)
