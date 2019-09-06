"""
tuple = (1, 2, 3)
namedtuple : 命名元组


dict:
defaultdict:

"""
#
# from collections import  namedtuple
# User = namedtuple('User', ["name", "age"])
# user = User("粉条", 10)
# print(user.name, user.age)
from collections import  defaultdict
from collections import  Counter

content = """
hello python
hello westos
hello world
"""

# 1). 将每个单词拿出来(split) ---> ['hello', 'python', .......]
content_list = content.split()
# 2). 定义一个有默认value值的字典, int的默认值是0；
counterDict = defaultdict(int)
# 3). 依次遍历每一个元素， 并且额统计出现次数；
for content in content_list:
    counterDict[content] += 1

# 4), 对统计数据进行排序
counter = Counter(counterDict)
top1word = counter.most_common(1)
print("出现次数最多的单词:", top1word[0][0])


