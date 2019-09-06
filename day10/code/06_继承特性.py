"""


        问题一: 如何让实现继承?
		子类在继承的时候,在定义类时,小括号()中为父类的名字

	     问题二: 继承的工作机制是什么?
	    	父类的属性、方法,会被继承给子类。 举例如下:  如果子类没有定义__init__方法,父类有,那么在子类继承父类的时候这个方法就被继承了,所以只要创建对象,就默认执行了那个继承过来的__init__方法。
"""
# 定义类的过程
# Father: 父类/基类
class People:
    goal = "先挣它1个亿"
    # 如果类里面的方法以双下划线开头/结尾, 魔术方法;
    def __init__(self, name, age, money):
        # 封装
        self.name = name
        self.age = age
        self.money = money
    def eat(self):
        print("%s正在吃大餐" %(self.name))
# Son: 子类/扩展类
# 代表Son类的父类为Father;
class Son(People):
    # Son没有构造方法, 因为父类Father有， 自动调用父类的构造方法;
    goal = "先挣它10个亿"


    def eat(self):
        # 调用父类的方法一:
        # Father.eat(self)
        # 调用父类的方法二(建议): 获取Son对应的父类，， 并执行该父类的eat方法
        super(Son, self).eat()
        print("%s正在吃xxxxxx" %(self.name))
# 实例化的过程: 通过类创建对象的过程
# wjl = Father("王健林", 68, 1000000000000)
wsc = Son("王思聪", 35, 10000000000)
# print(wjl.money)
# print(wsc.money)
wsc.eat()


# print(wjl.goal)
print(wsc.goal)

