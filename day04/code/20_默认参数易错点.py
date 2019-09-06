


# 一定要注意： 默认参数的默认值一定是不可变参数;
def listOperator(li=None):
    """
    对于原有的列表后面追加元素‘End’
    :return:
    """
    if li is None:  # is, ==
        li = []
    li.append('End')
    return  li
# print(listOperator([1, 2, 3]))
# print(listOperator([]))
# print(listOperator([]))

print(listOperator())
print(listOperator())
print(listOperator())