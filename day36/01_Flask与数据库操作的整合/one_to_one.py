# 数据库模型
# 数据库连接， db.Model
from run import db


class People(db.Model):
    __tablename__ = 'peoples'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, default=18)
    # 公民表和身份证表关联起来了, uselist=False一个对象不对应一个列表， 所以是一对一关系.
    # backref="people"给Card类里面添加属性信息名称为people， 可以根据身份证获取公民信息;
    card = db.relationship('Card', backref="people", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<People: %s>' % (self.name)


class Card(db.Model):  # 身份证
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cardID = db.Column(db.String(30), nullable=False)
    is_vaild = db.Column(db.Boolean, default=True)
    # 外键必须用类 sqlalchemy.schema.ForeignKey 来单独声明;# peoples指的是表名;
    # 限制身份证对应的公民必须是存在的公民;
    people_id = db.Column(db.Integer, db.ForeignKey('peoples.id'))

    def __repr__(self):
        return '<Card: %s>' % (self.name)


if __name__ == '__main__':
    db.create_all()
    # # 增:
    # p1 = People(name='张三')
    # p2 = People(name='李四')
    #
    # c1 = Card(cardID='001')
    # c2 = Card(cardID='002')
    #
    # c1.people = p1
    # c2.people = p2
    # # p1.card = c1
    # # p2.card = c2
    #
    # db.session.add_all([p1, p2, c1, c2])
    # db.session.commit()
    #

    # 删
    c1 = Card.query.get(1)
    db.session.delete(c1)
    db.session.commit()