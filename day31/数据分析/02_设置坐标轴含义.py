import random
from matplotlib import pyplot as plt, font_manager
import matplotlib

#  fc-list  :lang=zh  =====> 列出电脑上所有的中文字体库
myfont = font_manager.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc", size=12)
titlefont = font_manager.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc", size=32, weight=True)

y = [random.randint(20, 35) for i in range(120)]
x = range(0, 120)
plt.figure(figsize=(10, 5), dpi=100)
plt.plot(x, y)


plt.xlabel("时间", fontproperties=myfont)
plt.ylabel("温度(摄氏度)", fontproperties=myfont)
plt.title("10点到12点每分钟时间的时间变化情况", fontproperties=titlefont)
plt.show()
plt.savefig('./hello.png')