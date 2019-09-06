"""


# 没有拷贝: li1 = li
# 浅拷贝:
    li2 = li[:]
    li3 = copy.copy(li)
# 深拷贝:
    li4 = copy.deepcopy(li)


"""

# 1). li和li1指向同一块内存空间， 删除任意一个变量， 另一个变量就不能访问。 所以没有成功拷贝;
li = [1, 2, 3, 4, 5]
li1 = li
print(li, id(li))
print(li1, id(li1))

# 拷贝
print("****************浅拷贝**************")
li2 = li[:]
print(li, id(li))
print(li2, id(li2))

li[0] = 100
print(li)
print(li2)

# *******************为什么需要深拷贝***********************
scores = [100, 100, [100, 100, 100]]
scores1 = scores[:]
print(scores, id(scores))
print(scores1, id(scores1))

scores[-1][0] = 200
print(scores)
print(scores1)


# 实现深拷贝
import copy
# copy.copy()  # 浅拷贝
# copy.deepcopy()  # 深拷贝

scores = [100, 100, [100, 100, 100]]
# 深拷贝
scores1 = copy.deepcopy(scores)
print(scores, id(scores))
print(scores1, id(scores1))
scores[-1][0] = 200
print(scores)
print(scores1)




# 浅拷贝
print("浅拷贝第2种实现方式")
scores2 = copy.copy(scores)
print(scores, id(scores))
print(scores2, id(scores1))
scores[-1][0] = 200
print(scores)
print(scores2)


