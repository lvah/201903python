# 数据库模型
# 数据库连接， db.Model
from run import db

"""
create table users (id int primary key, name varchar(20) unique );
"""


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer, default=18)
    email = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return  '<User: %s>' %(self.name)


if __name__ == '__main__':
    # 创建模型文件中定义的数据库表(一个类对应一个数据库表)
    db.create_all()

    # # 创建: 添加用户信息到users表中
    # user = User(name='westos')
    # # 1). 添加到会话中;
    # db.session.add(user)
    # # 2). 提交到数据库中
    # db.session.commit()

    # # 查询数据库操作, filter_by根据姓名筛选用户信息， first获取列表中的第一个元素
    # user = User.query.filter_by(name='westos').first()
    # print("查询用户的信息:", user.id, user.name)
    #
    # # 删除用户信息: 要删除谁?
    # db.session.delete(user)
    # db.session.commit()

    # # 修改用户信息: 类似于添加
    # user = User.query.filter_by(name='westos').first()
    # user.name = '粉条'
    # db.session.add(user)
    # db.session.commit()

    # db.drop_all()

    # # 批量添加用户信息, 测试过滤器
    # for index in range(10):
    #     user = User(name="name" + str(index + 1))
    #     db.session.add(user)
    # db.session.commit()

    # print(User.query.limit(5).all())
    # print(User.query.offset(5).limit(5).all())
    # # 如果降序排， -User.name
    # print(User.query.order_by(User.name).all())
    # # group_by
    # print(User.query.group_by(User.name).all())