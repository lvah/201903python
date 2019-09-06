"""

f(1)=1, f(2)=1, f(3)=3.........f(n)=f(n-1)+f(n-2)

"""
# yield关键字
# return 关键字： 工作原理

def fib(n):
    """
    显示多少个fib数列
    :param n:
    :return:
    """
    # a代表第一个数， b代表第2个数， 也就是要显示的数; count: 当前已经显示fib数列的个数;当前为0;
    a, b, count = 0, 1, 0
    # 0<5
    while count < n:
        # print(b)
        yield  b
        # a, b = b, a+b
        a, b = b, a+b
        # 已经显示的次数加1
        count += 1
# fib(5)
# fib(100000)
# f是一个生成器(函数里面有yield)
f = fib(5)
# for i in f:
#     print(i)

while True:
    try:
        print(next(f))
    except:
        break