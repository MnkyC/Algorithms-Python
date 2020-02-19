'''
数据结构基本都是数组和链表演变而来

堆，实际是一个完全二叉树，可用数组实现
堆，又叫优先队列，但堆不是队列，队列按照进队列的先后顺序，堆按照元素的优先级
基本操作
    插入
        堆是优先队列，只能尾部添加，添加后可能破坏结构，需要从下到上调整
    移除
        堆是优先队列，只能头部移除，移除后使用尾部元素填充头部，头部开始进行下沉
    上浮：当子节点的值比父节点大
    下沉：当父节点的值比子节点小

'''

# 最大堆：节点的值>=其子节点的值，根节点最大
class MaxHeap(object):

    def __init__(self):
        self.__items = []
        self.__count = 0

    def push(self, item):
        self.__items.append(item)
        self.__count += 1

        if self.__count > 1:
            self.shiftup()

        return True

    def pop(self):
        if self.isEmpty():
            return None

        item = self.__items[0]
        self.__items[0] = self.__items.pop()
        self.__count -= 1

        if self.__count > 1:
            self.shiftdown()

        return item

    def shiftup(self):
        index = self.__count - 1
        parent = (self.__count - 2) >> 1

        while index > 0 and self.__items[parent] < self.__items[index]:
            self.__items[parent], self.__items[index] = self.__items[index], self.__items[parent]
            index = parent
            parent = (index - 1) >> 1

    def shiftdown(self):
        parent = 0
        lchild = (parent << 1) + 1

        while lchild < self.__count:
            if lchild + 1 < self.__count and self.__items[lchild+1] > self.__items[lchild]:
                lchild += 1

            if self.__items[parent] >= self.__items[lchild]:
                break

            self.__items[parent], self.__items[lchild] = self.__items[lchild], self.__items[parent]
            parent = lchild
            lchild = (parent << 1) + 1

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0
