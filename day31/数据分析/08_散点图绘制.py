import random
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
"""
绘制10月和三月温度变化的散点图
"""

# 字体设置
myfont = FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc", size=14)
titlefont = FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc", size=25)

# x轴和Y轴数据
march_y = [random.randint(10, 20) for i in range(31)]
october_y = [random.randint(20, 30) for j in range(31)]
x = range(1, 32) # 1, 2, 3, ...31


# 设置图形大小
plt.figure(figsize=(10, 5), dpi=100)

# 绘制散点图
plt.subplot(2,  1,  1)
plt.scatter(x, march_y, )
# 调整刻度
_x3_labels = ["3月{}日".format(_) for _ in x]
# rotation: 旋转
plt.xticks(x[::3], labels=_x3_labels[::3], fontproperties=myfont, rotation=45)
# x， y和标题的说明
plt.xlabel("月份", fontproperties=myfont)
plt.ylabel("温度(摄氏度)", fontproperties=myfont)
plt.title("3月温度变化散点图", fontproperties=titlefont)

plt.subplot(2,  1,  2)
plt.scatter(x, october_y)
_x10_labels = ["10月{}日".format(_) for _ in x]
plt.xticks(x[::3], labels=_x10_labels[::3], fontproperties=myfont, rotation=45)
# x， y和标题的说明
plt.xlabel("月份", fontproperties=myfont)
plt.ylabel("温度(摄氏度)", fontproperties=myfont)
plt.title("10月温度变化散点图", fontproperties=titlefont)

# 添加网格
plt.grid(alpha=0.5)

# 显示图像
plt.show()