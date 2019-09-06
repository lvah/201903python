# *nums用来接收多个变量/参数， 接收近来的nums是一个元组;
def numSquare(*nums):
    """
    求n个数的平方
    :param nums:
    :return:
    """
    # print(nums)
    result = 0
    for num in nums:
        result += pow(num, 2)
    print(result)
numSquare()
numSquare(1)
numSquare(1, 2, 3)
numSquare(3, 4, 5, 6, 7)

# # *score可以存多个数值;
# low, *score, high = [1, 2, 3, 4, 5, 6100]
