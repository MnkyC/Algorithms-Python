'''
冒泡排序, 平均时间O(n^2), 最好O(n), 最坏O(n^2), 空间O(1), in-place, 稳定
步骤：
   1比较相邻元素，前者比后者大就交换
   2每一对相邻元素进行步骤1，除了最后一个
'''


def bubbleSort(lst):
    countCompare = 0
    countSwap = 0
    length = len(lst)

    print('冒泡排序')
    print("数据:{0}".format(lst))

    for i in range(1, length):
        for j in range(0, length - i):
            countCompare += 1
            if lst[j] > lst[j+1]:
                countSwap += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst

# 冒泡排序优化1，立flag记录是否有交换，若遍历完没有交换就已经有序
def bubbleSortOpt(lst):
    countCompare = 0
    countSwap = 0
    length = len(lst)

    print('冒泡排序优化1')
    print("数据:{0}".format(lst))

    for i in range(1, length):
        exchange = False
        for j in range(0, length - i):
            countCompare += 1
            if lst[j] > lst[j+1]:
                countSwap += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchange = True

        if not exchange:
            break

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst

# 冒泡排序优化2，pos后的数据在上一次没有交换，则之后这些数据不需要重复比较
def bubbleSortOpt2(lst):
    countCompare = 0
    countSwap = 0
    endPoint = len(lst) - 1

    print('冒泡排序优化2')
    print("数据:{0}".format(lst))

    while endPoint > 0:
        pos = 1
        for j in range(0, endPoint):
            countCompare += 1
            if lst[j] > lst[j+1]:
                countSwap += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
                pos = j

        endPoint = pos - 1

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst

# 冒泡排序优化3，每次循环中进行正反两次冒泡得到最大最小值
def bubbleSortOpt3(lst):
    countCompare = 0
    countSwap = 0
    start = 0
    end = len(lst) - 1

    print('冒泡排序优化3')
    print("数据:{0}".format(lst))

    while start < end:
        for j in range(start, end):
            countCompare += 1
            if lst[j] > lst[j+1]:
                countSwap += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
        end -= 1

        for j in range(end, start, -1):
            countCompare += 1
            if lst[j-1] > lst[j]:
                countSwap += 1
                lst[j-1], lst[j] = lst[j], lst[j-1]
        start += 1

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst
