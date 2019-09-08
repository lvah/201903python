"""
用于启动程序以及其他的程序任务。
"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import create_app, db

# 动态创建app对象
app = create_app('default')
# 脚本管理
manager = Manager(app)
# migrate = Migrate(app, db)


# def make_shell_context():
#     return dict(app=app, db=db)


# 初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
