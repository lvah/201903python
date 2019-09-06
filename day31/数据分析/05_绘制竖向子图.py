import numpy as np
import matplotlib.pyplot as plt

# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot, 位于第一行
plt.subplot(2,  1,  1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sin(x)')
# 将第二个 subplot 激活，并绘制第二个图像， 位于第2行;
plt.subplot(2,  1,  2)
plt.plot(x, y_cos)

plt.title('Cos(x)')
# 展示图像
plt.show()
