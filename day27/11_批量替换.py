"""
sub 方法用于替换。它的使用形式如下：

"""
import  re
text = "本文章点赞数为100， 转发数为20"
patternObj = re.compile(r'\d+')
# 将text文本信息中符合patternObj规则的内容替换为0;
result = patternObj.sub('0' , text)
print(result)

# 需求： 匹配到的所有数值+1

def addNum(matchObj):
    """对匹配到的内容+1"""
    if matchObj:
        # 目前num时一个字符串
        num = matchObj.group()
        # 在原有基础上加1 , num时数值类型
        num = int(num) + 1
        return str(num)


def add_perfix(matchObj):
    if matchObj:
        return '1002' + matchObj.group()

result = patternObj.sub(addNum, text)
print(result)

result = patternObj.sub(add_perfix, text)
print(result)