"""
异常处理:
    1. what?
    2. how?  try....except.....else......finally......
    3. 抛出异常(raise Exception("报错内容"))
    4. 自定义异常类: BaseException是所有异常类的基类

        # Exception
        class AgeError(NameError):
            pass

        age = 188
        if not 0<age<150:
            raise  AgeError("年龄错误")
垃圾回收机制：
    1. 对象池： 小整形范围[-5, 257), 大整型池， 字符串池
    2. 引用计数， 标记-清除， 分代收集

面向对象的新名词:
    类:  class 类名： pass
    对象： 通过类实例化出来的叫做对象; 对象名=类名()
    实例化: 类--> 对象
    子类/父类:
    扩展类/基类:
    继承：

三大特性:
    封装:
        self: 实质上实例化出来的对象
        __init__()： 构造方法, 实例化对象时执行
        1). 如何实现封装? self.name = name
        2). 如何获取封装的内容? self.name, 对象名.name
    继承：
        1). 如何继承? class 子类(父类): pass
        2). 继承机制?  自动继承父类的属性和方法;
        3). super() 自动调用父类的方法

        私有属性和私有方法：双下划线

    多态:
        多种状态


"""
