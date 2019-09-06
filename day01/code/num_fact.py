#coding:utf-8
"""
求10的阶乘；
3！ = 1*2*3
4！= 1*2*3*4

"""
inputNum = int(input("请输入求阶乘的数:"))
if inputNum == 0:
	print(1)
elif inputNum < 0:
	print("请输入正确的数字(num>=0)")
else:
	# 初始值必须为1，如果为0， 则结果肯定错误为0；
	factResult = 1 
	# 获取10阶乘需要的所有数;
	nums = range(1,inputNum+1)
	# 依次 遍历所有的数, num=1, num=2, num=1.....num=10
	for num in nums:
		factResult *= num
	
	print(factResult)
