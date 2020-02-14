from base import DoubleNode
from DoubleNode import Node

# 双向循环链表，尾节点后续为头节点，头节点的前驱为尾节点，链表为空则头节点为None
class DoubleCircleLinkedList(object):

    def __init__(self):
        self.__head = None

    # 头插法，逆序插入到链表头部
    def add(self, data):
        newNode = Node(data)

        if self.isEmpty():
            newNode.setPrev(newNode)
            newNode.setNext(newNode)
            self.__head = newNode
        else:
            newNode.setNext(self.__head)
            newNode.setPrev(self.__head.getPrev())
            self.__head.getPrev().setNext(newNode)
            self.__head.setPrev(newNode)
            self.__head = newNode

    # 尾插法，顺序插入到链表尾部
    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.add(data)
        else:
            newNode.setNext(self.__head)
            # head的前驱就是链表尾部
            newNode.setPrev(self.__head.getPrev())
            self.__head.getPrev().setNext(newNode)
            self.__head.setPrev(newNode)

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
        if self.isEmpty():
            return

        currentHead = self.__head

        if currentHead.getData() == data:
            if self.size() == 1:
                self.__head = None
            else:
                prevp = currentHead.getPrev()
                nextp = currentHead.getNext()
                self.__head = nextp
                nextp.setPrev(currentHead.getPrev())
                prevp.setNext(nextp)
        else:
            while currentHead.getNext() is not self.__head:
                nextp = currentHead.getNext()

                if nextp.getData() == data:
                    nextp.getPrev().setNext(nextp.getNext())
                    nextp.getNext().setPrev(nextp.getPrev())
                else:
                    currentHead = nextp

            # 尾节点处理
            if currentHead.getData() == data:
                if currentHead is self.__head:
                    self.__head = None
                else:
                    currentHead.getPrev().setNext(self.__head)
                    self.__head.setNext(currentHead.getPrev())

    def search(self, data):
        if self.isEmpty():
            return False

        currentHead = self.__head

        while currentHead.getNext() is not self.__head:
            if currentHead.getData() == data:
                return True
            else:
                currentHead = currentHead.getNext()

        if currentHead.getData() == data:
            return True

        return False

    def size(self):
        if self.isEmpty():
            return 0

        currentHead = self.__head
        count = 1
        while currentHead.getNext() is not self.__head:
            count += 1
            currentHead = currentHead.getNext()

        return count

    def isEmpty(self):
        return self.__head is None

    def travel(self):
        if self.isEmpty():
            return []

        dataList = []
        currentHead = self.__head
        dataList.append(currentHead.getData())

        while currentHead.getNext() is not self.__head:
            currentHead = currentHead.getNext()
            dataList.append(currentHead.getData())

        return dataList
