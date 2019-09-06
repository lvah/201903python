# 导入正则表达式对应的模块;
import re

# 定义正则表达式的规则;
pattern = r'westos'
# 对正则表达式进行一个编译， 编译后， 匹配速度更快;
patternObj = re.compile(pattern)
# 将来要处理的字符串内容;
text = "hello westos hello world westos"
# 匹配符合正则规则的所有内容;
result = patternObj.findall(text)
print(result)