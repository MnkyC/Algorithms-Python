# 二分查找，数据结构有序，具有随机访问的特性
# 时间复杂度O(log2(n))，空间复杂度O(1)


# 最基本的算法，具有局限性，如nums=[1,2,2,2,3],target=2,结果为2
def binarySearch(nums, target):
    size = len(nums)
    if size == 0:
        return -1

    left = 0
    right = size - 1

    while left <= right:
        '''
        写法1: 整型溢出，不过py会将其自动转为long
        mid = (left + right) // 2
        写法2: 防止溢出，但是会导致可能永远取不到右边界
        mid = left + ((right - left) // 2)
        写法3: (left + right) >> 1，java装逼写法mid = (left + right) >>>1
        '''
        mid = (left + right) >> 1
        midValue = nums[mid]

        if midValue == target:
            return mid
        elif midValue < target:
            # mid和mid左边都小于target，下一轮搜索范围[mid + 1, right]
            left = mid + 1
        else:
            # mid和mid右边都大于target，下一轮搜索范围[left, mid - 1]
            right = mid - 1

    return -1


# 改进，排除法，减治思想，分为2部分，mid划分到左右区间中
def binarySearch2(nums, target):
    size = len(nums)
    if size == 0:
        return -1

    left = 0
    right = size

    while left < right:
        mid = (left + right) >> 1

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left if nums[left] == target else -1
