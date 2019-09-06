content = """
hello python
hello westos
hello world
"""

# 1). 将每个单词拿出来(split) ---> ['hello', 'python', .......]
content_list = content.split()
# 2）. 定义一个空字典d={}， 用来存储每个单词出现的次数;
counterDict = {}
# 3). 依次遍历列表的每个单词,
#       d['hello'] = 2
#       d['pyhton'] = 1
for item in content_list:
    # 如果该单词在字典中没有统计过， 赋值为1；
    if item not in counterDict:
        counterDict[item] = 1
    # 如果该单词在字典中已经统计过， 在原有的个数基础上加1；
    else:
        # oldCount = counterDict[item]
        # newCount = oldCount + 1
        # counterDict[item] = newCount
        counterDict[item] += 1

# 输出结果
print(counterDict)


# d = {'hello':3, 'python':1, 'westos':1, 'world':1}