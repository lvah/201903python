# 入口脚本
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import  *
from one_to_many import  *

# Manager类将追踪所有的在命令行中调用的命令和处理过程的调用运行情况;
# configure your app
from models import User
from run import app, db

manager = Manager(app)
# 第一个参数是Flask的实例,第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app, db)

# manager是Flask-Script的实例,添加一个db命令
manager.add_command('db', MigrateCommand)


@manager.command
def create_superuser():
    """创建超级用户"""
    try:
        name = input("请输入超级用户名称: ")
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return "超级用户创建失败:", e
    else:
        return "创建超级用户成功"


@manager.option('-n', '--name', help='Your name')
def del_admin(name):
    """删除超级用户"""
    user = User.query.filter_by(name=name).first()
    if not user:
        return "删除的超级用户不存在"
    else:
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            return "超级用户删除失败:", e
        else:
            return "删除超级用户成功"


if __name__ == '__main__':
    manager.run()
