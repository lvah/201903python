#coding:utf-8
# python2:
    # 经典类: 	class Father:
    # 新式类:   class Father(object):
# python3:
#       所有的都是新式类

# 新式类：  广度优先
# 经典类:  深度优先



class D:
	a = 'd'

class B(D):
	pass

class C(D):
	a = 'c'

class A(B, C):
	pass
obj = A()
print(obj.a)


