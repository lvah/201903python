
# 定义集合的第一种方式, 默认会去重;
s = {1, 2, 3, 4, 1, 2, 3}
print(type(s))
print(s)

# 定义集合的第2种方式: 定义一个空集合
# 注意： 定义空集合的方式
s = {}
print(type(s))
print(s)

s = set()
print(type(s))
print(s)

s = {1}
print(type(s), s)

# 集合里面不能存储可变的数据类型列表; 定义不成功;
# s3 = {1,2,3,'hello',(1,2,3),[1,2,3]}
# print(s3, type(s3))


# 可以成功
s4 = set('abracadabra')
print(s4)
print(type(s4))