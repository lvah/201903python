import random
from pyecharts import options as opts
from pyecharts.charts import Scatter


# 获取散点图需要绘制的数据信息;
x = list(range(10))
y1 = [random.randint(1, 20) for i in range(10)]
y2 = [random.randint(1, 20) for j in range(10)]
y3 = [random.randint(1, 20) for _ in range(10)]


# 实例化Scatter类未scatter对象, 并添加x和y对应的点;
scatter = (
    Scatter()
    .add_xaxis(x)
    .add_yaxis("商品A", y1)
    .add_yaxis("商品B", y2)
    .add_yaxis("商品C", y3)
    .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
)
# 将散点图信息保存到文件中;
scatter.render()