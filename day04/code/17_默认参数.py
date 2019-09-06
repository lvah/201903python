def mypow(x: int, y: int = 2) -> int:
    """
    求x的y次方
    :param x:
    :param y:
    :return:
    """
    return x ** y

#
# mypow(3, 2)
# mypow(4, 2)
# 如果传递一个参数, x=3, y没有传递就是默认值2；
print(mypow(3))
# 如果传递2个参数, x=3, y有默认值2， 但是3会覆盖默认值，也就是求2的三次方;
print(mypow(2, 3))
