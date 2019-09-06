"""
data.csv文件中存储了股票的信息， 其中第4-8列,即EXCEL表格中的D-H列,
分别为股票的开盘价,最高价,最低价,收盘价,成交量。
分析角度:
    1. 计算成交量加权平均价格
    概念:成交量加权平均价格,英文名VWAP(Volume-Weighted Average Price,成交量加权平均价格)是一个非常重要的经
    济学量,代表着金融资产的“平均”价格。
    某个价格的成交量越大,该价格所占的权重就越大。VWAP就是以成交量为权重计算出来的加权平均值。

    2. 计算最大值和最小值: 计算股价近期最高价的最大值和最低价的最小值
    3. 计算股价近期最高价的最大值和最小值的差值;----(极差)
    计算股价近期最低价的最大值和最小值的差值
    4. 计算收盘价的中位数
    5. 计算收盘价的方差
    6. 计算对数收益率， 股票收益率、年波动率及月波动率
     ***收盘价的分析常常是基于股票收益率的。
     股票收益率又可以分为简单收益率和对数收益率。
            简单收益率：是指相邻两个价格之间的变化率。  diff
            对数收益率：是指所有价格取对数后两两之间的差值。
            # [1, 2,3 4]   ======>[-1, ]
    ***使用的方法: NumPy中的diff函数可以返回一个由相邻数组元素的差值构成的数组。
    不过需要注意的是，diff返回的数组比收盘价数组少一个元素。
    ***在投资学中,波动率是对价格变动的一种度量,历史波动率可以根据历史价格数据计算得出。计算历史波动率时,需要用
    到对数收益率。
        年波动率等于对数收益率的标准差除以其均值,再乘以交易日的平方根,通常交易日取252天。
        月波动率等于对数收益率的标准差除以其均值,再乘以交易月的平方根。通常交易月取12月。
    7. 获取该时间范围内交易日周一、周二、周三、周四、周五分别对应的平均收盘价
    8. 平均收盘价最低,最高分别为星期几

"""


import numpy as np

print("**********************************************")

params1 = dict(
    fname="doc/data.csv",
    delimiter=",",   # 指定文件分隔符;
    usecols=(6, 7),
    unpack=True)  # 是否解包,返回两个一维数组;
# 收盘价,成交量
endPrice, countNum = np.loadtxt(**params1)
# print(endPrice, countNum)
VWAP = np.average(endPrice, weights=countNum)
print("1. 计算成交量加权平均价格：", VWAP)

print("**********************************************")
params2 = dict(
    fname="doc/data.csv",
    delimiter=",",
    usecols=(4, 5),
    unpack=True)
# 最高价和最低价
highPrice, lowPrice = np.loadtxt(**params2)

# 最高价的最大值和最低价的最小值
print("2.最高价的最大值： ", highPrice.max())
print("2.最低价的最小值： ", lowPrice.min())

print("**********************************************")
# 计算股价近期最高价的最大值和最小值的差值;----(极差)
#     计算股价近期最低价的最大值和最小值的差值

print("3. 近期最高价的极差： ", np.ptp(highPrice))
print("3. 近期最低价的极差： ", np.ptp(lowPrice))

print("**********************************************")
# 计算收盘价的中位数
print("4. 计算收盘价的中位数:", np.median(endPrice))

print("**********************************************")
# 计算收盘价的方差
print("5. 计算收盘价的方差:", np.var(endPrice))

print("**********************************************")
def get_week(date):
    """根据传入的日期28-01-2011获取星期数, 0-星期一 1-"""
    from datetime import datetime
    # 默认传入的不是字符串， 是bytes类型;
    date = date.decode('utf-8')
    return datetime.strptime(date, "%d-%m-%Y").weekday()
params3 = dict(
    fname="doc/data.csv",
    delimiter=",",
    usecols=(1, 6),
    converters={1: get_week},
    unpack=True)
# 星期数和收盘价
week, endPrice = np.loadtxt(**params3)
# print(week, endPrice)
allAvg = []
for weekday in range(5):
    # 依次判断获取星期一的平均收盘价, .......星期五
    average = endPrice[week == weekday].mean()
    allAvg.append(average)
    print("7. 星期%s的平均收盘价：%s" % (weekday + 1, average))

# print(allAvg)

print("**********************************************")
# [12, 23, 34, 45, 56]
print("8.平均收盘价最低是星期", np.argmin(allAvg) + 1)
print("8. 平均收盘价最高是星期", np.argmax(allAvg) + 1)
#

print("***********************************************************")
# 简单收益率
simpleReturn = np.diff(endPrice)
print(simpleReturn)
# 对数收益率: 所有价格取对数后两两之间的差值。
logReturn = np.diff(np.log(endPrice))
print("6. 对数收益率:", logReturn)
# 年波动率等于对数收益率的标准差除以其均值,再乘以交易日的平方根,通常交易日取252天。
annual_vol = logReturn.std()/logReturn.mean()*np.sqrt(252)
print("6. 年波动率:",  annual_vol)
#  月波动率等于对数收益率的标准差除以其均值,再乘以交易月的平方根。通常交易月取12月。
month_vol = logReturn.std()/logReturn.mean()*np.sqrt(12)
print("6. 月波动率:", month_vol)