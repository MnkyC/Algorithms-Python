# 数据结构基本都是数组和链表演变而来
# 链式栈，单链表实现，尾部操作需要遍历，头部操作只需要头指针移动即可


from base import SingleNode
from SingleNode import Node


class LinkedListStack(object):

    def __init__(self):
        self.__head = None
        self.__count = 0

    # 头插法
    def push(self, data):
        newNode = Node(data, nextp=self.__head)
        self.__head = newNode
        self.__count += 1

    # 头删法
    def pop(self, data):
        if self.isEmpty():
            return None

        self.__head = self.__head.getNext()
        self.__count -= 1

        return self.__head

    def peek(self):
        if self.isEmpty():
            return None

        return self.__head.getData()

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__head is None
