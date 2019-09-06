"""
match 方法用于查找字符串的头部（也可以指定起始位置），它是一次匹配，只要找到了一个匹配的结果就返回， 而不是查找所有匹配的结果。它的一般使用形式如下：
"""

import re
patternObj = re.compile(r'(?P<URL>(?P<schme>http|https)://\w+\.\w+\.\w+)')
text = 'helo http://www.baidu.com   https://www.westos.org'
print("findall: ", patternObj.findall(text))
print("finditer: ", patternObj.finditer(text))
print("match: ", patternObj.match(text))
print("search: ", patternObj.search(text))
matchObj = patternObj.search(text)
if matchObj:
    print("匹配成功")
    print(matchObj.group())     # 返回匹配到的第一个分组
    print(matchObj.groups())    # 返回所有的分组
    print(matchObj.groupdict())  # 命名分组的时候， 会返回内容, {命名分组的名称: 匹配到内容}
    print(matchObj.start())
    print(matchObj.end())
    print(matchObj.span())
else:
    print("没有匹配成功")