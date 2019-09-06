from flask import  Flask, request, render_template, flash
from forms import  LoginForm, RegisterForm
from flask_bootstrap import  Bootstrap

app = Flask(__name__)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    # 1. 实例化表单对象
    form = LoginForm()
    # 1). 是否为post提交表单信息;
    # 2). 是否通过验证函数?
    if form.validate_on_submit():
        # 获取表单的内容
        email = form.email.data
        password = form.password.data
        if email =='westos@qq.com' and password=='westos':
            return  '登录成功'
        else:
            return  "登录失败"
    else:
        return  render_template('bs_login.html', form=form)



@app.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return  '获取性别%s' %(form.gender.data)
    else:
        return  render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(port=5005)


