# 35 Search Insert Position
# 排序数组nums和目标值target，在nums中找到target返回索引，不存在就返回按顺序插入的位置
def searchInsert(nums, target):
    size = len(nums)
    if size == 0:
        return 0

    if nums[-1] < target:
        return size

    left = 0
    right = size

    while left < right:
        mid = (left + right) >> 1

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# 69 Sqrt(x)
# 计算并返回非负整数x的平方根，只保留整数部分
# 思路: 一个数的平方根最多不会超过它的一半
def sqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x >> 1

    while left < right:
        # 一定要取右中位数，左中位数可能会死循环
        #mid = left + ((right - left + 1) >> 1)
        mid = (left + right + 1) >> 1
        square = mid * mid

        if square > x:
            right = mid - 1
        else:
            left = mid

    return left


# Two Sum II
# 生序数组nums，找到和为target的两个下标，index1<index2
# 思路: 固定起点
def twoSum(nums, target):
    size = len(nums)
    if size == 0:
        return -1, -1

    # 指针碰撞, O(n), O(1)
    # left = 0
    # right = size -1

    # while left < right:
    #     value = nums[left] + nums[right]

    #     if value == target:
    #         return left+1, right+1
    #     elif value < target:
    #         left += 1
    #     else:
    #         right -= 1

    # 二分, O(nlog(n)), O(1)
    indexSize = size - 1

    for left in range(indexSize):
        right = binarySearch(nums, left + 1, indexSize, target - nums[left])
        if right != -1:
            return left+1, right+1

    return -1, -1

def binarySearch(nums, left, right, target):
    while left < right:
        mid = (left + right) >> 1

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left if nums[left] == target else -1


# 278 First Bad Version
# 版本基于之前版本开发，一旦出错后面的版本都是错误的，找到第一个错误的版本
def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) >> 1

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


# 349 Intersection of Two Arrays
# 求两个数组的交集
def intersection(nums1, nums2):
    #return list(set(nums1) & set(nums2))

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    res = set()

    for item in nums1:
        if exist(nums2, item):
            res.add(item)

    return list(res)

def exist(nums, item):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) >> 1

        if nums[mid] < item:
            left = mid + 1
        else:
            right = mid

    return True if nums[left] == item else False


# 350 Intersection of Two Arrays II
def intersect(nums1, nums2):
    pass


# 367 Valid Perfect Square
# 正整数num是否是一个完全平方数
# 完全平方数，即m*m=num，左边界=2，根据一个数的平方根最多不会超过它的一半，右边界=num/2
def perfectSquare(num):
    if num < 2:
        return True

    # 解1: 数学定理, (1 + 3 + 5 + ... + (2n - 1)) = n ^ 2, O(sqrt(n))
    # i = 1
    # while num > 0:
    #     num -= i
    #     i += 2

    # return num == 0

    # 解2: 牛顿迭代法, O(log(n)), O(1)
    # i = num >> 1

    # while i * i > num:
    #     i = (i + num // i) >> 1

    # return i * i == num

    # 解3: 二分
    left = 2
    right = num >> 1

    while left < right:
        mid = (left + right) >> 1
        square = mid * mid

        if square < num:
            left = mid + 1
        else:
            right = mid

    return left * left == num


# 374 Guess Number Higher or Lower
# 猜数字，guess函数，猜的数更大返回1，更小返回-1，相等返回0
def guessNumber(n):
    left = 0
    right = n

    while left < right:
        mid = (left + right) >> 1

        if guess(mid) > 0:
            left = mid + 1
        else:
            right = mid

    return left


# 392 Is Subsequence
# 仅包含小写字母的字符串s是否是t的子序列，t可能会很长~=500000，s是短字符串<=100
# 思路: 哈希，字母作key，对应字母的下标作value，然后将t存入
def subSequence(s, t):
    dp = dict()
    for i in range(26):
        dp[chr(97 + i)] = []

    for index, item in enumerate(t):
        dp.get(item).append(index)

    tag = -1
    for subStr in s:
        left = 0
        size = len(dp.get(subStr))
        right = size

        while left < right:
            mid = (left + right) >> 1

            if dp.get(subStr)[mid] > tag:
                right = mid
            else:
                left = mid + 1

        if size == 0 or dp.get(subStr)[left] < tag:
            return False

        tag = dp.get(subStr)[left]

    return True


# 441 Arranging Coins
# n枚硬币，摆成阶梯形状，第k行正好有k枚硬币，找出可形成完整阶梯行第总行数
def arrangeCoins(n):
    left = 0
    right = n

    while left < right:
        # 一定要取右中位数，左中位数可能会死循环
        mid = (left + right + 1) >> 1
        value = mid * (1 + mid) / 2

        if value > n:
            right = mid - 1
        else:
            left = mid

    return left


# 475 Heaters
# 供暖器加热半径固定，房屋和供暖器在一条水平线上，找到覆盖所有房屋的最小加热半径
# 输入房屋和供暖器的位置，输出加热半径
# 思路: 找出离房屋最近的供暖器，再选出距离最大的
def findRadius(houses, heaters):
    res = [] # 每个房屋和供暖器的最短距离
    size = len(heaters)

    if size == 1:
        return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))

    for house in houses:
        left = 0
        right = size

        while left < right:
            mid = (left + right) >> 1

            if heaters[mid] < house:
                left = mid + 1
            else:
                right = mid

        if left > size - 1:
            left = size - 1

        indexHeater = heaters[left]

        if indexHeater == house:
            res.append(0)
        elif indexHeater < house:
            res.append(house - indexHeater)
        else:
            res.append(min(indexHeater - house, house - heaters[left - 1]))

    return max(res)


# 744 Find Smallest Letter Greater Than Target
# 只包含小写字母的有序数组letters和目标字母target，letters中比target大的最小字母
def nextGreatestLetter(letters, target):
    if letters[0] > target or letters[-1] <= target:
        return letters[0]

    left = 0
    right = len(letters)

    while left < right:
        mid = (left + right) >> 1

        if letters[mid] > target:
            if letters[mid - 1] > target:
                right = mid
            else:
                return letters[mid]
        else:
            left = mid + 1

    return letters[left]


# 704 Binary Search
def search(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) >> 1

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left if nums[left] == target else -1


# 852 Peak Index in a Mountain Array
# A.length >= 3, A[0]<A[1]<...<A[i]>A[i+1]>...>A[A.length-1], 找到峰顶索引
def peakIndexInMountainArray(A):
    left = 0
    right = len(A) - 1

    while left < right:
        mid = (left + right) >> 1

        if A[mid] < A[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# 1064 Fixed Point
# 生序数组A，返回A[i]==i的最小索引，不存在返回-1
def fixedPoint(A):
    left = 0
    right = len(A)

    while left < right:
        mid = (left + right) >> 1

        if A[mid] < mid:
            left = mid + 1
        else:
            right = mid

    return left if A[left] == left else -1


# 1150 Check If a Number Is Majority Element in a Sorted Array
# 生序数组nums，nums中绝大多数(长度为N的数组中出现超过N/2次)等于target则返回True否则False
def majorityElement(nums, target):
    return nums.count(target) > (len(nums) >> 1) 


# 1237 Find Positive Integer Solution for a Given Equation
def findSolution(customfunction, z):
    pass