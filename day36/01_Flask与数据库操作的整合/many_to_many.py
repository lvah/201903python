# 数据库模型
# 数据库连接， db.Model
from run import db

# 多对多关系
# 第三方表
tags = db.Table('tags',
                db.Column('student_id', db.Integer, db.ForeignKey('math_students.id')),
                db.Column('course_id', db.Integer, db.ForeignKey('courses.id')))


class MathStudent(db.Model):
    __tablename__ = 'math_students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    # secondary指定关系表对象
    courses = db.relationship('Course', secondary=tags)

    def __repr__(self):
        return "<MathStudent: %s >" % (self.name)


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    # secondary指定关系表对象
    students = db.relationship('MathStudent', secondary=tags)

    def __repr__(self):
        return "<Course: %s >" % (self.name)


if __name__ == '__main__':
    db.create_all()
    # # 创建
    # s1 = MathStudent(name="拉格朗日")
    # s2 = MathStudent(name="麦克劳林")
    # s3 = MathStudent(name="罗尔")
    # course1 = Course(name="高等数学")
    # course2 = Course(name="线性代数")
    #
    # # 高等数学: 拉格朗日, 麦克劳林, 罗尔
    # # 线性代数: 拉格朗日,  罗尔
    # s1.courses.append(course1)
    # s1.courses.append(course2)
    # s2.courses.append(course1)
    # s3.courses.append(course2)
    # course1.students.append(s3)
    #
    # db.session.add_all([s1, s2, s3, course1, course2])
    # db.session.commit()

    # 删
    courseObj = Course.query.filter_by(name="线性代数").first()
    studentObj = MathStudent.query.filter_by(name="罗尔").first()
    print("删除前选择线性代数的学生: ", courseObj.students)
    courseObj.students.remove(studentObj)
    print("删除后择线性代数的学生: ", courseObj.students)
