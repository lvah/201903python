"""
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）
"""


def isPrime(num):
    """
    判断传入的数值是否为素数? 返回Bool类型
    :param num:
    :return:
    """
    if num < 2:
        return False
    else:
        for item in range(2, num):
            if num % item == 0:
                return False
        else:
            return True


if __name__ == '__main__':
    num = int(input())
    # 获取0-num之间所有的素数;
    prime_nums = [item for item in range(2, num + 1) if isPrime(item) ]
    # 统计素数对的变量， 默认为0；
    prime_pair_count = 0
    # 依次遍历所有的素数； item = [2, 3, 5, 7]
    for item in prime_nums:
        # 已知求素数对的和为10， 也就是10-item的数值在素数列表中表示符合条件;
        item2 = num - item   # [8, 7, 5, 3]
        if item2 in prime_nums and item <= item2:
            prime_pair_count += 1
            print((item, item2))
    print(prime_pair_count)
