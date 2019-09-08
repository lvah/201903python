# 路由和视图函数
from run import  app
@app.route('/')
def index():
    return  'index'