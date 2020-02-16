'''
插入排序, 平均时间O(n^2), 最好O(n), 最坏O(n^2), 空间O(1), in, 稳定
步骤：
   1第一个元素看作有序序列，第二个到最后的元素看作未排序序列
   2依次扫描未排序序列，将每个元素插入到有序序列中的适当位置，若有元素相等则插入到后面
'''


def insertionSort(lst):
    countCompare = 0
    countSwap = 0
    length = len(lst)

    print("插入排序")
    print("数据:{0}".format(lst))

    for i in range(length):
        preIndex = i - 1
        currentItem = lst[i]

        countCompare += 1
        while preIndex >= 0 and lst[preIndex] > currentItem:
            lst[preIndex+1] = lst[preIndex]
            preIndex -= 1

        lst[preIndex+1] = currentItem

    print("统计:{0}次比较, {1}次交换, {2}".format(countCompare, countSwap, lst))

    return lst
