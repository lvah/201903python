"""

文件操作:
    1. 普通字符串/二进制数据与文件的操作
    打开，读写, 关闭
    1). 打开:
        open(filename, mode='')
        mode=r, w, a, r+, w+, a+, rb, wb, ab, rb+, wb+, ab+

    2). 读写
        读: read, readline, readlines
        写: write, writeline
        定位: seek(偏移量, 固定参数) 固定参数: 0=开头 1=当前位置， 2=末尾

    3). 关闭
        f.close()
        with语句工作机制:====安全上下文

    2. 如果存储的是列表/字典/其他python对象， 如何保存到文件中?
    json, pickle
    序列化(dump,dumps)/反序列化(load, loads)


    3. python内置模块管理文件
    os
    1).
    2).

高级特性:
    1. 生成式
    列表/字典/集合生成式

    2. 生成器
    1). 如何创建生成器?
    - 列表生成式的[]改成()
    - yield关键字(如果函数中包含yield关键字， 那么调用该函数的返回值是一个生成器)
    e.g. Fib数列


    2). 如何访问生成器的内容?
    - for循环; (最常用)
    - next(), g.__next__()--用于测试


    3). return 和 yield工作机制有何不同?
    return: 函数中遇到return， 函数就执行结束;
    yield: 当调用next方法时， 函数运行， 遇到yield就停止运行; 当再次调用next方法时，会继续从上次停止的地方继续执行;


    4). 生成器其他的常用方法:
        next()
        send()













"""