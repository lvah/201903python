"""

假定有下面这样的列表:
    names = ['fentiao', 'fendai', 'fensi', 'apple']
    输出结果为:'I have fentiao, fendai, fensi and apple.'

"""
names = ['fentiao', 'fendai', 'fensi', 'apple']
# 列表切片和索引的掌握案例;
print('I have ' + ",".join(names[:-1]) + 'and ' + names[-1] + '.')
