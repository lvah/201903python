import  re

html = '<html><p>hello python</span></html>'
# r:原生字符串, \代表转义， \\如果没有r时必须用\\代表\字符串;
"""
((?P<FirstTag>.*): 给第一个分组命名为FirstTag， 格式:  (?P<tagName>TagRe)
(?P<SecondTag>.*):  给第2个分组命名为SecondTag
(?P=SecondTag): 判断和第二个分组的内容是否一致； 如果不一致， 匹配失败;
(?PFirstTag): 判断和第1个分组的内容是否一致； 如果不一致， 匹配失败;
"""
pattern = r'<((?P<FirstTag>.*)><(?P<SecondTag>.*)>(.*)</(?P=SecondTag)></(?P=FirstTag)>)'
patternObj = re.compile(pattern)
result = patternObj.findall(html)
print(result)