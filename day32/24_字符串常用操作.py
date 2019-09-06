
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

series1= pd.Series(['$A:1', '$B:2', '$C:3', np.nan, '$cat:3'])
print(series1)

# 将所有的字母转换为小写字母， 除了缺失值
print(series1.str.lower())


# 将所有的字母转换为大写字母， 除了缺失值
print(series1.str.upper())

# 分离
print(series1.str.split(":"))

# 去掉左右两端的某个字符
print(series1.str.strip('$'))
