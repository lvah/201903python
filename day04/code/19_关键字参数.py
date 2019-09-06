# **kwargs： 关键字参数, 接收的kwargs是一个字典;
def recordStudentInfo(name, sid, **kwargs):
    """
    录入学生信息， 必填的内容姓名和学号, 其他的可以自己输入
    :param name:
    :param sid:
    :return:
    """
    print("""
    
    姓名： %s
    学号: %s
    
    """%(name, sid))

    for key, value in kwargs.items():
        print("\t %s: \t%s" %(key, value))

recordStudentInfo("西部开源", '001', score=100, courses=['python', 'c', 'Linux'])