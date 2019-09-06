# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
def draw():
    data = pd.read_excel('data/discdata.xls')
    str1 = 'C:\\'
    str2 = 'D:\\'
    dataC = data[(data['DESCRIPTION'] == '磁盘已使用大小') & (data['ENTITY'] == str1)]
    dataD = data[(data['DESCRIPTION'] == '磁盘已使用大小') & (data['ENTITY'] == str2)]
    dataC.plot(y='VALUE', label='C')
    dataD.plot(y='VALUE', label='D')
    plt.show()


def draw1():
    from pandas.plotting import register_matplotlib_converters
    register_matplotlib_converters()
    data = pd.read_excel('data/discdata.xls')
    str1 = 'C:\\'
    str2 = 'D:\\'
    dataC = data[(data['DESCRIPTION'] == '磁盘已使用大小') & (data['ENTITY'] == str1)]
    dataD = data[(data['DESCRIPTION'] == '磁盘已使用大小') & (data['ENTITY'] == str2)]
    plt.plot(dataC['COLLECTTIME'], dataC['VALUE'], label='C', color='r')
    plt.plot(dataD['COLLECTTIME'], dataD['VALUE'], label='D', color='g')
    plt.xlabel('date')
    plt.ylabel('value')
    plt.xticks(rotation=45)
    plt.grid(alpha=0.3)
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    draw1()