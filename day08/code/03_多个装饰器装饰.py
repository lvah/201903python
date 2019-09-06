# 1). 判断用户是否登录？
# 2). 判断用户是否有权限?
# 系统中的用户信息;
db = {
    'root': {
        'name': 'root',
        'passwd': 'westos',
        'is_super': 0  # 0-不是 1-是
    },
    'admin': {
        'name': 'admin',
        'passwd': 'westos',
        'is_super': 1  # 0-不是 1-是
    }
}
# 存储当前登录用户的信息;
login_user_session = {}


def is_login(fun):
    """
    判断用户是否登录， 如果没有登录，先登录
    :param fun:
    :return:
    """
    def wrapper1(*args, **kwargs):
        if login_user_session:
            result = fun(*args, **kwargs)
            return result
        else:
            print("跳转登录".center(50, '*'))
            user = input("User: ")
            passwd = input('Password: ')
            if user in db:
                if db[user]['passwd'] == passwd:
                    login_user_session['username'] = user
                    print('登录成功')
                    # ***** 用户登录成功， 执行删除学生的操作;
                    result = fun(*args, **kwargs)
                    return result
                else:
                    print("密码错误")
            else:
                print("用户不存在")

    return wrapper1


def is_permission(fun):
    def wrapper2(*args, **kwargs):
        print("判断是否有权限......")
        current_user = login_user_session.get('username')
        permissson = db[current_user]['is_super']
        if permissson == 1:
            result = fun(*args, **kwargs)
            return result
        else:
            print("用户%s没有权限" % (current_user))

    return wrapper2


"""
**** 被装饰的过程: 
1). delete = is_permission(delete)   # delete = wrapper2
2). delete = is_login(delete)        # delete = is_login(wrapper2)       # delete = wrapper1
"""


@is_login  # delete = is_login(delete)
@is_permission
def delete():
    return "正在删除学生信息"
"""
*******被调用的过程: 
delete()    ------>  wrapper1()   ---> wrapper2()  ---> delete()
"""
result = delete()
print(result)
