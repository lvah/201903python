# 定义每个古董重量
antique = [4, 10, 7, 11, 3, 5, 14, 2]


def max_ans(antique):
    anti_sort = sorted(antique)  # 对重量排序
    ans, tmp = 0, 0  # ans记录装载古董数量，tmp记录装载古董重量
    ship = []  # 记录装载的古董
    for a in anti_sort:
        tmp += a
        if tmp <= 30:
            ans += 1
            ship.append(a)
    print('装载古董数量:', ans)
    print('装载的古董', ship)


max_ans(antique)
