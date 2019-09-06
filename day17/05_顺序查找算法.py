def sequence_search(array, key):
    """
    顺序查找算法
    """
    for i in range(len(array)):
        if array[i] == key:
            return i
    return False


array_0 = [23, 43, 12, 54, 65, 48]
print(sequence_search(array_0, 12))
