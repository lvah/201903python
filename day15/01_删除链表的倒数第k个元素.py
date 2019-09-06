"""
删除链表的倒数第k个元素
"""
from SingleLink import SingleLink
def delKthToTail(link, k):
    """
    删除链表的倒数第k个元素
        1. 判断用户输入的合法性? link, k
        2. 如果输入数据合法
            1). p, q
            2). 让p指针和q指针之间的间距为k；
            3). 让p指针和q指针一块向后移动， 直到q.next为空的时候停止移动;
            4). p指针指向哪里? 指向要删除的元素的前一个节点 p.next = p.next.next
    :param link:
    :param k:
    :return:
    """
    if not link:
        return
    if not link.head:
        return
    if k <= 0:
        return
    # 1). p, q
    p = link.head
    q = link.head

    # 2). 让p指针和q指针之间的间距为k；
    for i in range(k):
        q = q.next
    # 3). 让p指针和q指针一块向后移动， 直到q.next为空的时候停止移动;
    while q.next:
        p = p.next
        q = q.next

    # 4). p指针指向哪里? 指向要删除的元素的前一个节点
    p.next = p.next.next

    return  link



if __name__ == '__main__':
    # 实例化一个单向链表
    link = SingleLink()
    # 向链表里面添加元素
    for item in range(5):
        link.append(item + 1)  # 1 2 3 4 5
    link.trvel()
    link1 = delKthToTail(link, 3)  # 1 2 3 5
    link1.trvel()
