"""

文件名: .py

创建时间: 2019-01-12 16:

作者: lvah

联系方式: 976131979@qq.com

代码描述:







银行转账:

    银行卡号:

    金额:









"""

import pymysql


class TransferMoney(object):

    # 构造方法

    def __init__(self, conn):

        self.conn = conn

        self.cur = conn.cursor()



    def transfer(self, source_id, target_id, money):

        # 1). 判断两个银行卡号是否存在?

        # 2). 判断source_id是否有足够的钱？

        # 3). source_id扣钱

        # 4). target_id加钱

        if not self.check_account_avaialbe(source_id):

            raise  Exception("账户不存在")

        if not self.check_account_avaialbe(target_id):

            raise  Exception("账户不存在")



        if self.has_enough_money(source_id, money):

            try:

                self.reduce_money(source_id, money)

                self.add_money(target_id, money)

            except Exception as e:

                print("转账失败:", e)

                self.conn.rollback()

            else:

                self.conn.commit()

                print("%s给%s转账%s金额成功" % (source_id, target_id, money))
        else:
            print("没有足够的金额")



    def check_account_avaialbe(self, acc_id):

        """判断帐号是否存在， 传递的参数是银行卡号的id"""

        select_sqli = "select * from bank where cardid=%s;" % (acc_id)

        print("execute sql:", select_sqli)

        res_count = self.cur.execute(select_sqli)

        if res_count == 1:

            return True

        else:

            # raise  Exception("账户%s不存在" %(acc_id))

            return False



    def has_enough_money(self, acc_id, money):

        """判断acc_id账户上金额> money"""

        # 查找acc_id存储金额?

        select_sqli = "select money from bank where cardid=%s;" % (acc_id)

        print("execute sql:", select_sqli)

        self.cur.execute(select_sqli)  # ((1, 500), )



        # 获取查询到的金额钱数;

        acc_money = self.cur.fetchone()[0]

        # 判断

        if acc_money >= money:

            return True

        else:

            return False



    def add_money(self, acc_id, money):

        update_sqli = "update bank set money=money+%d  where cardid=%s" % (money, acc_id)

        print("add money:", update_sqli)

        self.cur.execute(update_sqli)



    def reduce_money(self, acc_id, money):

        update_sqli = "update bank set money=money-%d  where cardid=%s" % (money, acc_id)

        print("reduce money:", update_sqli)

        self.cur.execute(update_sqli)



    # 析构方法

    def __del__(self):

        self.cur.close()

        self.conn.close()





if __name__ == '__main__':

    # 1. 连接数据库，

    conn = pymysql.connect(

        host='172.25.254.123',

        user='root',

        password='westos',

        db='pymysql',

        charset='utf8',

        autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。

    )

    trans = TransferMoney(conn)

    # print(trans.check_account_avaialbe('130001'))
    # print(trans.check_account_avaialbe('130004'))



    # print(trans.has_enough_money('130001', 800))
    # print(trans.has_enough_money('130001', 1200))



    # trans.add_money('130001', 200)
    # trans.reduce_money('130001', 200)

    # trans.transfer('130001', '130002', 100)
    # trans.transfer('130001', '130002', 1000)
    trans.transfer('130001', '130003', 1000)

