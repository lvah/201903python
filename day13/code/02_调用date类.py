import time
from datetime import  date


# 1. 根据时间戳返回当前的日期date对象;
d = date.fromtimestamp(time.time())
print(d)


# 2. date类本身不支持修改年月日
# d.month = 7
# print(d)


# 3. 如果间接修改: 重新实例化一个对象返回
d1 = d.replace(year=1999)
print(d)  # 2019-06-23
print(d1)  # 1999-06-23

# 4. 魔术方法： __add__代表两个对象是可以连接/相加的, 返回两周之后的时间;
from datetime import  timedelta  # 时间间隔对象
delta = timedelta(weeks=2)
print(d + delta)

