"""
 明明的随机数

"""
import  random
N = int(input("生成数:"))
# **). 生成了N个1到1000之间的随机整数（N≤1000）, 其余相同的数去掉
# 创建一个集合, 默认会去重
allNum = set()

# 循环N次
for count in range(N):
    # 随机生成一个1-1000之间的随机数;
    num = random.randint(1, 1000)
    allNum.add(num)
print("生成的数据:", allNum)
# **). 然后再把这些数从大到小排序
# 集合没有排序的方法， 列表有排序的方法
allNum = list(allNum)
print("正在排序.....")
# 由大到小进行排序;
allNum.sort(reverse=True)
print("排序结果:", allNum)


