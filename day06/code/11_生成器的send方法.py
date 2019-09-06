"""
next方法:
send方法: 给生成器传递数据
"""

# 面向切面编程
def fun():
    while True:
        print('welcome......')
        receive = yield  'hello'
        print(receive)


# f是生成器
f = fun()
in_function = next(f)
print("函数里面返回的值:", in_function)
f.send("西部开源")