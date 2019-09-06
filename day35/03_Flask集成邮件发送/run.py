from flask_mail import Mail, Message
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
# 获取配置文件中的配置信息;
app.config.from_pyfile('config.py')
def send_mail(to, subject, filename, **kwargs):
    """

    :param to: 收件人
    :param subject: 邮件主题
    :param filename: 邮件正文对应的html名称
    :param kwargs: 关键字参数， 模版中需要的变量名
    :return:
    """
    # 初始化mail对象, 一定要先配置邮件信息;
    mail = Mail(app)
    msg = Message(subject=subject,
                  sender='976131979@qq.com',
                  recipients=to,
                  )
    # msg.body = info
    msg.html = render_template(filename + '.html',  **kwargs)
    with app.app_context():
        mail.send(msg)


# send_mail(to=['976131979@qq.com', '2834746621@qq.com'], subject="第2次测试",
#           info="邮件测试正文")


@app.route('/register/', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return  render_template('login.html')
    else:
        email = request.form.get('email')

        password = request.form.get('password')
        try:
            send_mail(to=[email], subject='注册通知邮件', filename='registerok', username=email)
        except Exception as e:
            flash("注册失败")
            return redirect('/register/')
        else:
            flash("注册成功")
            return redirect('/login/')

@app.route('/login/')
def login():
    return 'login'

if __name__ == '__main__':
    app.run(port=5004)