"""
数据分析
"""
import pandas as pd
from config import  *
import matplotlib.pyplot as plt
import  matplotlib


#配置中文字体和修改字体大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.size'] = 10
# 读取csv文件的内容;
df = pd.read_csv(csvFileName)

#  获取数据的前5行;
# print(df.head(5))
# # 获取文件中的某一列数据
# thirdTypes = df['thirdType']
# # 对数据进行分组统计;
# groupTypesCount = thirdTypes.value_counts()
# print(thirdTypes)
# print(groupTypesCount)


def show_second_type():
   # 获取职位类别分类并分组统计
   secondType_Series = df['secondType'].value_counts()
   print(secondType_Series)
   # 设置图形的大小;
   plt.figure(figsize=(10,5))
   # 绘制条形图;bar: 条形图，
   secondType_Series.plot.bar()
   # # 展示图形
   plt.show()




if __name__ == '__main__':
    show_second_type()