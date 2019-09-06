import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



# csv, excel, json........
# 1). csv文件的写入

df = pd.DataFrame(
    {'province': ['陕西', '陕西', '四川', '四川', '陕西'],
     'city': ['咸阳', '宝鸡', '成都', '成都', '宝鸡'],
     'count1': [1, 2, 3, 4, 5],
     'count2': [1, 2, 33, 4, 5]
     }
)

# print(df)
#
# df.to_csv('doc/csvFile.csv', index=False)  # index=False不存储行索引
# print("csv文件保存成功")
#
# # 2). csv文件的读取
# df2 = pd.read_csv('doc/csvFile.csv')
# print(df2)

# 3). excel文件的写入
df.to_excel("/tmp/excelFile.xlsx", sheet_name="省份统计")
print("excel文件保存成功")

