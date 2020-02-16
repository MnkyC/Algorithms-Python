'''
选择排序, 平均时间O(n^2), 最好O(n^2), 最坏O(n^2), 空间O(1), in-place, 不稳定
步骤：
   1未排序序列中找最小（大）值，放到起始位置
   2剩余的未排序序列中继续找最小（大）值，放到已排序序列的末尾
   3重复步骤2
不管什么数据规模都是O(n^2)，所以使用时数据规模越小越好
需要进行n*(n-1)/2次交换，比较冒泡排序，其交换次数更少
冒泡排序每次遍历后前者>后者就会交换，但是前者可能不是最小的，还会发生交换，需要多次才能确定，比较耗时
'''


def selectionSort(lst):
    countCompare = 0
    countSwap = 0
    length = len(lst)

    print("选择排序")
    print("数据:{0}".format(lst))

    for i in range(0, length-1):
        minIndex = i

        for j in range(i+1, length):
            countCompare += 1
            if lst[j] < lst[minIndex]:
                minIndex = j

        countCompare += 1
        if minIndex != i:
            countSwap += 1
            lst[i], lst[minIndex] = lst[minIndex], lst[i]

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst

# 选择排序优化，每次循环确定最小最大值
def selectionSortOpt(lst):
    countCompare = 0
    countSwap = 0
    length = len(lst)
    mid = length >> 1

    print("选择排序优化")
    print("数据:{0}".format(lst))

    for i in range(0, mid):
        minIndex = i
        maxIndex = i

        for j in range(i+1, length-i):
            countCompare += 2
            if lst[j] < lst[minIndex]:
                minIndex = j
            elif lst[j] > lst[maxIndex]:
                maxIndex = j

        countCompare += 2

        if minIndex != i:
            countSwap += 1
            lst[i], lst[minIndex] = lst[minIndex], lst[i]
            countCompare += 1
            if maxIndex == i:
                maxIndex = minIndex

        if maxIndex != length-1-i:
            countSwap += 1
            lst[length-1-i], lst[maxIndex] = lst[maxIndex], lst[length-1-i]

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst
