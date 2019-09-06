"""
基于yield计算平均值
# 17行;
"""
def averager():
    # 所有数的和, 默认为0；
    total = 0.0
    # 数值的个数;
    count = 0
    # 平均值结果;
    average = None
    # 所有数值存储的容器(List);
    all_items = []
    while True:
        # 函数包含yield关键字
        new_item = yield average, all_items
        all_items.append(int(new_item))
        total += new_item
        count += 1
        average = total / count


def main():
    # AVERAGER是个生成器;
    AVERAGER = averager()
    # 第一次调用next方法， 遇到yield停止，
    next(AVERAGER)

    # 死循环， 依次求解平均值;
    while True:
        new_num = input("请输入求平均值的数: ")
        if new_num == 'q':
            print("程序执行结束.....")
            break
        # 1). 通过send方法将求平均值的数值传到yield所在位置,(14行);
        # 2). send方法的返回值是求平均值的列表和平均值结果;
        average, all_items = AVERAGER.send(int(new_num))
        print(all_items, "的平均值为:", average)

main()
