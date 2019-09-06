# 连接操作符
aStr = "hello\t"
bStr = "python"
print(aStr+bStr)

# 重复操作符
print('*'*50 + '学生管理系统' + '*'*50)

# 计算长度
print(len(aStr))

# 索引
str = 'abcd hello world jjj'
# 正向索引
print(str[0])
print(str[2])
print(str[3])
# 反向索引
print(str[-1])

# 切片(获取多个值)=====range(start,end) 从start开始到end-1结束
print(str[0:2])  # 获取前2个元素
print(str[:2])  # 获取前2个元素, 如果start没有指定， 默认从头开始
print(str[0:3])  # 获取前3个元素
print(str[:3])  # 获取前3个元素

print(str[2:4])  # 获取除了前2个元素
print(str[2:])  # 获取除了前2个元素, 如果end没有指定， 则到末尾

#
# print(id(str))
# copyStr = str[:]
# print(id(copyStr))

print(str[::2])     # 间隔为2显示字符串
print(str[::-1])    # 翻转字符串



# 成员操作符
print('he' in 'hello')   # True
print('ho' in 'hello')  # False
print('ho' not in 'hello')  # True
print('he' not in 'hello')



# string模块
import string
# 所有的小写字母
print(string.ascii_lowercase)
# 所有的大写字母
print(string.ascii_uppercase)
# 所有的字母
print(string.ascii_letters)
# 所有的数字
print(string.digits)



'Hello'

