def halffind(nums, key, low, high):
    """
    二分查找递归实现
    """
    mid = (low + high) // 2
    if key == nums[mid]:
        return mid
    if low > high:
        return False

    if key > nums[mid]:
        return halffind(nums, key, mid + 1, high)
    else:
        return halffind(nums, key, low, mid - 1)


if __name__ == "__main__":
    nums = [-789, -96, -53, 23, 52, 56, 520]  # 测试案例
    key = int(input("请输入要搜索的关键字:"))
    print(halffind(nums, key, 0, len(nums)))
