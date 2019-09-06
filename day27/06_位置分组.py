import  re

html = '<html><p>hello python</p></html>'
# r:原生字符串, \代表转义， \\如果没有r时必须用\\代表\字符串;
"""
<(.*)>: 第一个分组
<(.*)>: 第2个分组
(.*)： 第3个分组
</\2>: \2的位置必须和第二个分组的内容保持一致， 否则不匹配;
</\1>: \1的位置必须和第1个分组的内容保持一致， 否则不匹配;
"""
pattern = r'<(.*)><(.*)>(.*)</\2></\1>'
patternObj = re.compile(pattern)
result = patternObj.findall(html)
print(result)