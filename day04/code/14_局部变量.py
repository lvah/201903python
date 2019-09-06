def save_money(money):
    """
    存钱
    :return:
    """
    # 局部变量， 只在当前函数中生效;
    allMoney = 100
    print("存钱前：", allMoney)
    allMoney += money
    print("存钱后：", allMoney)

def view_money():
    """
    查询金额
    :return:
    """
    # 局部变量， 只在当前函数中生效;
    allMoney = 100
    # NameError: name 'allMoney' is not defined
    print("当前金额为:", allMoney)


view_money()
save_money(200)
view_money()
