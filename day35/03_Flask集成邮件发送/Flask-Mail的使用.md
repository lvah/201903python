# 为什么需要使用Flask-Mail组件?

在我们开发完web系统后，一些特定的事件发生时,系统要自动发送相关邮件至管理员，运维人员和其他相关人员。
python标准库中的smtplib包也可以用在Flask程序中发送邮，但包装了smtplib的flask-mail扩展能更好地
和Flask集成。


# 如何使用flask-mail扩展发送邮件?



- 安装flask-mail扩展

```
 pip install flask-mail
```

- 查看安装情况

```
pip show flask-mail

```

# 发送邮件的时候需要设置什么?
- 发件人账户
- 密码
- 收件人
- 邮件标题
- 邮件正文
- QQ邮件服务器的域名或者IP;


# 详细代码

```python
from flask_mail import Mail, Message
from flask import Flask, render_template

app = Flask(__name__)

# 配置发送邮件的相关信息;
# 指定邮件服务器的域名或者IP https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=369
app.config['MAIL_SERVER'] = 'smtp.qq.com'

# 指定端口， 默认25， 但qq邮箱默认为 端口号465或587；
app.config['MAIL_PORT'] = 465
# app.config['DEBUG'] = True
"""
由于QQ邮箱不支持非加密的协议，那么使用加密协议, 分为两种加密协议，选择其中之一即可
"""
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '976131979'
# 此处的密码并非邮箱登录密码， 而是开启pop3
app.config['MAIL_PASSWORD'] = "sdjuoeyoxjoubedb"

# 初始化mail对象, 一定要先配置邮件信息;
mail = Mail(app)

def send_mail(to, subject, info):
    msg = Message(subject=subject,
                  sender='976131979@qq.com',
                  recipients=to,
                  )
    msg.body = info
    msg.html = '<h1>邮件正文html内容</h1>'
    with app.app_context():
        mail.send(msg)
send_mail(to=['976131979@qq.com', '2834746621@qq.com'], subject="第2次测试",
          info="邮件测试正文")

```