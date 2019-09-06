# 拿出100以内的所有偶数; range(0, 101, 2)

# 方法一:
# def is_odd(num):
#     """
#     判断是否为偶数， 返回值为Bool类型
#     :param num:
#     :return:
#     """
#     return  num %2 ==0
#
# odd_nums = filter(is_odd, range(0,101))
# for num in odd_nums:
#     print(num)

# 方法2：
# odd_nums = filter(lambda  num: num%2==0, range(0, 101))
# print(list(odd_nums))


"""
1. 获取100以内能被3或者5整除的所有数;
2. 获取2000-2999年，所有的闰年;
3. 获取1000内容所有的素数;
"""
# 1.
result1 = filter(lambda num: num % 3 == 0 or num % 5 == 0, range(100))
print(list(result1))

# 2.
is_leap = lambda year: (year % 4 == 0 and year % 100 !=0) or year % 400 == 0
result2 = filter(is_leap, range(2000, 3000))
print(list(result2))

# 3.
def is_prime(num):
    """判断是否为素数"""
    if num < 2:
        return  False
    for i in range(2, num):
        if num %i == 0:
            return  False
    else:
        return  True

result3 = filter(is_prime, range(1001))
print(list(result3))


