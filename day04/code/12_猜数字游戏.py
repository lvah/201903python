"""



"""
import random
# 1). 形参-定义函数时里面的参数： 形式参数(可以任意修改名字)
# 2). 如果函数没有return， 默认会返回None;
# 3). 实参-调用函数时指定的值 : 实际存在的参数
def isEuqal(guessNum, gameNum):
    """
    判断用户猜测的数字和游戏给定的数字是否相等?
    :param guessNum:
    :param gameNum:
    :return: Bool-是/否
    """
    if guessNum > gameNum:
        print("太大了")
        return  False
    elif guessNum < gameNum:
        print("太小了")
        return  False
    else:
        print("恭喜你， 中了100万")
        return  True

def main():
    """
    脚本的主函数
    :return:
    """
    for count in range(3):
        gameNum = random.randint(1, 100)
        guessNum = int(input("请开始游戏， 猜测数字(1-100):"))
        if isEuqal(guessNum, gameNum):
            break
    else:
        print("游戏结束， 一百万还很遥远")

main()

