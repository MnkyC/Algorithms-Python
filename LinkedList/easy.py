# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1290 Convert Binary Number in a Linked List to Integer
# 二进制链表转整数
# 单链表引用节点head，每个节点的值不是0就是1，已知是整数数字的二进制表示形式，返回所表示的十进制值
def getDecimalValue(head):
    cur = head
    sum = 0

    while cur is not None:
        sum = sum << 1 | cur.val
        cur = cur.next


# 876 Middle of the Linked List
# 链表的中间节点
# 头节点head的非空单链表，返回中间节点，若有两个，返回第二个
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# 206 Reverse Linked List
# 反转一个单链表，用迭代和递归
def reverseList(head):
    # 迭代，设置一个哨兵节点prev
    # prev = None
    # cur = head

    # while cur is not None:
    #     nextNode = cur.next
    #     cur.next = prev
    #     prev = cur
    #     cur = nextNode

    # return prev

    # 递归，停止条件是当前为空或下一个节点为空
    if head is None or head.next is None:
        return head

    # cur是最后一个节点
    cur = reverseList(head.next)
    # 最后一个节点的next指向前一节点
    head.next.next = head
    # 防止循环，设为空
    head.next = None

    return cur


# 237 Delete Node in a Linked List
# 删除链表中的节点
# 一个链表head = [4,5,1,9], 只提供要删除的非末尾的节点，不返回任何结果
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


# 21 Merge Two Sorted Lists
# 合并两个有序链表, 数值从小到大排序并返回
def mergeTwoLists(l1, l2):
    # 递归
    # if l1 is None:
    #     return l2

    # if l2 is None:
    #     return l1

    # if l1.val < l2.val:
    #     l1.next = mergeTwoLists(l1.next, l2)
    #     return l1
    # else:
    #     l2.next = mergeTwoLists(l1, l2.next)
    #     return l2

    # 迭代, 哨兵节点prev
    prev = ListNode(-1)

    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next

    prev.next = l1 if l1 is not None else l2

    return prev.next


# 83 Remove Duplicates from Sorted List
# 删除排序链表中的重复元素
def deleteDuplicates(head):
    cur = head

    while cur.next is not None and cur is not None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head
