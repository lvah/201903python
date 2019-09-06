"""
假设已有若干用户名字及其喜欢的电影清单，现有某用户，已看过并喜欢一些电影，现在想找个新电影看看，又不知道看什么好。
根据已有数据，查找与该用户爱好最相似的用户，也就是看过并喜欢的电影与该用户最接近，然后从那个用户喜欢的电影中选取
一个当前用户还没看过的电影，进行推荐。


"""
import random
import pprint
# 1). 设计沪剧存储的数据结构; 字典里面， value值是列表;
movieDb = {
    '小明': ["流浪地球", "复仇者联盟4"],
    '小红': ["流浪地球", "复仇者联盟4", "前任"]

}

# 2). 随机生成100个电影名
movies = []
for item in range(100):
    movie_name = '电影' + str(item)
    movies.append(movie_name)
print(movies)

# 3). 随机生成用户和喜欢电影的集合;
for item in range(100):
    name = 'user' + str(item)
    # random.sample([1, 2, 3, 4], 3) ---> 从指定的序列中拿出指定个数据出来;返回的是列表;
    user_movies = random.sample(movies, random.randint(2, 30))
    movieDb[name] = user_movies


# 4). 更加友好的打印数据信息;
# pprint.pprint(movieDb)


# 5). 如何写入文件中;
# json: javascript  object
import json
# 以写的权限打开文件;
f = open('movie.txt', 'w')
# 将python的字典转成json格式的字符串， 并保存到文件对象f中;
# ensure_ascii=False: 中文显示正确
# indent=4缩进进为4个空格;
json.dump(movieDb, f, ensure_ascii=False, indent=4)
# 关闭文件;
f.close()
