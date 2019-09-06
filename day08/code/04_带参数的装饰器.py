"""
装饰器的框架
"""


# 如果装饰器需要传递参数， 在原有的装饰器外面嵌套一个函数即可
def auth(type):
    def wrapper1(fun):
        def wrapper(*args, **kwargs):
            if type=='local':
                user = input("User:")
                passwd = input("Passwd:")
                if user == 'root' and passwd == 'westos':
                    result = fun(*args, **kwargs)
                    return result
                else:
                    print("用户名/密码错误")
            else:
                print("暂不支持远程用户登录")

        return wrapper

    return wrapper1


"""
# python中装饰器的语法糖结构: @funName  ===> 
# python中装饰器结构如果为@funName()  ====> 默认跟的不是函数名， 先执行改函数， 获取函数返回结果  ====》 @funNameNew
@函数名      add=函数名(add)
@函数名()     @新的函数名    
"""


@auth(type='remote')
def home():
    print("这是主页")


home()
