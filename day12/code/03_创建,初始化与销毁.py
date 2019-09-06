class Student(object):
    def __new__(cls, name):
        print('正在new.....')
        # 不知道new方法试药干吗的, 直接返回父类的new方法
        return  super(Student, cls).__new__(cls)

    # 初始化(构造)方法: 创建对象时自动执行
    def __init__(self, name):
        print("正在初始化对象.....")
        self.name = name

    # 析构方法: 对象删除时自动调用
    def __del__(self):
        print("正在删除对象.....")


# 当程序运行结束之后, 会自动释放变量信息. 会自动调用析构方法;
s = Student('westos')
print(s.name)


