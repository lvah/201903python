# -*-coding: utf-8-*-
import xlwt
import pandas as pd
def attr_trans(x):
    """
    x的内容如下:
           SYS_NAME     NAME       TARGET_ID    DESCRIPTION        ENTITY   VALUE         COLLECTTIME
    184   财务管理系统  CWXT_DB    184          磁盘已使用大小     C:\      34793245.31     2014-11-16
    185   财务管理系统  CWXT_DB    184          磁盘已使用大小     D:\      89377527.25     2014-11-16
    """
    result = pd.Series(index=['SYS_NAME', 'CWXT_DB:184:C:\\', 'CWXT_DB:184:D:\\', 'COLLECTTIME'])
    result['SYS_NAME'] = x['SYS_NAME'].iloc[0]          # 财务管理系统
    result['COLLECTTIME'] = x['COLLECTTIME'].iloc[0]    # 2014-11-16
    result['CWXT_DB:184:C:\\'] = x['VALUE'].iloc[0]     # 34793245.31
    result['CWXT_DB:184:D:\\'] = x['VALUE'].iloc[1]     # 89377527.25


    # print('******************')
    # print(result)
    return result

if __name__ == '__main__':
    discfile = 'data/discdata.xls'
    transformeddata = 'data/discdata_processed.csv'
    # 加载excel文件
    data = pd.read_excel(discfile)


    # 目前只对target_id=184的数据进行处理；获取所有已经使用的容量;
    data = data[data['TARGET_ID'] == 184].copy()

    # 按时间分组
    data_group = data.groupby('COLLECTTIME')


    #  # 将函数应用到由各列或行形成的数组上。DataFrame的apply方法可以实现此功能
    data_processed = data_group.apply(attr_trans)

    print(data_processed.head(5))

    data_processed.to_csv(transformeddata, index=False)