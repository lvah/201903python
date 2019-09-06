#
# # 自定义异常====> NameError, IndexError实质上是一个类;(此处不理解也没关系, 后面还会在说)
# class AgeError(NameError):
#     pass

# 录入学生信息的系统;
# 对录入的信息进行校验: 1). len(姓名)>2  2). 0<age<150

name = input("姓名:")
if len(name) < 2:
    raise NameError("姓名必须大于2位")
age = int(input("年龄:"))
if age < 0 or age >= 150:
    raise NameError("年龄必须在0<age<150")

