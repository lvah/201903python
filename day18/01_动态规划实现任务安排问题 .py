# 数组arr存储的是每个任务的收益；
arr = [0, 5, 1, 8, 4, 6, 3, 2, 4]
#数组prev存储的是指定任务之前可以执行的任务
prev = [0, 0, 0, 0, 1, 0, 2, 3, 5]

def dp_opt(arr):
    #计算任务的长度
    len_arr = len(arr)
    # 存储执行到每个任务可以获得的最优解;
    opt = [0 for i in range(len_arr)]
    opt[0] = 0
    opt[1] = arr[1]
    for i in range(2, len(arr)):
        # 不选择做这个任务的最优解；
        A = opt[i - 1]
        # 选择做这个任务的最优解；
        B = arr[i] + opt[prev[i]]
        opt[i] = max(A, B)
    return opt[-1]
print(dp_opt(arr))
