import random
from pyecharts import options as opts
from pyecharts.charts import Scatter, Line


# 获取散点图需要绘制的数据信息;
x = []
y = []
with open('cpu.txt') as f:  # 以读的方式打开文件
    for line in f:          # 依次遍历文件的每一行内容
        time, per = line.split()    # 返回时间和对应时间的cpu占有率
        x.append(time)
        y.append(per)

# 实例化Scatter类未scatter对象, 并添加x和y对应的点;
scatter = (
    Line()
    .add_xaxis(x)
    .add_yaxis("", y)

    .set_global_opts(title_opts=opts.TitleOpts(title="Cpu占有率散点图"))
)
# 将散点图信息保存到文件中;
scatter.render()
