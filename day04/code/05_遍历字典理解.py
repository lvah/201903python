d = dict(name='fentiao', age=10)

# 默认遍历字典只遍历key值;
for item in d:
    print(item)

# [('name', 'fentiao'), ('age', 10)]
print(d.items())
for x in d.items():
    print(x)

# 遍历字典的key-value
for key, value  in d.items():
    print(key, '-->', value)

# 元组多元赋值
key, value = ('name', 'fentiao')
print(key, value)

# 列表可以多元赋值
key, value = ['name', 'fentiao']
print(key, value)


# 列表的多元赋值及循环;
goods = [
    ['phone', 2999, 5],
    ['watch', 10, 1000]
]
for name, price, count in goods:
    print(name, price, count)
