# def sum(arg1:int, arg2:int)->int:
#     """
#     求两个数的和
#     :param arg1:
#     :param arg2:
#     :return:
#     """
#     # result = arg1 + arg2
#     # return  result
#     return  arg1 + arg2
#
# print("运行结果: ", sum(1, 2))
# print("运行结果: ", sum(3, 5))
#
#
# print("匿名函数".center(50, '*'))
# # lambda 形参：返回值
# lambda_sum = lambda arg1, arg2 :  arg1+arg2
# print("运行结果: ", lambda_sum(1, 2))
# print("运行结果: ", lambda_sum(3, 5))
#
#
# def mypow(num1, num2=2):
#     """
#     num1的num2次方
#     :param num1:
#     :param num2:
#     :return:
#     """
#     return  num1 ** num2
#
# lambda_mypow = lambda num1, num2=2:num1 ** num2
# print(lambda_mypow(2))
# print(lambda_mypow(2, 3))


# def myFun(num1, num2, fun=pow):
#     print('num1=', num1, end=', ')
#     print('num2=', num2, end=', ')
#     print("result=", fun(num1, num2))
#
# myFun(1, 2, lambda x, y: x + y)
# myFun(1, 2, lambda x, y: x * y)
# myFun(1, 2, lambda x, y: x ** y)
# myFun(1, 2)


# 排序
#       1). 列表有li.sort()
#       2). sorted()函数

# nums = {3, 1, 45, 2}
# nums = list(nums)
# nums.sort(reverse=True)
# print(nums)


# sort_nums = sorted(nums)
# print(nums)
# print(sort_nums)


# 复杂的排序:
def pretty_show(goods):
    """
    以表格的方式友好的显示商品信息
    :param goods:
    :return:
    """
    # 导入prettytable模块里面的类PrettyTable, 并起一个别名pt
    from  prettytable import  PrettyTable as pt
    # 实例化表格对象
    table = pt()
    # 往表格里面添加表头信息
    table.field_names = ["Name", "Price", "Count"]
    # 依次添加每一行商品的信息；
    for good in goods:
        table.add_row(good)
    # 最终显示表格
    print(table)




goods = [
    # 商品名称 商品价格  商品的数量
    ["电脑", 5999, 100],
    ["电视", 1999, 1000],
    ["手机", 2999, 50],

]
pretty_show(goods)
# sorted方法， key：按照什么进行排序， lambda x: x[1]  x=["电脑", 5999, 100], x[1],
# reverse=True按照商品的价格进行排序
sort_goods = sorted(goods, key=lambda x: x[1], reverse=True)
# print(sort_goods)
print("按照价格进行排序".center(30, '*'))
pretty_show(sort_goods)


# 按照商品的数量进行排序
sort_count_goods = sorted(goods, key=lambda  x:x[2])
# print(sort_count_goods)
print("按照商品数量进行排序".center(30, '*'))
pretty_show(sort_count_goods)



# *********************************# 字典的排序:*******************************
# goods = {
#     # 商品名称 商品价格  商品的数量
#     '001': ["电脑", 5999, 100],
#     '002': ["电视", 1999, 1000],
#     '003': ["手机", 2999, 50],
# }
# # 按照商品的价格进行排序
# # 按照商品的数量进行排序(提示： 使用字典的items方法)
# # print(goods.items())
# sorted_by_price = sorted(goods.items(), key=lambda x:x[1][1])
# print(sorted_by_price)
# sorted_by_count = sorted(goods.items(), key=lambda x:x[1][2])
# print(sorted_by_count)