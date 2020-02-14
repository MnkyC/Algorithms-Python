# 数据结构基本都是数组和链表演变而来
# 顺序栈，数组实现，满了就不能再添加，头部操作需要遍历，尾部操作则无需遍历


class ArrayStack(object):

    def __init__(self, capacity):
        self.__items = [0 for i in range(capacity)]
        self.__capacity = capacity
        self.__count = 0

    def push(self, item):
        if self.__count == self.__capacity:
            return False

        self.__items[self.__count] = item
        self.__count += 1

        return True

    def pop(self):
        if self.isEmpty():
            return None

        item = self.__items[self.__count - 1]
        self.__count -= 1

        return item

    def peek(self):
        if self.isEmpty():
            return None

        return self.__items[self.__count - 1]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0
