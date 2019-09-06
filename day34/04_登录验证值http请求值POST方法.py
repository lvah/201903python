"""

# 1.自定义错误页面:
    1). 为什么要自定义错误页面?
    如果你在浏览器的地址栏中输入了不可用的路由,那么会显示一个状态码为 404 的错误页
    面。现在这个错误页面太简陋、平庸.
    2). 如何自定义错误页面?
    像常规路由一样,Flask 允许程序使用基于模板的自定义错误页面。
    最常见的错误代码有两个:
            - 404,客户端请求未知页面或路由时显示;
            - 500,有未处理的异常时显示。

"""

from flask import Flask, request, render_template, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "这是主页"


# 默认路由只支持get方法， 如何指定接受post方法?
@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    1. 用户访问网址: http://xxxx/login, 返回登录的html页面;
        方法method: GET
    2. 用户在表单中填写信息，
        <form action="/login/" method="POST">
    3. 执行post提交的逻辑;

    :return:
    """
    if request.method == 'POST':
        # 难点: post请求提交的数据如何获取?  request.form
        # 难点: get请求提交的数据如何获取?   request.args
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        # 如果用户名和密码正确， 跳转到主页;
        if username == 'root' and password == 'redhat':

            return redirect('/')
        # 如果登录不正确， 则警告红色信息;还是在登录页面;
        else:
            # 可以给html传递变量
            return render_template('login_post.html',
                                   errMessages="用户名或者密码错误"
                                   )
    else:
        # abort(500)
        return render_template('login_post.html')


@app.route('/welcome/<string:username>')
def welcome(username):
    app.logger.error("欢迎界面......")
    return render_template('welcome.html', name=username)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()
