'''
1313 Decompress Run-Length Encoded List
行程长度编码压缩的整数列表nums（len(nums) % 2 = 0）
每对相邻的元素[a, b] = [nums[2*i], nums[2*i+1]](i>=0)，每对都表示解压后有a个值为b的元素，返回解压后的元素
'''
def decompressRLElist(nums):
    # nums[::2]是反复次数，nums[1::2]是出现的元素
    return [i for i, j in zip(nums[1::2], nums[::2]) for _ in range(j)]


# 1295 Find Numbers with Even Number of Digits
# 整数数组nums，返回其中位数为偶数的数字的个数
def findNumbers(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)


# 1351 Count Negative Numbers in a Sorted Matrix
# m * n的矩阵grid，无论是行还是列都以非递增顺序排列，统计并返回grid中负数的数目，m = grid.length, n = grid[i].length
def countNegatives(grid):
    count = 0
    m = grid.length
    n = grid[0].length

    for i in range(m):
        row = grid[i]

        # 整行都是负数，后面的行也不用遍历，直接计算
        if row[0] < 0:
            count += (m - i) * n
            break

        # 整行非负，跳过
        if row[-1] > 0:
            continue

        # 二分查找第一个小于0的索引
        first = binarySearch(row)
        count += n - first

    return count


def binarySearch(lst):
    left = 0
    right = len(lst)

    while left < right:
        mid = (left + right) >> 1

        if mid < 0:
            right = mid
        else:
            left = mid + 1

    return left


'''
1266 Minimum Time Visiting All Points
平面上n个点，坐标用整数表示points[i] = [xi, yi]，计算访问所有点需要的最小时间（秒为单位）
规则：每秒沿水平或竖直方向移动一个单位长度或对角线，按数组顺序依次访问
n = points.length, points[i].length = 2
'''
'''
思路
    两个点(x0, y0), (x1, y1)
    水平距离之差dx = |x0 - x1|, 垂直距离之差dy = |y0 - y1|
    dx < dy: 对角线移动dx次，再垂直移动dy - dx次，总计dx + (dy - dx) = dy次
    dx == dy: 对角线移动dx次
    dx > dy: 对角线移动dy次，再水平移动dx - dy次，总计dy + (dx - dy) = dx次
    所以，移动的最少次数是dx和dy的较大值
'''
def minTimeToVisitAllPoints(points):
    # size = len(points)
    # rlt = 0
    # x0, y0 = points[0]

    # for i in range(1, size):
    #     x1, y1 = points[i]
    #     rlt += max(abs(x0 - x1), abs(y0 - y1))
    #     x0, y0 = points[i]

    # return rlt

    size = len(points) - 1
    return sum(max(abs(points[i+1][0] - points[i][0]), abs(points[i+1][1] - points[i][1])) for i in range(size))
