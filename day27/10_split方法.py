import re
# 需求： 拿出运算操作中所有的数字
text = '1+3+5*10-8'
patternObj = re.compile(r'\+|-|\*|/')
# maxsplit=最大分割次数;
result = patternObj.split(text, maxsplit=3)
print(result)