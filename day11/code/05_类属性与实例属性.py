"""

不同点整理：
                    类属性                           对象属性
1. 定义               直接定义在类里面country='xxx'       属性和对象绑定在一起: self.name='xxxx'
2. 占用内存不一样       只存一份， 跟对象的个数无关           有多少个对象， 存储多少份;
3. 调用的时候不一样     类名.属性名， 对象名.属性名            对象名.属性名

"""
import string
from collections import Counter


class People(object):
    # 类属性， 在内存中只存一份；
    country = 'china'
    __gender = 'male'
    def __init__(self, name, age, money):
        # self.name, self.age, self.money: 实例属性（有多少个对象， 就有多少份属性;）
        self.name = name
        self.age = age
        self.money = money


# 实例化三个对象， 有三份实例属性；
p1 = People("westos1", 10, 1000000000)
print(p1.name)
print(p1.age, id(p1.age))
print(p1.money, id(p1.money))
p2 = People("westos2", 10, 1000000000)
print(p2.money, id(p2.money))
p3 = People("westos3", 10, 1000000000)
print(p3.money, id(p3.money))



# 调用p1, p2, p3的属性country： 当对象没有country属性时， 调用类的属性country;
print(p1.country, p2.country, p3.country)
# 设置p2对象的属性country为‘us’, 并不会修改类的属性；
p2.country = 'us'
# 调用p1, p2, p3的属性country： 当对象没有country属性时， 调用类的属性country; 当对象有country‘属性时， 调用拥有的country'属性；
print(p1.country, p2.country, p3.country)

# 类属性名如果前面添加双下划线， 那么他是私有属性， 类的外部时不能访问的；
print(p1._People__gender)
print(People.country)

string