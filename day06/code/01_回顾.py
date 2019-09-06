"""

# 函数部分
    匿名函数: lambda args1, args2=2, *args, **kwargs:返回值
            sum = lambda x,y: x+y

            应用场景: 排序sorted(iterable, key=lambda x:x[1], reverse=True)

    递归函数:
        1). 求阶乘: n! = n* (n-1)!    0!=1, 1!=1
            def f(n):
                if n in (0, 1):
                    return 1
                else:
                    return n*f(n-1)


        2). fib   f(n) = f(n-1) + f(n-2)    f(1)=1 f(2)=1
            def fib(n):
                if n<=2:
                    return 1
                else:
                    return f(n-1) + f(n-2)
        3). 汉诺塔
            def hanoi(n, a='A', b='B', c='C'):
                if n==1:
                    print(a, '--->', c)
                else:
                    hanoi(n-1, a, c, b)
                    hanoi(1, a, b, c)
                    hanoi(n-1, b, a, c)


# 文件部分
    - 文件的操作
        打开open()    -------mode=r,w,a, r+, w+, a+, rb, wb
        操作:(读/写)    read, readline, readlines      write writeines        seek(0, 2)-tell
        关闭close()-------with

            with open(filename, 'r') as f:   ====> f= open(filename, 'r')
                f.read()
    - os
        - 操作系统信息的获取
        - 对于文件和目录的操作
            os.mknod()
            os.mkdir()
        - 拷贝文件
        - 批量修改后缀名()

"""