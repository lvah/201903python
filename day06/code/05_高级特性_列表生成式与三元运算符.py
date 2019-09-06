"""
 找出1～100之间所有奇数， 并且返回一个列表。如果能被3整除， 返回返回该数的平方,
 否则返回该数的三次方 。
"""
# 如果列表生成式和三元运算符结合在一起， if语句放前面;
nums = [num ** 2 if num % 3 == 0 else num ** 3 for num in range(1, 101, 2)]
print(nums)


# for循环里面嵌套for循环
print([i+j for i in range(1, 5) for j in range(4, 6)])