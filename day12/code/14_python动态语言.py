from prettytable import  PrettyTable
# 自省功能

# 判断;类里面是否包含指定的属性?
print(hasattr(PrettyTable, '__doc__'))
print(hasattr(PrettyTable, 'a'))


# 获取指定属性对应的内容;
print(getattr(PrettyTable, "__bases__"))
# print(getattr(PrettyTable, "a"))

# 设置指定的属性, 动态添加属性信息的
setattr(PrettyTable, 'a', 1)
print(getattr(PrettyTable, 'a'))

@staticmethod
def test():
    print("这是一个测试方法")


if hasattr(PrettyTable, 'test'):
    print(getattr(PrettyTable, 'test'))
else:
    print("正在动态添加方法:")
    setattr(PrettyTable, 'test', test)
    print(getattr(PrettyTable, 'test'))
    test = getattr(PrettyTable, 'test')  # 返回的时函数名
    test()

print(hasattr(PrettyTable, 'a'))
print("正在删除属性")
delattr(PrettyTable, 'a')

print(hasattr(PrettyTable, 'a'))