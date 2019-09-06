import re

"""
http://www.baidu.com
https://www.baidu.com
ftp://www.baidu.com
"""
# | 或者
# ()分组, 如果有分组， 只返回分组里面匹配到的内容;
# 匹配http和https协议的URL地址;
# r:代表规则为原生字符串， 一般情况下\代表转义的意思， 如果匹配的规则里面包含\时， 要写成\\, 而有了r， 就不用\\了.
URLpattern = r'((http|https)://(\w+\.\w+\.\w+))'
# 匹配http和https协议的URL地址;
# URLpattern = 'https?://\w+\.\w+\.\w+'
patternObj = re.compile(URLpattern)
text = 'http://www.baidu.com https://www.baidu.com ftp://www.baidu.com'
result = patternObj.findall(text)
print(result)