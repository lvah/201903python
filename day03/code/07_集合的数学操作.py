"""



"""

set1 = {1, 2, 3}
set2 = {1, 2, 4}

# print("交集".center(50, '*'))
# print("集合1和集合2的交集:", set1.intersection(set2))
# # print(set1.intersection_update(set2))
# # print(set1)
# # # 求集合1和集合2的交集, 并更新集合1为交集的内容
# # set2.intersection_update(set1)
# # print(set2)
# print("集合1和集合2的交集:", set1 & set2)


# print("并集".center(50, '*'))
# print(set1.union(set2))
# print(set1 | set2)


# 自己 - 交集
print("差集".center(50, '*'))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1 - set2)
# print(set2 - set1)

# 对等差分 = 交集 - 并集
print("对等差分".center(50, '*'))
# print(set1.symmetric_difference(set2))
# print(set2.symmetric_difference(set1))
# print(set1 ^ set2)


set3 = {1, 2, 3, 4}
set4 = {1, 2, 3}
print(set3.issubset(set4))
print(set4.issubset(set3))
print(set3.issuperset(set4))
print(set3.isdisjoint(set4))
print({1, 2}.isdisjoint({3, 4}))

"""
s1 = {1, 2, 3}
s2 = {1,2 }
s1.issuperset(s2)   # s1里面包含s2吗?
Out[4]: True
s3 = {1, 4}
s1.issuperset(s3) # s1里面包含s3吗?
Out[6]: False
s2.issubset(s1)  # s2包含在s1里面吗?
Out[7]: True
"""