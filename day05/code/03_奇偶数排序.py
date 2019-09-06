"""

问题描述1： 有一个整数列表(10个元素)， 要求调整元素顺序，把所有的奇数放在前面，偶数放在后面，
"""

# def isodd(num):
#     """判断是否为偶数"""
#     return num % 2 == 0
# li = [30, 10, 21, 32, 45, 56, 23, 23, 23, 56]
# sorted_num = sorted(li, key=lambda x: 1 if isodd(x) else 0)
# print(sorted_num)


li = [30, 10, 21, 32, 45, 56, 23, 23, 23, 56]
print(sorted(li, key=lambda x: 1 if x % 2 == 0 else 0))
