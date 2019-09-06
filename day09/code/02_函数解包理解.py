def fun(*args):
    print(sum(args))


# 参数解包
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*li)
fun(*li)    # 等同于fun(1, 2, 3, 4, 5, 6)
