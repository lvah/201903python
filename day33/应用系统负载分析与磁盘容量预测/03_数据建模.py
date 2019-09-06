# -*- coding:utf-8 -*-

"""
# 1. ARIMA模型
    ARIMA模型的全称是自回归移动平均模型，是用来预测时间序列的一种常用的统计模型，一般记作ARIMA(p,d,q)。

# 2. ARIMA的适应情况
    ARIMA模型相对来说比较简单易用。在应用ARIMA模型时，要保证以下几点：
        时间序列数据是相对稳定的，总体基本不存在一定的上升或者下降趋势，如果不稳定可以通过差分的方式来使其变稳定。
        非线性关系处理不好，只能处理线性关系

# 3. 判断时序数据稳定
    基本判断方法：稳定的数据，总体上是没有上升和下降的趋势的，是没有周期性的，方差趋向于一个稳定的值。

# 4. ARIMA数学表达
    ARIMA(p,d,q)，其中
        p是数据本身的滞后数，是AR模型即自回归模型中的参数。
        d是时间序列数据需要几次差分才能得到稳定的数据。
        q是预测误差的滞后数，是MA模型即滑动平均模型中的参数。


"""

import pandas as pd
def stationarityTest():
    '''
    检验时间序列稳定性:
    平稳性检验:
        为了确定原始数据序列中没有随机趋势或确定趋势，需要对数据进行平稳性检验，否则将会产生“伪回归”的现象。采用ADF方法来进行平稳性检验。
        p值小于0.05认为是平稳的
    :return:
    '''
    discfile = 'data/discdata_processed.csv'
    predictnum = 5
    data = pd.read_csv(discfile)  # 100
    data = data.iloc[: len(data) - predictnum] # 95
    # 平稳性检验
    from statsmodels.tsa.stattools import adfuller as ADF  # 单位根检测法
    diff = 0
    adf = ADF(data['CWXT_DB:184:D:\\'])
    # print(adf)
    # p值小于0.05认为是平稳的
    while adf[1] > 0.05:
        diff = diff + 1
        adf = ADF(data['CWXT_DB:184:D:\\'].diff(diff).dropna())
    print(u'原始序列经过%s阶差分后归于平稳，p值为%s' % (diff, adf[1]))
def whitenoiseTest():
    '''

    白噪声检验:
        为了验证序列中有用的信息是否已被提取完毕，需要对序列进行白噪声检验。
        如果序列检验为白噪声序列，就说明序列中有用的信息已经被提取完毕了，剩下的全是随机扰动，无法进行预测和使用。
        采用LB统计量的方法进行白噪声检验。
    :return:

    '''
    discfile = 'data/discdata_processed.csv'
    data = pd.read_csv(discfile)
    data = data.iloc[: len(data) - 5]
    # 白噪声检验
    from statsmodels.stats.diagnostic import acorr_ljungbox
    [[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'], lags=1)
    if p < 0.05:
        print(u'原始序列为非白噪声序列，对应的p值为：%s' % p)
    else:
        print(u'原始该序列为白噪声序列，对应的p值为：%s' % p)

    [[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'].diff().dropna(), lags=1)

    if p < 0.05:

        print(u'一阶差分序列为非白噪声序列，对应的p值为：%s' % p)

    else:

        print(u'一阶差分该序列为白噪声序列，对应的p值为：%s' % p)
def findOptimalpq():
    '''
    得到模型参数:
        获取时间序列数据
        观测数据是否为平稳的，否则进行差分，化为平稳的时序数据,确定d
        通过观察自相关系数ACF与偏自相关系数PACF确定q和p

    :return:
    '''
    discfile = 'data/discdata_processed.csv'
    data = pd.read_csv(discfile, index_col='COLLECTTIME')
    data = data.iloc[: len(data) - 5]
    xdata = data['CWXT_DB:184:D:\\']
    from statsmodels.tsa.arima_model import ARIMA
    # 定阶

    # 一般阶数不超过length/10
    pmax = int(len(xdata) / 10)
    qmax = int(len(xdata) / 10)
    # bic矩阵
    bic_matrix = []
    for p in range(pmax + 1):
        tmp = []
        for q in range(qmax + 1):
            try:
                tmp.append(ARIMA(xdata, (p, 1, q)).fit().bic)
            except:
                tmp.append(None)
        bic_matrix.append(tmp)
    bic_matrix = pd.DataFrame(bic_matrix)
    # 先用stack展平，然后用idxmin找出最小值位置。
    p, q = bic_matrix.stack().astype('float64').idxmin()
    print(u'BIC最小的p值和q值为：%s、%s' % (p, q))
def arimaModelCheck():

    '''

    模型检验

    :return:

    '''

    discfile = 'data/discdata_processed.csv'

    # 残差延迟个数

    lagnum = 12



    data = pd.read_csv(discfile, index_col='COLLECTTIME')

    data = data.iloc[: len(data) - 5]

    xdata = data['CWXT_DB:184:D:\\']

    # 建立ARIMA(0,1,1)模型

    from statsmodels.tsa.arima_model import ARIMA

    # 建立并训练模型

    arima = ARIMA(xdata, (0, 1, 1)).fit()

    # 预测

    xdata_pred = arima.predict(typ='levels')

    # 计算残差

    pred_error = (xdata_pred - xdata).dropna()



    from statsmodels.stats.diagnostic import acorr_ljungbox

    # 白噪声检验

    lb, p = acorr_ljungbox(pred_error, lags=lagnum)

    # p值小于0.05，认为是非白噪声。

    h = (p < 0.05).sum()

    if h > 0:

        print(u'模型ARIMA(0,1,1)不符合白噪声检验')

    else:

        print(u'模型ARIMA(0,1,1)符合白噪声检验')
def calErrors():

    '''
    误差计算

    :return:

    '''

    # 参数初始化

    file = './data/predictdata.xls'

    data = pd.read_excel(file)



    # 计算误差

    abs_ = (data[u'预测值'] - data[u'实际值']).abs()

    mae_ = abs_.mean()  # mae

    rmse_ = ((abs_ ** 2).mean()) ** 0.5

    mape_ = (abs_ / data[u'实际值']).mean()



    print(u'平均绝对误差为：%0.4f，\n均方根误差为：%0.4f，\n平均绝对百分误差为：%0.6f。' % (mae_, rmse_, mape_))

if __name__ == '__main__':
    stationarityTest()
    whitenoiseTest()
    findOptimalpq()
    arimaModelCheck()
    calErrors()