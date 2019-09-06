def factorial(num):
    """
    0! = 1
    1! = 1
    2! = 2 * 1 = 2 * 1!
    3! = 3*2*1  = 3*2!
    4! = 4*3*2*1 = 4*3!
    ....
    n! = n * n-1 *n-2 .....1 = n * (n-1)!

    求num的阶乘
    """
    result = 1
    for item in range(1, num + 1):
        result = result * item
    return result


def recursive_factorial(num):
    """
    使用递归求num的阶乘
    """
    # 如果num等于0或者1， 返回1；
    if num in (0, 1):
        return 1
    # num的阶乘为num*（num-1）!
    else:
        return num * recursive_factorial(num - 1)

print("3的阶乘: ", factorial(3))
print("6的阶乘: ", factorial(6))
print("3的阶乘: ", recursive_factorial(3))
print("6的阶乘: ", recursive_factorial(6))
print("998的阶乘: ", recursive_factorial(998))