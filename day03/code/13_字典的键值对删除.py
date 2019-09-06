
# 创建字典
services = {
    'ssh': 22,
    'mysql': 3306
}



# # 1). 删除ssh对应的键值对
# del services['ssh']
# print(services)


# # 2）. 删除ssh对应的键值对, 并返回ssh对应的value值， 可以保存并使用;
# popReturn =  services.pop('ssh')
# print(services)
# print(popReturn)


# # 3). 随机删除字典的key-value值;
# services.popitem()
# print(services)


# 4). clear
services.clear()
print(services)