"""
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
json模块是实现Python 对象和JSON 字符串之间转换的模块;
"""
import json
"""
pprint 包含一个“美观打印机”，用于生成数据结构的一个美观视图。格式化工具会生成数据结构的一些表示，不仅可以由解释器正确地解析，
而且便于人类阅读。输出尽可能放在一行上，分解为多行时则需要缩进。
"""
import pprint
# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
from collections import  Counter



# 1). 从文件中读取用户和电影数据
# 打开文件信息, 默认打开方式是读
f = open('movie.txt')
# 将文件中的json字符串转成python便于处理的字典数据类型;
movieDb = json.load(f)
# 关闭文件
f.close()
# print(type(movieDb))
# pprint.pprint(movieDb)


searchUser = input("请输入需要推荐的用户名: ")
# 2).  依次遍历字典的每一个元素， 查找跟user3用户交集最多的用户(user1);
# searchUser 和自己是不需要比较的；
searchUserMovies = set(movieDb.pop(searchUser))
# result存储 searchUser和每个用户喜欢电影交集的个数;= {'user1': 1, 'user2': 2}
result = {}
for user, movies in movieDb.items():
    # 求用户和searchUser交集的个数;
    interaction_count = len(set(movies) & searchUserMovies)
    # 并存储到字典中;
    result[user] = interaction_count


# 3). 打印统计结果
# pprint.pprint(result)


# 4). 对于结果进行排序
# 对字典的value值进行排序， 由大到小;
counter = Counter(result)
# 打印排序结果的前几个, 目前指定的是前5个;
top5UserCounter  = counter.most_common(5)
# print(top5UserCounter)


# 5). 获取前5个跟searchUser相似用户喜欢的电影， 并求并集；
# 获取所有跟searchUser最相关的前5个用户名;
top5User = dict(top5UserCounter).keys()
# allUnionMovies 跟searchUser最相关的前5个用户喜欢的电影的并集; 定义空集合用set()
allUnionMovies = set()
for user in top5User:
    # 获取用户喜欢的电影; 列表;
    # 集合添加元素: add: 添加一个元素; update: 一次添加多个元素；
    allUnionMovies.update(movieDb[user])

# 前5个用户喜欢的电影的并集 -  searchUser喜欢的电影
allRecommendMovies = allUnionMovies -  searchUserMovies
print(allRecommendMovies)
