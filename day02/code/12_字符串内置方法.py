"""

枚举： ‘hello’  0-'h' 1-'e' 2-'l' 'l' 'o'
"""
# enumerate()	枚举对象同时列出数据和数据下标
for index, value in enumerate('hello'):
    print("%.3d : %s" %(index, value))
    print(type(index))


# zip()		将对象中对应的元素打包成一个个元组，
# 		    然后返回由这些元组组成的列表
# 将两个字符串一一对应并返回;
for item in zip('abcd', '123'):
    print("".join(item))


print('%s %d %.2f' %('hello', 10, 12.36565463473))
from string import  Template
s = Template("$who like $what")
# 渲染
print(s.substitute(who="曾金林", what="唱跳"))
print(s.substitute(who="粉条", what="睡觉"))


