class Node(object):

    def __init__(self, data, lchild=None, rchild=None):
        self.__data = data
        self.__lchild = lchild
        self.__rchild = rchild

    def setData(self, data):
        self.__data = data

    def setLChild(self, lchild):
        self.__lchild = lchild

    def setRChild(self, rchild):
        self.__rchild = rchild

    def getData(self):
        return self.__data

    def getLChild(self):
        return self.__lchild

    def getRChild(self):
        return self.__rchild
