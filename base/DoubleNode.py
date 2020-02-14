# 每个节点中next存放后续节点，prev存放前驱节点
class Node(object):

    def __init__(self, data, prevp=None, nextp=None):
        self.__data = data
        self.__prev = prevp
        self.__next = nextp

    def setData(self, data):
        self.__data = data

    def setPrev(self, prevp):
        self.__prev = prevp

    def setNext(self, nextp):
        self.__next = nextp

    def getData(self):
        return self.__data

    def getPrev(self):
        return self.__prev

    def getNext(self):
        return self.__next
