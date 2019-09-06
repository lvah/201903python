import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

names = ['来电狂想', '战狼', '无名之辈']
scores_14 = [2358, 388, 789]
scores_15 = [9078, 328, 489]
scores_16 = [2458, 3868, 7389]

# 设置图形大小
plt.figure(figsize=(20, 15), dpi=100)
# 设置字体
myfont = FontProperties(fname='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc', size=32)

# 绘制条形图
namesNum = range(len(names))
bar_width = 0.3
plt.bar(namesNum, scores_14, color='pink', width=0.3, label='9月14日')
plt.bar([i + bar_width for i in namesNum], scores_15, color='orange',
        width=0.3, label='9月15日')
plt.bar([i + bar_width * 2 for i in namesNum], scores_16, color='black',
        width=0.3, label='9月16日')

# 设置x轴
_x_ticks = [i + bar_width for i in namesNum]
plt.xticks(_x_ticks, names, fontproperties=myfont)

plt.legend(loc='upper right', prop=myfont)
# 显示图像
plt.show()