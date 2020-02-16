'''
快速排序, 平均时间O(nlog(n)), 最好O(nlog(n)), 最坏O(n^2), 空间O(log(n)), in, 不稳定
思路：分治
步骤：
    1序列中挑选一个元素（如第一个元素）作为“基准”
    2比基准小的都放在基准前面，大的在基准后面，相同则任一边，操作结束基准就在序列中间
    3递归将小于基准的子序列和大于基准的子序列进行快速排序
'''


def quickSort(lst, left=None, right=None):

    print("快速排序")
    print("数据:{}".format(lst))

    left = 0 if not isinstance(left, (int, float)) else left
    right = len(lst) - 1 if not isinstance(right, (int, float)) else right

    if left < right:
        print('对区间[{}, {}]进行快速排序'.format(left, right))
        partitionIndex = partition(lst, left, right)
        quickSort(lst, left, partitionIndex - 1)
        quickSort(lst, partitionIndex + 1, right)

    return lst


def partition(lst, left, right):
    pivot = left
    index = pivot + 1
    i = index

    while i <= right:
        if lst[i] < lst[pivot]:
            swap(lst, i, index)
            print('交换数据:{}'.format(lst))
            index += 1

        i += 1

    swap(lst, pivot, index - 1)

    print('初始基准位置{}, 排序后的数据:{}, 现在基准位置{}'.format(pivot, lst, index - 1))

    return index - 1


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
