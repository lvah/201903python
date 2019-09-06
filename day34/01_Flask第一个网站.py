from flask import  Flask
app = Flask(__name__)

# 实现首页: http://172.25.254.197:9999/
@app.route('/')  # 路由
def index():    # 视图函数， 一定不能重复;
    return  '这是网站的首页'


@app.route('/login/')
def login():
    return  "正在登录......"

@app.route('/logout/')
def logout():
    return  "正在登出......"

if __name__ == '__main__':
    # 运行Flask项目， 默认ip和端口是127.0.0.1：5000
    # 如何特色化指定? host='0.0.0.0'  开放本机的所有IP port=5000 端口必须是整形数
    # debug=True: 是否开启调试模式， 测试环境中开启， 生产环境一定要关闭.
    app.run(host='0.0.0.0', port=9999, debug=True)

