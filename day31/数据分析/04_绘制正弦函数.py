# y = sinx
# y = cosx


import numpy as np
import matplotlib.pyplot as plt
# 计算正弦和余弦曲线上点的 x 和 y 坐标,
# np.arange([start, ]stop, [step, ]dtype=None): arange函数用于创建等差数组
"""
start:可忽略不写，默认从0开始;起始值
stop:结束值；生成的元素不包括结束值
step:可忽略不写，默认步长为1；步长
dtype:默认为None，设置显示元素的数据类型
"""
x = np.arange(0,  3  * np.pi,  0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 设置标题和xy轴信息;
plt.title("sine wave form")
plt.xlabel('x')
plt.ylabel('y')


# 使用 matplotlib 来绘制点
plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
