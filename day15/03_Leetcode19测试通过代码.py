# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        if n <= 0:
            return 
        # 1). p, q
        p = q = head
        # 2). 让p指针和q指针之间的间距为k；
        for i in range(n):
            q = q.next
        # 特例： 如果n=链表的长度， 也就是删除头节点
        if not q:
            head = head.next
            return head
            # 3). 让p指针和q指针一块向后移动， 直到q.next为空的时候停止移动;
        while q.next:
            p = p.next
            q = q.next

        # 4). p指针指向哪里? 指向要删除的元素的前一个节点
        p.next = p.next.next

        return head
