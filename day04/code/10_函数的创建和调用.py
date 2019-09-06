

# 1). 定义了一个函数名为add;---不会执行里面的代码
# def是python中定义函数的关键字
def add(x, y):
    """
    # 三个双引号可以实现函数的注释
    :param x: 是一个数值
    :param y: 是另一个数值
    :return(返回值): x和y的和
    """
    result = x + y
    # 返回函数的值;如果要显示返回值， 必须要print;
    return  result

# 2). 调用函数----执行函数里面的内容
result = add(1, 2)
print(result)



def get_passwd():
    pass   # 空， 占位关键字


get_passwd()
