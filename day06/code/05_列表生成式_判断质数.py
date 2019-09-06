def isPrime(num):
    """
    判断num是否为质数?
    质数: 只能被1和它本身整除的数就是质数. (负数不是质数， 1不是质数)
    :param num:
    :return:Bool(True, False)

    num=5: 5%2==0  5%3==0 5%4==0     (2, 5)   (2, num)
    num=6: 6%2==0(---不需要继续判断了) ----> 不是质数
    """
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return  False
        else:
            return  True


#  找出1～100之间所有的质数。
primeNums = [num for num in range(1, 101) if isPrime(num)]
print(primeNums)
