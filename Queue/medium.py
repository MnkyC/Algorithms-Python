from collections import deque

# 582 Kill Process
# pid和ppid两个列表，杀掉父进程的话子进程也会被杀掉，一个父进程可以有多个子进程
def killProcess(pid, ppid, kill):
    rlt = []
    q = deque([kill])
    hashTable = dict()
    for item in ppid:
        hashTable[item] = []

    for index, item in enumerate(pid):
        hashTable.get(ppid[index]).append(item)

    while q:
        item = q.popleft()
        rlt.append(item)
        for value in hashTable.get(item, []):
            q.append(value)

    return rlt

# 622 Design Circular Queue
# 设计循环队列，大小为k，普通队列一旦满了即使队列前面有空间也不能插入，但是循环队列可以利用这部分空间
class Node:

    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__capacity = k
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        newNode = Node(value)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = self.__head
        else:
            self.__tail.next = newNode
            self.__tail = newNode

        self.__count += 1

        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.__head = self.__head.next
        self.__count -= 1

        return True

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.__head.value

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.__tail.value

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__count == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.__count == self.__capacity


# 641 Design Circular Deque
# 设计循环双端队列，大小为k
class DoubleNode:

    def __init__(self, value, prevNode=None, nextNode=None):
        self.value = value
        self.prev = prevNode
        self.next = nextNode


class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.__capacity = k
        self.__head = None
        self.__tail = None
        self.__count = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.__head = DoubleNode(value)
            self.__tail = self.__head
        else:
            newNode = DoubleNode(value, None, self.__head)
            self.__head.prev = newNode
            self.__head = newNode

        self.__count += 1

        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.__tail = DoubleNode(value)
            self.__head = self.__tail
        else:
            self.__tail.next = DoubleNode(value, self.__tail, None)
            self.__tail = self.__tail.next

        self.__count += 1

        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.__head = self.__head.next

        if self.__head:
            self.__head.prev = None

        self.__count -= 1

        if self.isEmpty():
            self.__tail = None

        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.__tail = self.__tail.prev

        if self.__tail:
            self.__tail.next = None

        self.__count -= 1

        if self.isEmpty():
            self.__head = None

        return True

    def getFront(self):
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.__head.value

    def getRear(self):
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.__tail.value

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return self.__count == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        return self.__count == self.__capacity


# 621 Task Scheduler
def leastInterval(tasks, n):
    pass
