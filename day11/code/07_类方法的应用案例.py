class Date(object):
    # 魔术方法(构造方法)
    def __init__(self, year=2019, month=6, day=16):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def echo(self):
        print("%s-%s-%s" % (self.year, self.month, self.day))

    # 类方法: 默认传递的第一个参数是类名
    @classmethod
    def as_string(cls, str):
        """
        # # 将字符串的时间处理， 并执行echo方法
        # str  = '10/1/2019'
        # month, day, year = str.split('/')
        # d1 = Date(year, month, day)
        # d1.echo()
        :param str:
        :return:
        """
        # print(cls) # <class '__main__.Date'>
        # 将字符串的时间处理， 并执行echo方法
        # str  = '10/1/2019'
        month, day, year = str.split('/')
        d1 = cls(year, month, day)
        return d1

    @staticmethod
    def is_vaild(str):
        # str = '10/1/2019'
        month, day, year = map(int, str.split('/'))
        return  year > 0 and 0 < month <= 12 and 0 < day <= 31


d = Date()
# 运行类的实例方法
d.echo()

# str  = '10/1/2019'
# d1 = Date.as_string(str)
# d1.echo()
print(Date.is_vaild('13/13/2019'))

