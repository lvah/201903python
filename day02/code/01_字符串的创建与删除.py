str1 = 'our company is westos'
str2 = "our company is westos"
str3 = """our company is westos"""
str4 = """this's  best languages "python"""""
# 三引号的作用:
#   1). 块注释
#   2). 创建字符串
str5 = """
                学生管理系统

        1). 增加学生
        2). 删除学生信息

        请选择:

"""
# ctrl+D    复制一行内容
# ctrl+Y    删除一行
# ctrl+/    注释(选中要注释的代码)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

# 删除字符串对象;
del str1
print(str1)



