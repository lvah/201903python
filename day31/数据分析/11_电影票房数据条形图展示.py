"""
文件名: .py
创建时间: 2019-01-14 23:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
import random
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

names = ["战狼%s" %(i) for i in range(10)]
# print(names)
scores = [random.randint(50, 100) for i in range(10)]

# 设置图形大小
plt.figure(figsize=(20, 15), dpi=80)

# 绘制条形图
plt.barh(range(len(names)), scores, height=0.5, color='orange')

# 设置字体格式
myfont = FontProperties(fname='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc', size=32)

# # 设置字符串到x轴
# plt.xticks(range(len(names)), labels=names, fontproperties=myfont)

# 设置字符串到y轴
plt.yticks(range(len(names)), labels=names, fontproperties=myfont)


# 绘制网格
plt.grid(0.1)

# 显示图像
plt.show()