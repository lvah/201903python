"""
游戏规则：
    1). 假设游戏场景为范围（x,y）为0<=x<=10,0<=y<=10
    2). 游戏生成1只乌龟和10条鱼, 它们的移动方向均随机
    3). 乌龟的最大移动能力为2（它可以随机选择1还是2移动），
    鱼儿的最大移动能力是1当移动到场景边缘，自动向反方向移动
    4). 乌龟初始化体力为100（上限）, 乌龟每移动一次，体力消耗1
    当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20, 鱼暂不计算体力
    5). 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束



有几个类?   Fish, Turtle
分析属性信息:
    Fish: x, y坐标位置
    Turtle: x, y坐标位置, hp
分析方法:
    Fish: 移动
    Turtle: 移动, 吃鱼
"""
import random




class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        """
         鱼儿的最大移动能力是1当移动到场景边缘，
        """
        # 鱼儿的最大移动能力是1当移动到场景边缘，
        move_skills = [-1, 0, 1]
        # 计算鱼最新的x轴坐标;
        new_x = self.x + random.choice(move_skills)
        new_y = self.y + random.choice(move_skills)
        self.x = new_x % 10
        self.y = new_y % 10


class Turtle:
    def __init__(self, hp=100):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.hp = hp

    def move(self):
        # 乌龟儿的最大移动能力是2当移动到场景边缘，
        move_skills = [-2, -1, 0, 1, 2]
        # 计算乌龟最新的x轴坐标;
        new_x = self.x + random.choice(move_skills)
        new_y = self.y + random.choice(move_skills)
        self.x = new_x % 10
        self.y = new_y % 10
        # 乌龟每移动一次，体力消耗1
        self.hp -= 1

    def eat_fish(self):
        #  当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
        self.hp += 20


# 游戏生成1只乌龟和10条鱼, 它们的移动方向均随机
turtle = Turtle()
fishs = [Fish() for i in range(10)]
