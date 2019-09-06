moveCount = 0
def hanoi(n, a='A', b='B', c='C'):
    """
    :param n:盘子个数
    :param a:初始塔
    :param b:缓存塔
    :param c:目标塔
    :return:移动次数
    """
    if n == 1:
        global moveCount
        moveCount += 1
        print(a, "--->", c)
    else:
        # 只是调用自己， 并没有真实的移动;
        # 1). 打开冰箱门
        hanoi(n - 1, a, c, b)   
        # 2). 把大象放进去
        hanoi(1, a, b, c)
        # 3). 把冰箱门close
        hanoi(n - 1, b, a, c)
hanoi(3)
print("移动次数:", moveCount)
