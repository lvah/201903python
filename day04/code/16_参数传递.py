# 告诉解释器， 形参的类型， 和返回值的类型
def add(x: int, y: int) -> int:
    # if type(x) == int and type(y) == int:
    # iterable可迭代的,
    #       all是python的内置方法， 如果全为True， 返回True， 有一个为Flase，返回False;
    #       any是python的内置方法， 如果全为False， 返回False， 有一个为True，返回True;
    if all([isinstance(x, int), isinstance(y, int)]):
        return x + y


print(add(1, 2))
#    如果参数类型不对,Python 解释器就无法帮我们检查。(type,isinstance )
print(add('hello', 1))
# 调用函数时,如果参数个数不对,Python 解释器会自动检查出来,并抛出 TypeError；
# print(add('hello'))

# isinstance查看/判别数据类型的
print(isinstance('hello', str))
print(isinstance('hello', int))
