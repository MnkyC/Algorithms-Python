from base import SingleNode
from SingleNode import Node

# 单向循环链表，尾节点后续为头节点
class SingleCircleLinkedList(object):

    def __init__(self):
        self.__head = None

    # 头插法，逆序插入到链表头部
    def add(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
            newNode.setNext(self.__head)
        else:
            # 创建新节点，其指针域指向头节点
            newNode = Node(data, nextp=self.__head)
            currentHead = self.__head
            while currentHead.getNext() is not self.__head:
                currentHead = currentHead.getNext()

            # 尾节点指向新节点
            currentHead.setNext(newNode)
            self.__head = newNode

    # 尾插法，顺序插入到链表尾部
    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
            newNode.setNext(self.__head)
        else:
            currentHead = self.__head
            while currentHead.getNext() is not self.__head:
                currentHead = currentHead.getNext()

            currentHead.setNext(newNode)
            newNode.setNext(self.__head)

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

            # 新节点的指针域指向插入位置的节点
            newNode.setNext(preHead.getNext())
            # 插入位置前一个节点的指针域指向新节点
            preHead.setNext(newNode)

    def remove(self, data):
        if self.isEmpty():
            return

        currentHead = self.__head
        preNode = None

        while currentHead.getNext() is not self.__head:
            if currentHead.getData() == data:
                if currentHead is self.__head:
                    rear = self.__head
                    while rear.getNext() is not self.__head:
                        rear = rear.getNext()

                    self.__head = currentHead.getNext()
                    rear.setNext(self.__head)
                else:
                    # 删除位置前一个节点的指针域指向删除位置后的那个节点
                    preNode.setNext(currentHead.getNext())
            else:
                preNode = currentHead
                currentHead = currentHead.getNext()

        # 尾节点处理
        if currentHead.getData() == data:
            if currentHead is self.__head:
                self.__head = None
            else:
                preNode.setNext(self.__head)

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
