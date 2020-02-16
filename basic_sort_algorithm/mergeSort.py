'''
归并排序, 平均时间O(nlog(n)), 最好O(nlog(n)), 最坏O(nlog(n)), 空间O(n), out, 稳定
思路：分治
步骤：
   1申请空间，大小为已经排好序的序列之和，该空间用于存储合并后的序列
   2设定两个指针，分别指向两个已经排序的序列的起始位置
   3比较两个指针指向的元素，选择较小的元素放入合并空间，移动指针到下一位置
   4重复步骤3直到序列末尾
   5将另一个序列剩下的所有元素直接复制到合并序列的末尾
'''


def mergeSort(lst):
    size = len(lst)
    if size < 2:
        return lst

    print("归并排序")
    print("数据:{0}".format(lst))

    mid = len(lst) >> 1
    left = lst[:mid]
    right = lst[mid:]

    print("分成两部分数据:{0}, {1}".format(left, right))

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    rlt = []

    while left and right:
        if left[0] < right[0]:
            rlt.append(left.pop(0))
        else:
            rlt.append(right.pop(0))

    while left:
        rlt.append(left.pop(0))

    while right:
        rlt.append(right.pop(0))

    print("完成排序的数据:{}".format(rlt))

    return rlt
