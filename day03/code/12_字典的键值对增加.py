
# 创建字典
services = {
    'ssh': 22,
    'mysql': 3306
}

# # 1). 根据key值增加;services[key]， 如果key不存在， 增加键值对； 如果key已经存在， 更新key对应的value值;
# services['http'] = 80
# print(services)
# services['ssh'] = 80
# print(services)

# # 2). setdefault, 如果key不存在， 增加键值对； 如果key已经存在，不做任何操作;
# services.setdefault('http', 80)
# print(services)
#
# services.setdefault('ssh', 80)
# print(services)

# 3). update，(和第一种方法的区别: 可以一次更新多个键值对) 如果key不存在， 增加键值对； 如果key已经存在， 更新key对应的value值;
services.update({'http':80, 'ftp':21})
print(services)
services.update({'ssh': 80})
print(services)
