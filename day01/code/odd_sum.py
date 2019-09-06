#coding:utf-8


# 0+2+4+6+...100
sumResult = 0
# 获取100以内所有的偶数;
odds = range(0, 101, 2)
# 依次 遍历所有的偶数, num=0, num=2, num=4.....num=100
for num in odds:
	sumResult += num

print(sumResult)
