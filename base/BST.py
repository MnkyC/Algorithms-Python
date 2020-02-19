'''
数据结构基本都是数组和链表演变而来

节点的度：含有子树的个数
树的度：最大的节点度
叶节点/终端节点：度为零的节点
父节点/父亲节点：一个节点含有子节点，则该节点为这些子节点的父节点
子节点/孩子节点：
兄弟节点：具有相同父节点的节点的互称
节点的层次：根节点开始，为第1层，根的子节点为第2层，以此类推
树的高度/深度：树中节点的最大层次
堂兄弟节点：父节点在同一层的节点的互称
节点的祖先：从根到该节点经历的分支上的所有节点
子孙：某节点为根的子树中的任一节点
森林：n(n>0)棵互不相交的树的集合

遍历：深度优先遍历（先序中序后序遍历，一般用递归，也能用栈），广度优先遍历（层次遍历，一般用队列）
'''

from base import TreeNode
from TreeNode import Node


class BST(object):

    def __init__(self):
        self.__root = None
        self.__items = []

    def add(self, item):
        newNode = Node(item)

        if self.__root is None:
            self.__root = newNode
            self.__items.append(self.__root)
        else:
            treeNode = self.__items[0]
            if treeNode.getLChild() is None:
                treeNode.setLChild(newNode)
                self.__items.append(treeNode.getLChild())
            elif treeNode.getRChild() is None:
                treeNode.setRChild(newNode)
                self.__items.append(treeNode.getLChild())

    # 递归实现先序遍历
    def frontRecursiveTravel(self, root, dataList=[]):
        if root is None:
            return

        dataList.append(root.getData())
        self.frontRecursiveTravel(root.getLChild(), dataList)
        self.frontRecursiveTravel(root.getRChild(), dataList)

        return dataList

    # 递归实现中序遍历
    def middleRecursiveTravel(self, root, dataList=[]):
        if root is None:
            return

        self.middleRecursiveTravel(root.getLChild(), dataList)
        dataList.append(root.getData())
        self.middleRecursiveTravel(root.getRChild(), dataList)

        return dataList

    # 递归实现后序遍历
    def laterRecursiveTravel(self, root, dataList=[]):
        if root is None:
            return

        self.laterRecursiveTravel(root.getLChild(), dataList)
        self.laterRecursiveTravel(root.getRChild(), dataList)
        dataList.append(root.getData())

        return dataList

    # 栈实现先序遍历
    def frontStackTravel(self, root):
        if root is None:
            return

        dataList = []
        stack = []
        currentNode = root

        while currentNode or stack:
            while currentNode:
                dataList.append(currentNode.getData())
                stack.append(currentNode)
                currentNode = currentNode.getLChild()

            currentNode = stack.pop()
            currentNode = currentNode.getRChild()

        return dataList

    # 栈实现中序遍历
    def middleStackTravel(self, root):
        if root is None:
            return

        dataList = []
        stack = []
        currentNode = root

        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.getLChild()

            currentNode = stack.pop()
            dataList.append(currentNode.getData())
            currentNode = currentNode.getRChild()

        return dataList

    # 栈实现后序遍历
    def laterStackTravel(self, root):
        if root is None:
            return

        dataList = []
        stack = []
        currentNode = root
        prevNode = root

        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.getLChild()

            currentNode = stack[-1]

            if currentNode.getRChild() is None or currentNode.getRChild() is prevNode:
                dataList.append(currentNode.getData())
                currentNode = stack.pop()
                prevNode = currentNode
                currentNode = None
            else:
                currentNode = currentNode.getRChild()

        return dataList

    # 队列实现层次遍历
    def bfs(self, root):
        if root is None:
            return

        dataList = []
        queue = []
        currentNode = root
        queue.append(currentNode)

        while queue:
            currentNode = queue.pop(0)
            dataList.append(currentNode.getData())

            if currentNode.getLChild() is not None:
                queue.append(currentNode.getLChild())

            if currentNode.getRChild() is not None:
                queue.append(currentNode.getRChild())
