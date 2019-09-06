"""
需求1:
    获取所有男生的身高, 求平均值;获取所有女生的身高, 求平均值;并绘制柱状图显示


需求2:
    获取所有男生的体重, 求平均值;获取所有女生的体重, 求平均值;并绘制柱状图显示
"""
import numpy as np
def get_avg_height():
    fname = "doc/eg6-a-student-data.txt"
    # 定义读取列的数据类型
    dtype = np.dtype([('gender', '|S1'), ('height', 'f2')])
    # 读取文件的第2列和第3列， 前9行忽略;
    data = np.loadtxt(fname=fname, dtype=dtype, skiprows=9,
                      usecols=(1, 3))
    # print(data)
    # print(data['gender'])
    # print(data['height'])
    # print(data['height'][data['gender'] == b'M'].mean())
    # print(data['height'][data['gender'] == b'F'].mean())

    # 判断是否性别为那男的表达式
    isMale = data['gender'] == b'M'
    male_avg_height = data['height'][isMale].mean()
    # ~代表取反
    female_avg_height = data['height'][~isMale].mean()
    return male_avg_height, female_avg_height
def parser_weight(weight):
    # 对于体重数据的处理, 如果不能转换为浮点数据类型, 则返回缺失值;
    try:
        return  float(weight)
    except ValueError as e:
        return  -99
def get_avg_weight():
    fname = "doc/eg6-a-student-data.txt"
    # 定义读取列的数据类型
    dtype = np.dtype([('gender', '|S1'), ('weight', 'f2')])
    # 读取文件的第2列和第4列， 前9行忽略;
    data = np.loadtxt(fname=fname, dtype=dtype, skiprows=9,
                      usecols=(1, 4), converters={4:parser_weight})

    # 判断是否性别为男的平均身高
    isMale = data['gender'] == b'M'

    # 判断是否性别为男的平均体重
    is_weight_vaild = data['weight'] > 0
    male_avg_weight = data['weight'][isMale & is_weight_vaild].mean()
    female_avg_weight = data['weight'][~isMale & is_weight_vaild].mean()
    return  male_avg_weight, female_avg_weight
if __name__ == '__main__':
    print(get_avg_height())
    print(get_avg_weight())