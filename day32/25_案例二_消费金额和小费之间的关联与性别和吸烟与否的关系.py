"""
文件内容: 总消费金额， 小费金额， 性别， 是否抽烟， 日期， 时间， 星期
需求:
    - 分别吸烟顾客与不吸烟顾客的消费金额与小费之间的散点图;
    - 女性与男性中吸烟与不吸烟顾客的消费金额与小费之间的散点图关系;
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


filename = 'doc/tips.csv'
data = pd.read_csv(filename)
# print(data.head())
# print(data.info())


# # 实现吸烟顾客消费金额与小费之间的散点图
# smoker = data[data['smoker'] == 'Yes']
# # print(smoker.head())
# x_total_bill = smoker['total_bill']
# y_tip = smoker['tip']
#
# from pyecharts import  Scatter
# scatter = Scatter("吸烟顾客消费金额与小费之间的散点图")
# scatter.add("", x_total_bill, y_tip)
# scatter.render()



# # 实现不吸烟顾客消费金额与小费之间的散点图
# no_smoker = data[data['smoker'] != 'Yes']
# # print(smoker.head())
# x_total_bill = no_smoker['total_bill']
# y_tip = no_smoker['tip']
#
# from pyecharts import  Scatter
# scatter = Scatter("不吸烟顾客消费金额与小费之间的散点图")
# scatter.add("", x_total_bill, y_tip)
# scatter.render()



# 女性中吸烟与不吸烟顾客的消费金额与小费之间的散点图关系;
# 1). 获取所有吸烟的用户信息
smoker = data[data['smoker'] == 'Yes']
# 2).从所有的吸烟用户中找出性别为女的用户信息;
female_smoker = smoker[smoker['sex']=='Female']


# 1). 获取所有不吸烟的用户信息
no_smoker = data[data['smoker'] != 'Yes']
# 2).从所有的吸烟用户中找出性别为女的用户信息;
female_no_smoker = no_smoker[no_smoker['sex']=='Female']
# 3). 绘制散点图
from pyecharts import  Scatter
scatter = Scatter("消费金额与小费之间的散点图")
scatter.add("吸烟女顾客", female_smoker['total_bill'], female_smoker['tip'])
scatter.add("不吸烟女顾客", female_no_smoker['total_bill'], female_no_smoker['tip'])

scatter.render()