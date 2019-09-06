import random
import matplotlib.pyplot as plt

names = ['电影%s' %(i) for i in range(100)]
times = [random.randint(40, 140) for i in range(100)]


# hist代表直方图， times为需要统计的数据， 20为统计的组数.
plt.hist(times, 20)

plt.show()




