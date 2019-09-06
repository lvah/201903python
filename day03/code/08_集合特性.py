s = {1, 2, 3}

# 因为集合是无序的, 所以不支持列表和元组拥有的特性;
# 连接操作符
# s = s + {2, 3, 4}
# print(s)
# print(s * 3)
# print(s[0])
# print(s[::-1])


# 成员操作符
print(1 in s)

# # for循环
# for item in s:
#     print(item)


# 枚举
for index, value in enumerate(s):
    print("index=%s, value=%s" % (index, value))

# # zip:
# for item in zip({'a', 'b', 'c'}, {'d', 'e', 'f'}, {1, 2, 3}):
#     print(item)
