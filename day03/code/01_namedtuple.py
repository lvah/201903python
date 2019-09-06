import collections

# 定义一个命名元组的类， 类名User, 属性有三个, 分别是'name', 'age', 'scores'；
User = collections.namedtuple("User", ['name', 'age', 'scores'])
# 实例化一个类， 名字叫粉条， 等等其他信息;
user = User("粉条", 10, [100, 100, 100])
# 打印该对象的属性;
print(user)
print(user.name)
print(user.age)
print(user.scores)
# ****************************
print(user._fields)
user1 = User._make(['粉丝', 10, [100, 90, 90]])
print(user1)
# 间接改变属性信息;
user2 = user1._replace(name="粉黛")
print(user2)