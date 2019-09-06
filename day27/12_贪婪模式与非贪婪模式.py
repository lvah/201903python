import re
text = 'abbbbbb'
pattern1 = re.compile(r'ab*')  # 贪婪模式
pattern2 = re.compile(r'ab*?')  # 非贪婪模式

result1 = pattern1.findall(text)
result2 = pattern2.findall(text)

print(result1)
print(result2)