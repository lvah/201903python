# 案例1： 匹配所有的qq邮箱， username@qq.com, 其中username必须是字母数字或者下划线， 次数为2-12个之间；
import re

pattern1 = r'\s\w{2,12}@qq\.com'
text = ' westos@qq.com  hello@qq.com  dhwehfhjrefhjrehfuhregiuhgggggggggggggiu@qq.com'
patternObj = re.compile(pattern1)
result = patternObj.findall(text)
print(result)

# 案例2：
#     北美电话的常用格式:(eg: 2703877865)
#             前3位: 第一位是区号以2~9开头 , 第2位是0~8, 第三位数字可任意;
#             中间三位数字:第一位是交换机号, 以2~9开头, 后面两位任意
#             最后四位数字: 数字不做限制;
pattern2 = r'\(?[2-9][0-8]\d\)?[-\.\s]?[2-9]\d{2}[-\.\s]?\d{4}'
text = '(323)4567890'
patternObj = re.compile(pattern2)
result = patternObj.findall(text)
print(result)