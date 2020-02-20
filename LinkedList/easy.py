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
    # 迭代
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
