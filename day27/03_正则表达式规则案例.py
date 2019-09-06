import re

# #1.  . : 代表除了\n之外的任意单个字符;
# # 编译正则表达式
# patternObj = re.compile(r'a.c')
# # 需要过滤的字符串;
# text = 'abc'
# # 返回符合正则规则的内容;(匹配与过滤)
# print(patternObj.findall(text))




# 2. 如果匹配的规则里面包含正则规则的特殊字符， 那么一定要通过\进行转义；
# 需求： 匹配www.westos.org
# 编译正则表达式
patternObj = re.compile(r'www\.westos\.org')
# 需要过滤的字符串;
text = 'www.westos.org www.baidu.com'
# 返回符合正则规则的内容;(匹配与过滤)
print(patternObj.findall(text))

# 3.字符集: []
#       所有数字: [0-9]
#       所有小写字母: [a-z]
#       所有大写字母: [A-Z]
#       所有字母: [a-zA-Z]
#       字母，数字或者下划线: [a-zA-Z0-9_]
# 需求: 匹配 wwww.westos.org  www.westoa.org
# 编译正则表达式
# patternObj = re.compile(r'www\.westo[sa]\.org')
patternObj = re.compile(r'www\.westo[^sa]\.org')  # 除了s或者a之外的任意字符串;
# 需要过滤的字符串;
text = 'www.westos.org www.baidu.com www.westob.org'
# 返回符合正则规则的内容;(匹配与过滤)
print(patternObj.findall(text))