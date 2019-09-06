import random
from collections import  defaultdict
import pprint
# 1). 随机生成50个1-100之间的随机数
count = 50
allNums = []
for item in range(count):
    allNums.append(random.randint(1, 100))

# 2). 大于66的元素和小于66的元素
classifyNums = defaultdict(list)
for num in allNums:
    if num > 66:
        classifyNums['大于66的元素'].append(num)
    elif num < 66:
        classifyNums['小于66的元素'].append(num)

pprint.pprint(classifyNums)

