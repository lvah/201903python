"""
根据用于指定月份，打印该月份所属的季节。
	提示: 3,4,5 春季 6,7,8 夏季  9,10,11 秋季 12, 1, 2 冬季
	考察点: 列表的成员操作符, if判断语句
	'3' in ['3', '4', '5']
"""
# while, for, if, elif, else
while True:
    month = input('月份(q退出):')
    # if month in ['3','4','5']:
    if month in '345':
        print("春季")
    elif   month in '678':
        print("夏季")
    elif   month in ['9', '10', '11']:
        print("秋季")
    elif   month in ['12', '1', '2']:
        print("冬季")
    elif month == 'q':
        print("查询结束......")
        break
    else:
        print("请输入正确的月份")