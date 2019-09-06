# def fun():
#     print('step 1')
#     return  'step 2'  # 图国函数里面遇到return， 函数就执行结束;
#     print('step 3')
#
# result = fun()
# print(result)


# 如果函数里面有yield关键字， 这个函数的返回值是生成器
#********** 如果遇到yield， 函数停止执行， 当再次调用next方法时， 从停止的地方继续执行;
def fun():
    print('step 1')
    yield  'step 2'  # 图国函数里面遇到return， 函数就执行结束;
    print('step 3')
    yield  'step 4'

result = fun()
# print(result)

# for i in result:
#     print(i)

# # 默认next方法会发yield后面的值返回回来;
# print(next(result))
# print(next(result))
# print(next(result))



# for循环时如何封装next方法的；（异常处理）
while True:
    try:
        print(next(result))
    except:
        break
