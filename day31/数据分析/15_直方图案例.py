"""
文件名: .py
创建时间: 2019-01-16 17:
作者: lvah
联系方式: 976131979@qq.com
代码描述:




# 数据来源: https://en.wikipedia.org/wiki/Histogram#Examples
The U.S. Census Bureau found that there were 124 million people who work outside of
their homes.[9] Using their data on the time occupied by travel to work, the table
below shows the absolute number of people who responded with travel times "at least
30 but less than 35 minutes" is higher than the numbers for the categories above and
 below it. This is likely due to people rounding their reported journey time.[citation
 needed] The problem of reporting values as somewhat arbitrarily rounded numbers is a
 common phenomenon when collecting data from people.[citation needed]


Data by absolute numbers
Interval,Width,Quantity,Quantity/width
0,5,4180,836
5,5,13687,2737
10,5,18618,3723
15,5,19634,3926
20,5,17981,3596
25,5,7190,1438
30,5,16369,3273
35,5,3212,642
40,5,4122,824
45,15,9200,613
60,30,6461,215
90,60,3435,57


"""

import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc')

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 57]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制条形图
plt.bar(range(12), quantity, width=1)

# 设置x轴的刻度
_x = [i - 0.5 for i in range(13)]
_x_labels = interval + [150]
plt.xticks(_x, _x_labels)

# 绘制网格
plt.grid(alpha=0.1)
# 显示图片
plt.show()