# DataFrame: 二维数组

import pandas as pd
datas = [
    {'user':'root', 'pwd':'root'},
    {'user':'westos', 'pwd':'123'},
]

df = pd.DataFrame(datas)
# # print(df)

# ***************************快速存储为csv文件************************
# """
#     sep: 输出文件的字段分隔符, 默认为逗号;
#     header: 是否写出列名;
#     index: 是否写入行名称(索引);
#
# """
# df.to_csv('doc/datas.csv', sep=':', header=True, index=False)


datas1 = [
    {'user':'root1', 'pwd':'root1'},
    {'user':'westos1', 'pwd':'1234'},
]

df1 = pd.DataFrame(datas1)


datas2 = [
    {'user':'root2', 'pwd':'root2'},
    {'user':'westos2', 'pwd':'1234'},
]
df2 = pd.DataFrame(datas2)

dfs = [df, df1, df2]
#  # 拼接获取的所有信息, axis=0代表往跨行（down)，而axis=1代表跨列（across)
df_results = pd.concat(dfs, axis=0)
print(df_results)
