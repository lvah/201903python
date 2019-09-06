"""

# 1.路由中的变量规则

    有时候需要接收URL中的参数变量，可以把参数标记为一个变量<变量名>，这个部分将会作为命名参数传递给函数。
    同时还可以限制参数变量的类型<类型:变量名>。
# 2. 数据类型一共有三种：int, float, path
    类型	        描述
    int	        接受整数
    float	    同 int ，但是接受浮点数
    path	    和默认的相似，但也接受斜线

# 3. 范例1:
    http://www.csdn.org/12000
    http://www.csdn.org/12001
    http://www.csdn.org/12002
    http://www.csdn.org/12003


# 4.范例2-动态路由：
    http://www.csdn.org/<userid>

"""

from flask import  Flask, request


app = Flask(__name__)


@app.route('/<int:userid>/')
def userinfo(userid):
    return  "正在查看用户%s的详细博客........" %(userid)


@app.route('/welcome/<string:username>')
def welcome(username):
    return  "欢迎访问%s用户的主页" %(username)



"""
https://movie.douban.com/top250?start=25&filter=
"""
@app.route('/top250')
def top250():
    users = ['user%s' %(i) for i in range(100)]
    # request存储用户请求页面的所有头部信息
    print("客户端的用户代理: ", request.user_agent)  # Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
    print("请求页面的头部信息: ", request.headers)
    print("客户端的IP：",  request.remote_addr)  # 127.0.0.1
    print("客户端请求的参数详细信息: ", request.args)  # ImmutableMultiDict([('start', '25'), ('user', 'westos')])

    print("客户端HTTP请求方法: ", request.method) # GET
    # 获取用户请求的url地址里面可以对应的value值;
    start = int(request.args.get('start'))   # '25'
    user = request.args.get('user')     # 'westos'
    # return  'top 250  显示数据开始：%s条   用户名: %s' %(start, user)
    import json
    return  json.dumps(users[start:start+10])


if __name__ == '__main__':
    app.run()