"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
1、1、2、3、5、8、13、21、34、……在数学上，斐波纳契数列以如下被以递推的方法定义：
F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
"""


def fib(num):
    """
    斐波那契数列
    :param num:
    :return:
    """
    if num <= 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
result = fib(4)
print(result)
