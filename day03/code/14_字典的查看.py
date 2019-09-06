
# 创建字典
services = {
    'ssh': 22,
    'mysql': 3306,
}
print(services.keys())
print(services.values())
print(services.items())


# # 如何遍历字符串?
# for item in 'hello':
#     print(item, end=',')
#
# # 如何遍历列表？
# for item in [1, 2, 3]:
#     print(item , end=':')
# # 如何遍历元组？
# for item in (1, 2, 3):
#     print(item )

# 如何遍历字典?
# 1). 遍历字典， 默认遍历的是字典的key值;
for item in services:
    print(item)

# 2). 遍历字典的所有value值;
for value in services.values():
    print(value)

#  3). 获取字典的key-value对: [('ssh', 22), ('mysql', 3306)]
# item = ('ssh', 22)
for key,value in services.items():
    print(key, '->', value)
