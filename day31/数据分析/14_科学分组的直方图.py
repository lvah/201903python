import random
import matplotlib.pyplot as plt

names = ['电影%s' % (i) for i in range(100)]
times = [random.randint(40, 140) for i in range(100)]

# 如何实现数据的分组?   组数 = 极差 / 组距; 极差= max - min
#  数据为100个以内， 一般分为5~12组;

bin_width = 3  # 设置组距为3;
num_bins = (max(times) - min(times)) // bin_width  # 合理确定组数
print(num_bins)
# hist代表直方图， times为需要统计的数据， 20为统计的组数.
# plt.hist(times, num_bins)
# plt.hist(times, [min(times) + i * bin_width for i in range(num_bins)])
# normed: bool, 是否绘制频率分布直方图， 默认为频数直方图.
plt.hist(times, [min(times) + i * bin_width for i in range(num_bins)], normed=1)

# x轴的设置
plt.xticks(list(range(min(times), max(times)))[::bin_width], rotation=45)

# 设置网格
plt.grid(True, linestyle='-.', alpha=0.5)
plt.show()