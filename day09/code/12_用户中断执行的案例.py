# 用户可以一直输入数字, 当按ctrl+c之后计算所有数的和;
result = 0
while True:
    try:
        num = int(input('Num:'))
        # result = result +  num
        result += num
    #  用户中断运行的异常; ===捕获异常
    except KeyboardInterrupt:
        print("运行结果:", result)
        break
