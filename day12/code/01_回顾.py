"""
1. 类属性和实例属性
  类属性:   类名.属性名    对象名.属性名
  实例属性:  对象名.属性名
2. 类方法, 实例方法， 静态方法
     类方法 函数的第一个参数是类名        @classmethod
     实例方法: 函数的第一个参数是对象/实例
     静态方法： python解释器不会自动传入任何信息   @staticmethod

3. property属性
.setter      @age.deleter


4. 单例模式
    类只能实例化一个对象的模式
"""


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def eat(self):
        pass

    @classmethod
    def look(cls):
        pass

    @staticmethod
    def sleep():
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, item):
        if 0 < item < 150:
            self.__age = item





p = People('name', 10)
print(p.age)
p.age = 60
print(p.age)
