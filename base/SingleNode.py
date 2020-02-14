# 每个节点有一个属性next存放后续节点
class Node(object):

    def __init__(self, data, nextp=None):
        self.__data = data
        self.__next = nextp

    def setData(self, data):
        self.__data = data

    def setNext(self, nextp):
        self.__next = nextp

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next
