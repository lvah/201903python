# 数据库模型
# 数据库连接， db.Model
from run import db


# 一对多关系， 外键写在多的一端
# Grade: Student == 1:N
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    # 外键关联,限制学生所属班级的id必须是grdes表中有的班级id;
    grade_id = db.Column(db.Integer, db.ForeignKey('grades.id'))
    # Student(name='sss', grade_id=8)

    def __repr__(self):
        return  "<Student: %s>" %(self.name)


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    # 关系, backref=‘grade’给Student类中添加属性grade， uselist=True, 一对多关系, 一个对象对应一个列表;
    students = db.relationship('Student', backref="grade", uselist=True)


if __name__ == '__main__':
    db.create_all()

    # 增
    # s1 = Student(name='张单')
    # s2 = Student(name='里斯')
    # s3 = Student(name='粉条')
    # grade1 = Grade(name='Python开发')
    # grade2 = Grade(name='Java开发')
    #
    # grade1.students = [s1, s2, s3]
    # db.session.add_all([s1, s2, s3, grade1, grade2])
    # db.session.commit()




    # 删
    grade1 = Grade.query.get(1)
    s1 = Student.query.get(1)
    s1.grade_id = None
    db.session.add_all([grade1, s1])
    db.session.commit()


