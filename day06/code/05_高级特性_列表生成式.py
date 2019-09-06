"""
# 1). 老办法

# 定义一个空列表，用来存储生成的数据;
import random
nums = []
# 生成100个, 循环100次
for i in range(100):
    num = random.randint(1, 100)
    nums.append(num)

# 2). 列表生成式快速生成的办法
nums_quick =  [random.randint(1, 100) for i in range(100)]
# i=0, 3
# i=1, 39
print(nums)
print(nums_quick)


"""

# 1). 求1-50所有数的平方
square = [(i + 1) ** 2 for i in range(50)]
print(square)

# 2). 生成一个2n+1的数字列表，n为从3到11的数字。
nums_list = [2 * n + 1 for n in range(3, 12)]
print(nums_list)

# 3).  求以r为半径的圆的面积和周长(r的范围从1到10)。
import math

circle = [(math.pi * (r ** 2), 2 * math.pi * r) for r in range(1, 11)]
print(circle)

# 4). 将100以内的所有偶数拿出来;
odd_nums = range(0, 101, 2)


# odd_nums_list = []
# for i in range(0, 101):
#     if i%2==0:
#         odd_nums_list.append(i)


# odd_nums_1 = [i for i in range(0,101) if i%2==0]


def is_odd(num):
    return num % 2 == 0
odd_nums_1 = [i for i in range(0,101) if is_odd(i)]

