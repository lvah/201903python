import numpy as np
import matplotlib.pyplot as plt

# 设置x和y
x = np.arange(1, 11)  # [1, 2, 3,.....10]
y1 = x + 5
y2 = x ** 2 + 5
y3 = x ** 3 + 5

# 设置标题， x周和y轴含义
plt.title("Matplotlib demo")
plt.xlabel("x")
plt.ylabel("y")


# label是一个子图多条图像时，设置的图例名称;
plt.plot(x, y1, 'ob', label='y=x+5')  # 'o'代表圆点， ‘b’颜色， 蓝色blue
plt.plot(x, y2, "*y", label='y=x**2+5')
plt.plot(x, y3, label='y=x**3+5')

# 设置图例位置
plt.legend(loc="upper left")

# # 添加网格
plt.grid(alpha=0.1)

plt.show()
