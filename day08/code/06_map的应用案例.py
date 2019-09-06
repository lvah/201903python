"""
# 输入10个数, 然后对这10个数进行排序
#   1. 获取一个数并换行
# nums = []
# for i in range(10):
#     num = input()
#     nums.append(num)

# nums = [input() for i in range(5)]
# print(nums)


# 2. 把所有的数输入到一行
nums = input().split()

# 2-1). 使用for循环将数值转为整形
# int_nums = []
# for num in nums:
#     int_num = int(num)
#     int_nums.append(int_nums)

# int_nums = [int(num) for num in nums]
# print(sorted(int_nums))


# 2-2). 使用map转换数值为整形
map_num = map(int, nums)
sorted_num  = sorted(map_num)
print(sorted_num)
# 判断是否为可迭代对象
# from collections.abc import  Iterable
# print(isinstance(map_num, Iterable))

"""


def line(num1, num2):
    return  num1 *10 + num2
# map含有多个序列
nums1 = range(2, 6)
nums2 = range(1, 6)
# nums1 = 2   3  4   5
# nums2 = 1   2  3   4  5
# line=====> num1 * 10 + num2
# result = 21 32 43 54

result = list(map(line, nums1, nums2))
print(result)