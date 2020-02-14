from base import SingleNode
from SingleNode import Node

# 单链表，每个节点两个域，信息域和指针域，指针域指向下一个节点，最后一个节点指向空，head->A|next->B|next->C|None
class SingleLinkedList(object):

    def __init__(self):
        self.__head = None

    # 头插法，逆序插入到链表头部
    def add(self, data):
        # 创建新节点，其指针域指向头节点
        newNode = Node(data, nextp=self.__head)
        # 头节点指向新节点
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
        currentHead = self.__head
        preNode = None

        while currentHead is not None:
            if currentHead.getData() == data:
                if not preNode:
                    currentHead = currentHead.getNext()
                else:
                    # 删除位置前一个节点的指针域指向删除位置后的那个节点
                    preNode.setNext(currentHead.getNext())
            else:
                preNode = currentHead
                currentHead = currentHead.getNext()

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
