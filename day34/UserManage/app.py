from flask import Flask, request, render_template, redirect, session, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "westos"  # 加密盐

users = [
    {
        'username':'root',
        'password':'root'
    }
]
# 会话: session
# 缓存: cookie

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return  render_template('login.html')
    # request.method=='POST
    else:
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        for user in users:
            if user['username'] == username and user['password'] == password:
                # 存储用户登录信息; session可以认为时字典对象
                session['username'] = username
                # print(session)
                flash("登录成功")
                return redirect('/')
        else:
            flash("登录失败")
            return render_template('login.html', errMessages='login fail')

@app.route('/logout/')
def logout():
    # 将session中的用户信息删除;
    session.pop('username')
    flash("注销成功")
    return  redirect('/login/')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """
    1), http请求的方法为get方法， 直接返回注册页面;
    2). http请求的方法为post方法，
        - 注册的用户名是否已经存在， 如果存在， 重新注册；
        - 如果不存在， 存储用户名和密码到数据库中；
    """
    if request.method == 'GET':
        return  render_template('register.html')
    else:
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        for user in users:
            # 注册的用户名是否已经存在， 如果存在， 重新注册；
            if user['username'] == username:
                flash("注册失败: 用户名冲突")
                # session['username'] = username
                return redirect('/register/')
        # 如果不存在， 存储用户名和密码到数据库中；
        else:
            users.append(dict(username=username, password=password))
            flash("用户注册成功, 请登录")
            return  redirect('/login/')

@app.route('/list/<int:page>/') # 用户信息的分页查看
def list(page):
    return  render_template('list.html', users=users)





if __name__ == '__main__':
    app.run(port=5001)
