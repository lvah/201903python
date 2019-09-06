def BubbleSort(nums):
    """
    冒泡排序
    需要排n趟， i趟需要比较(n-i-1)
    :param nums: 需要排序的数值
    :return:
    """
    nums_len = len(nums)
    for count in range(nums_len):
        for index in range(nums_len-count-1):
            if nums[index]  < nums[index+1]:
                nums[index], nums[index+1] = nums[index+1], nums[index]

    return  nums

if __name__ == '__main__':
    nums = [12, 34, 23, 45, 66, 1, 2, 0]
    sorted_nums = BubbleSort(nums)
    print(sorted_nums)