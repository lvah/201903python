from datetime import  date


d = date(2019, 10, 10)
print(d.year)
print(d.month)
print(d)


class Student(object):
    # 初始化(构造)方法: 创建对象时自动执行
    def __init__(self, name):
        print("正在初始化对象.....")
        self.name = name
    # 如果没有__str__, 自动返回__repr__的内容
    # 对象的字符串打印
    def __str__(self):
        return  "<Student: %s>" %(self.name)

    # 在交互式python环境中产生作用
    def __repr__(self):
        return  self.name

s = Student("westos")
print(s)


