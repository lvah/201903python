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


def shellSort(arr):
    """
    5 4 3 2 1
    """
    step = int(len(arr) / 2)   # step
    while step > 0:
        print("step=", step)
        arr_len = len(arr)
        # index = 0 1 2 3 4
        for index in range(arr_len):
            # index=0  index+step=3
            # index=1   indx+step=4
            if index + step < arr_len:
                current_val = arr[index]
                if current_val > arr[index + step]:
                    arr[index], arr[index + step] = arr[index + step], arr[index]
                step = int(step / 2)
    else:
        # 直接插入排序
        return insert_sort(arr)


arr = [12, 34, 54, 2, 3, 4, 5, 2, 1, 44]

sorted_arr = shellSort(arr)
print(sorted_arr)
