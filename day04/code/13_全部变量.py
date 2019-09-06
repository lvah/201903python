#   在函数外边定义的变量叫做全局变量
allMoney = 100

def save_money(money):
    """
    存钱
    :return:
    """
    #  如果在函数中修改全局变量,那么就需要使用global进行声明,否则出错
    global allMoney
    #   全局变量能够在所有的函数中进行访问， 但是不能直接修改;
    print("存钱前：", allMoney)
    allMoney += money
    print("存钱后：", allMoney)

def view_money():
    """
    查询金额
    :return:
    """
    # NameError: name 'allMoney' is not defined
    # 就近原则;
    allMoney = 20
    print("当前金额为:", allMoney)


view_money()
save_money(200)
view_money()
