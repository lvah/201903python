# type(class_name, base_class, class_attr)

# 自定义的元类
def upper_attr(cls_name, bases, attr):
    """

    :param cls_name: 类名称
    :param bases: 父类名称(元组)
    :param attr: 属性(字典)
    :return:
    """
    newAttr = {}
    for key, value in attr.items():
        newAttr[key.upper()] = value
    print(newAttr)
    return  type(cls_name, bases, newAttr)
# python3的写法
class Student(object, metaclass=upper_attr):
    # 自定义指定元类名称
    # python2:
    # __metaclass__ = upper_attr
    country = 'china'
    score = 100
s = Student()
# print(s.country)
print(s.COUNTRY)
