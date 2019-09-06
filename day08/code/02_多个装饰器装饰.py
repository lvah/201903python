# 1). 判断用户是否登录？
# 2). 判断用户是否有权限?




def is_login(fun):
    def wrapper1(*args, **kwargs):
        print("判断是否登录......")
        result = fun(*args, **kwargs)
        return  result
    return  wrapper1

def is_permission(fun):
    def wrapper2(*args, **kwargs):
        print("判断是否有权限......")
        result = fun(*args, **kwargs)
        return  result
    return  wrapper2



# 1). 上面装饰器先执行， 下面的装饰器后执行;
# 2). 函数先被哪个装饰器装饰呢? 函数先被下面的装饰器装饰;    # delete = is_permission(delete)
"""
1). delete = is_perssion(delete)    # delete实际上是wrapper2
2). delete = is_login(delete)       # delete = is_login(wrapper2)    # delete实际上是wrapper1
3). delete()    --->    wrapper1()    --->  wrapper2()  ---> delete()
"""

@is_login   # delete = is_login(delete)
@is_permission
def delete():
    return  "正在删除学生信息"
result = delete()
print(result)