""""

"""
def fun():
    print('fun.......')

# 1). 类的定义
class People:
    # 构造方法： 当创建对象时会自动调用并执行;
    # self实质上是实例化出来的对象， e.g: xiaoming， xiaohong;
    def __init__(self, name, age, gender):
        # print("正在创建对象")
        # print(self)
        # 将创建对象的属性(name, age, gender)封装到self(就是实例化的对象)变量里面;
        # 在类里面定义的变量: 属性
        self.name = name
        self.age = age
        self.gender = gender
    # 在类里面定义的函数： 方法
    def eat(self):
        print('%s eating......' %(self.name))

    def sleep(self):
        # 获取对象self封装的属性(name, age, gender)
        print('%s sleep.......' %(self.name))

# 2). 实例化: 通过类实现对象的创建
xiaoming = People("小明", 20, '男')
# 将对象self/xiaoming封装的属性(name, age, gender)从里面拿出来;
print(xiaoming.name)
xiaoming.eat()
xiaoming.sleep()

xiaohong = People("小红", 20, '女')
print(xiaohong.name)
xiaohong.eat()
xiaohong.sleep()


# # 3). 打印类和打印对象
print(People)   # <class '__main__.People'>
print(xiaoming)  # <__main__.People object at 0x7f5f42be14a8>
print(xiaohong) # <__main__.People object at 0x7f5f34e6ce10>

