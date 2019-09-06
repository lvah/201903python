"""直接插入排序算法"""


def insert_sort(nums):
    """
      # 插入排序
    :param nums:
    :return:
    """
    count = len(nums)  # 待排序的序列
    # # 第一个索引认为是有序的数值序列， 依次遍历除了第一个元素之外的其他元素， 插入到前面有序的序列
    for i in range(1, count):
        # 要插入的数值元素
        key = nums[i]
        # 和有序表的最后一个元素开始比较(此时j=i-1)，
        #  直到比较到有序序列的第一个元素时结束(此时j=0)
        j = i - 1
        while j >= 0:
            # 比较大小
            if nums[j] > key:
                nums[j + 1] = nums[j]
                nums[j] = key
            j -= 1
    return nums


if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    sort_nums = insert_sort(nums)
    print(sort_nums)
