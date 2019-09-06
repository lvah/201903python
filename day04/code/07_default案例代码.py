from collections import  defaultdict
# 创建一个空字典， 所有的value值默认是空列表[]
dict1 = defaultdict(list)
# 判断‘a’这个key值是否存在， 如果不存在， 返回[], .append, 在空列表后面追加元素1；
dict1['a'].append(1)
# 判断‘a’这个key值是否存在， 如果存在， 获取value值, .append, 在原有的value值后面追加元素1；
dict1['a'].append(2)

dict1['b'].append(4)
print(dict1)


# 创建一个空字典， 所有的value值默认是空集合set()
dict1 = defaultdict(set)
# 判断‘a’这个key值是否存在， 如果不存在， 返回set(), .add, 在空列表后面追加元素1；
dict1['a'].add(1)
# 判断‘a’这个key值是否存在， 如果存在， 获取value值, .add, 在原有的value值后面追加元素1；
dict1['a'].add(2)

dict1['b'].add(4)
print(dict1)