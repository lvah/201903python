# ^:以什么开头,     [^abc]: 如果字符集中代表除了什么之外， 如果不再字符集， 在规则的开头代表以什么开头;
# $:以什么结尾


import  re
pattern = r'\A1[\n\d]+8\Z'
text  = '178789\n7898098'
patternObj = re.compile(pattern)
result = patternObj.findall(text)
print(result)