"""
# 1.Http请求中常见的请求方式: GET POST
    1). url可见性：
        get，参数url可见；
        post，url参数不可见
    2). 数据传输上：
        get，通过拼接url进行传递参数；
        post，通过body体传输参数
    3). 缓存性：
        get请求是可以缓存的
        post请求不可以缓存
    4). 后退页面的反应
        get请求页面后退时，不产生影响
        post请求页面后退时，会重新提交请求
    5). 传输数据的大小
        get一般传输数据大小不超过2k-4k（根据浏览器不同，限制不一样，但相差不大）
        post请求传输数据可以无限大。
    6). 安全性: 原则上post肯定要比get安全。

# 2. 模版渲染
    hello {{ name }}
    name = westos    hello westos

    Flask和Django一样都配备了Jinja2模版引擎，可以使用render_template()方法来渲染模版。

# 3. 重定向和错误（redirect,error）
    使用redirect()函数把用户重定向到其他地方。 '/bbs' ---> '/login'
    使用abort()函数，放弃请求并返回错误代码。  # HTTP状态码: 404, 200, 304, 500

"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return  "<h1>主页</h1>"

@app.route('/login/')
def login():
    """
    一般情况， 不会直接把html文件内容直接返回；
    而是将html文件保存到当前的templates目录中；
          1). 通过render_template方法调用;
          2). 默认情况下,Flask 在程序文件夹中的 templates 子文件夹中寻找模板。
    """
    return  render_template('login.html')


@app.route('/login2/')
def login2():
    # 获取用户输入的用户名
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    # 逻辑处理， 用来判断用户和密码是否正确;
    if username == 'root' and password == 'redhat':
        # 重定向到指定路由；
        # 如果登录成功， 进入主页.
        return  redirect('/')
        # return "登录成功"
    else:
        # return  "登录失败"
        # 如果登录失败， 重定向到登录界面重新登录;
        return  redirect('/login/')

if __name__ == '__main__':
    app.run()