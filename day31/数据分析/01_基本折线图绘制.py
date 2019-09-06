import random
from matplotlib import pyplot as plt

# 指的是时间: 2 4 6 8 .......24
x = range(2, 26, 2)
# 温度
y = [random.randint(10, 30) for i in range(12)]  # 2 10

# 设置图形的大小;
plt.figure(figsize=(20, 8), dpi=100)
# 传递x和y的值
plt.plot(x, y)
# x轴和y轴显示的范围;
plt.xticks(x[:])
plt.yticks(range(min(y), max(y)+1))
# plt.show()
plt.savefig("./hello.png", dpi=100)