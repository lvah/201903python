"""




"""

# 分割
ip = '172.25.254.250'
# 以.为分隔符进行分割;
print(ip.split('.'))  # ['172', '25', '254', '250']
#  以.为分隔符进行分割;最多切割1次；
print(ip.split('.', maxsplit=1))    # ['172', '25.254.250']

filename = 'hello.py'
print(filename.split('.'))

# 按行进行分割
info = """

user1: user1
user2: user2
user3: user3
user4: user4
"""
# 以空格（\t, \n, \ ）进行分割
print(info.split())
# 以\n进行分割;
print(info.splitlines())



# 组合
ips = ['172', '25', '254', '250']
# 将ips里面的每个元素拼接在一起， 拼接符为.；
print(".".join(ips))
print("-".join(ips))




# 小米笔试编程题:
# s='hello xiao mi'  -----> 'mi xiao hello'
s = 'hello xiao mi'
# items = s.split()
# print(" ".join(items[::-1]))
print(" ".join(s.split()[::-1]))