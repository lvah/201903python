def singleton(cls):
    """
    用来装饰类的装饰器: 实例化类时， 只实例化一个对象；
    """
    # 初始化一个字典instances, key: 类名 ， value: 类实例化的对象
    instances = {}
    def wrapper(*args, **kwargs):
        """
        如果类在缓存instances存在时， 直接返回类对应的对象;
        如果类不在缓存instances存在时， 先实例化对象, 将类名和对象名存储到缓存中instances;
        """
        if cls in instances:
            return  instances[cls]
        else:
            # instances[cls] = cls(*args, **kwargs)
            obj = cls(*args, **kwargs)
            instances[cls] = obj
            return obj
    return  wrapper

@singleton   # @single  =====> Student = singleton(Student)
class Student(object):
    pass

# # 如果类没有被装饰器sigleton装饰的化， 返回的s1和s2时两个不同的对象（内存地址不同）;
# s1 = Student()
# s2 = Student()
# print(s1, s2)

# 如果类有被装饰器sigleton装饰， 返回的s1和s2时两个相同的对象（内存地址相同）;
s1 = Student()
s2 = Student()
print(s1, s2)
