# 第一种方法: 列表生成式的改写。 []改成()
# nums = [i**2 for i in range(100)]
# print(nums)


nums = (i**2 for i in range(5))
# print(nums)  # <generator object <genexpr> at 0x7f40e1b642a0>
# print(type(nums)) # <class 'generator'>

# for num in nums:
#     print(num)

# __next__和next()效果相同(面向对象-魔术方法)
# nums.__next__()
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

