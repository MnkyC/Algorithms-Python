# 数据结构基本都是数组和链表演变而来
# 顺序队列，数组实现


class ArrayQueue(object):

    def __init__(self, capacity):
        self.__items = [0 for i in range(capacity)]
        self.__capacity = capacity
        self.__count = 0

    def enqueue(self, item):
        if self.__count == self.__capacity:
            return False

        self.__items.insert(0, item)
        self.__count += 1

        return True

    def dequeue(self):
        if self.isEmpty():
            return None

        item = self.__items.pop()
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
