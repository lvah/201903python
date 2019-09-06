class Student(object):
    country = 'china'

# 如何动态创建类? (基于元类创建的;)
MathStudent = type('MathStudent', (object, ), {'country': 'china'})
print(MathStudent)
print(MathStudent.__bases__)
print(MathStudent.__dict__)
print(MathStudent.country)