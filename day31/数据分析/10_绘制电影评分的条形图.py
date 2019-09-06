import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('douban.csv')
# 获取评分的区间
counts = {}
scores = df['score']
for score in scores:
    try:
        # 'score'
        score = float(score.strip())
    except Exception as e:
        continue
    if 9.5 < score <= 10:
        counts['9.5~10'] = counts.get('9.5~10', 0) + 1
    elif 9.0 < score <= 9.5:
        counts['9.0~9.5'] = counts.get('9.0~9.5', 0) + 1
    elif 8.7 < score <= 9.0:
        counts['8.7~9.0'] = counts.get('8.7~9.0', 0) + 1
    elif 8.5 < score <= 8.7:
        counts['8.5~8.7'] = counts.get('8.5~8.7', 0) + 1
    else:
        counts['other'] = counts.get('other', 0)
plt.bar(counts.keys(), counts.values(), color='g')
plt.show()
