"""

验证回文串
"""
import string
str  = input("请输入验证的字符串:")
if len(str) == 0:
    print(True)
else:
    # 将字符串转成小写字母， 忽略大小写;
    str = str.lower()

    # 创建一个变量cleanStr, 保存清洗过后的字符串;
    cleanStr = ''
    # 依次遍历所有的字符串元素
    for item in str:
        # 判断是否为字母或者数字， 如果是，加入到cleanStr;
        if item in string.ascii_letters + string.digits:
            cleanStr += item

    print("清洗后的字符串:", cleanStr)
    # 判断是否为回文字符串， 正向和反向读取内容相同，即回文.
    print(cleanStr == cleanStr[::-1])

# s = 'hello'
# s1 = 'helleh'
# print(s == s[::-1])
# print(s1 == s1[::-1])