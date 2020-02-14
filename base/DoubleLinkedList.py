from base import DoubleNode
from DoubleNode import Node

# 双向链表，尾节点的后续和头节点的前驱都None，链表为空则头节点为None
class DoubleLinkedList(object):

    def __init__(self):
        self.__head = None

    # 头插法，逆序插入到链表头部
    def add(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
        else:
            newNode.setNext(self.__head)
            self.__head.setPrev(newNode)
            self.__head = newNode

    # 尾插法，顺序插入到链表尾部
    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
        else:
            currentHead = self.__head
            while currentHead.getNext() is not None:
                currentHead = currentHead.getNext()

            currentHead.setNext(newNode)
            newNode.setPrev(currentHead)

    # 插入指定位置
    def insert(self, data, pos=0):
        if pos <= 0:
            self.add(data)
        elif pos > self.size() - 1:
            self.append(data)
        else:
            newNode = Node(data)
            preHead = self.__head
            count = 0

            # preHead指向指定位置前一个位置pos-1
            while count < pos - 1:
                count += 1
                preHead = preHead.getNext()

            newNode.setPrev(preHead)
            newNode.setNext(preHead.getNext())
            preHead.getNext().setPrev(newNode)
            preHead.setNext(newNode)

    def remove(self, data):
        currentHead = self.__head

        while currentHead is not None:
            nextp = currentHead.getNext()

            if currentHead.getData() == data:
                if currentHead is self.__head:
                    self.__head = nextp
                    if nextp:
                        nextp.setPrev(None)
                else:
                    currentHead.getPrev().setNext(nextp)
                    if nextp:
                        nextp.setPrev(currentHead.getPrev())
            else:
                currentHead = nextp

    def search(self, data):
        currentHead = self.__head

        while currentHead is not None:
            if currentHead.getData() == data:
                return True
            else:
                currentHead = currentHead.getNext()

        return False

    def size(self):
        count = 0
        currentHead = self.__head

        while currentHead is not None:
            count += 1
            currentHead = currentHead.getNext()

        return count

    def isEmpty(self):
        return self.__head is None

    def travel(self):
        dataList = []
        currentHead = self.__head

        while currentHead is not None:
            dataList.append(currentHead.getData())
            currentHead = currentHead.getNext()

        return dataList
