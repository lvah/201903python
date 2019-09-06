"""

标识符(变量)合法性检查
"""
import string
# H2jhhh
variable = input("输入标识符:")
# 1). 只检查长度大于等于 2 的标识符
if len(variable) >= 2:
    # 通过， 如果某一段代码不知道怎么写， 但将来要写。pass占位
    # pass
    # 2). 以字母或者下划线开始;
    if variable[0] not in string.ascii_letters + '_':
        print("Error: 错误的标识符(以字母或者下划线开始)")
    else:
        # 获取除了第一个元素之外的其他元素; variable[1:]
        for item in variable[1:]:
            if item not in string.ascii_letters + string.digits + '_':
                print("Error： 错误的标识符(后面要跟字母,下划线或者或数字)")
                break
        # 遍历除了第一个元素之外的所有元素， 都符合条件， 执行下面的内容;
        else:
            print("%s是正确的标识符" %(variable))
else:
    print("Error: 错误的标识符")
