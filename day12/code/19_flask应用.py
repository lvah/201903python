from flask import  Flask

# http://www.baidu.com
# http://www.baidu.com/login/
# http://www.baidu.com/register/

# 创建APP应用
app = Flask(__name__)


@app.route('/')
def index():
    with open('baidu.html') as f:
        content = f.read()
    return  content

@app.route('/login/')
def login():
    return  '<h1 style="color:red">login</h1>'

# 运行APP应用
app.run()

