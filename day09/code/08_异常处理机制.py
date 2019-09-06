"""
try......except........
"""


try:
    # try里面写的是要执行的代码;
    print(a)
    print(10/0)
    # 此处不会打印westos, 因为上一行代码执行报错;
    print('westos')
except NameError:
    # try里面的代码如果有异常/错误, 才会执行的代码;
    # except NameError:, 只对NmaeError错误进行处理;
    print("错误")
else:
    # 判断是否有异常, 如果没有, 执行此代码;
    print("运行成功")
finally:
    # 有异常和没有异常都会执行的代码;
    print("检测finally的作用")
# 此处不会打印westos, 因为代码实现了异常处理;
print('westos')