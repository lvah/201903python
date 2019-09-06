"""
Tushare是一个免费、开源的python财经数据接口包。主要实现对股票等金融数据从数据采集、清洗加工 到 数据存储的过程，
能够为金融分析人员提供快速、整洁、和多样的便于分析的数据。其网址为：http://tushare.org/
"""
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt

print('***********************上下连接******************************************')
print("正在获取股票 600036 一月和七月前5天的股票数据............")
report1 = ts.get_k_data('600036', start='2017-01-01', end='2017-01-05')
print("股票一月的数据: \n", report1)
report2 = ts.get_k_data('600036', start='2017-07-01', end='2017-07-05')
print("股票七月的数据: \n", report2)
concat_report = pd.concat([report1, report2], axis=0)
print("拼接结果: \n", concat_report)

print('***********************左右连接******************************************')
print("正在获取股票八月和上证股票数据， 并实现走势对比............")
stock = ts.get_k_data('600036', start='2017-08-01', end='2017-08-31')
sh = ts.get_k_data('sh', start='2017-08-01', end='2017-08-31')
trend = pd.concat([stock, sh], axis=1)
print("水平拼接的结果:  \n", trend.head())


def show1():
    # keys时字原有基础上新加了索引值;
    trend = pd.concat([stock, sh], axis=1, keys=['zsyh', 'sh'])
    print("水平拼接并添加新的索引: \n", trend.head())
    print('绘制图形')
    df = trend.loc[:, [('zsyh', 'close'), ('sh', 'close')]]
    # print(df.head(5))
    # 绘制双Y轴图形
    df.plot(kind='line', secondary_y=[('sh', 'close')])
    plt.show()


def show2():
    print('绘制图形')
    trend = pd.concat([stock, sh], axis=1, ignore_index=True)
    # print(trend)
    # 对列索引重命名
    trend.rename(columns={2: 'zsyh_close', 9: 'sh_close'}, inplace=True)
    df = trend.loc[:, ['zsyh_close', 'sh_close']]
    df.plot(kind='line', secondary_y=['sh_close'])
    plt.show()


if __name__ == '__main__':
    show2()
