"""

"""

# 列表: 如果列表的顺序发生变化, 后面的操作也需要修改下标或者其他信息;
users = ["root", 'password']
# 通过索引方式修改值
users[0] = 'admin'

users = ['password', "root"]
# 通过索引方式修改值
users[1] = 'admin'




# 字典:可以快速定位到需要的信息;
users = {
    'username' : 'root',
    'password': 'westos'
}

print(users['username'])
print(users['password'])

users = {
    'password': 'westos',
    'username' : 'root',

}

print(users['username'])
print(users['password'])



# 1). 简单字典创建
# 键(key)一般是唯一的，如果重复最后的一个键值对会替换前面的，值(value)不需要唯一。
# 字典是由键值对组成(key-value)
services = {
    # 冒号前面的值叫做键key, 冒号后面的值叫做值value;
    'ssh' : 22,
    'http': 80,
    'mysql' : 3306,
    'ssh': 33
}
# 如果重复最后的一个键值对会替换前面的
print(services)

# 字典是不支持索引和切片的,
print(services['ssh'])



# 2).    内建方法:fromkeys
# 根据序列依次创建多个key-value对, key值是序列的每个元素, value相同(如果没有指定, 全为None; 如果指定了, 为指定的内容)
# 应用场景: 批量生成银行卡号;批量生成value值相同的信息;
usersInfo = {}.fromkeys(['user1', 'user2', 'user3'], 'westos')
print(usersInfo)

# 3). zip间接创建
users = dict(zip(['name', 'age', 'gender'], ['粉条', 10, 'male']))
print(users)

# 4). dict工厂函数创建
users = dict(name="粉条", age=10, gender='male')
print(users)
