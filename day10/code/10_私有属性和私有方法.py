
class Student(object):
    __country = 'china'
    def __init__(self, name, age, score):
        self.name = name
        # 年龄和分数是私有属性
        self.__age = age
        self.__score = score

    # 私有方法， 只能在类内部执行;
    def __modify_score(self, scores):
        self.__score = scores
        print(self.__score)


    def set_age(self, age):
        if 0<age <150:
            self.__age = age
            print("当前年龄:", self.__age)
        else:
            raise  Exception("年龄错误")


    def set_score(self, scores):
        if len(scores) == 3:
            self.__score = scores
        else:
            raise Exception("成绩异常")
class MathStudent(Student):
    pass

student = Student("粉条", 10, [100, 100, 100])
# 在类的外部是不能直接访问的;
print(student.name)

student.set_age(15)
# 为什么私有属性不能访问? python解释器看到以双下划开头的属性和方法， 对其修改名称; 是因为 Python 解释器对外把  __属性名 改成了  _类名__属性名
# print(student._Student__age)

# student1 = MathStudent("粉条", 10, [100, 100, 100])
