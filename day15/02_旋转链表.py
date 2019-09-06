from SingleLink import SingleLink
def rorateRight(link, k):
    """
    向右移动k个元素(绕圈法):
        1. 判断录入数据的合法性? link是否存在? link是否为空? k是否为非负数.
        2. 如果数据合法；
            1). 访问到链表的最后
            2). 首尾相连
            3). 对k值进行处理:  k = k%len(link)
            4). 让指针移动到（len-k-1）, 更新链表头结点
            5). 断开链表循环的部分
    :param link: 单链表对象
    :param k: 向右移动的数值
    :return:
    """
    # 1. 判断录入数据的合法性? link是否存在? link是否为空? k是否为非负数.
    if not link:
        return
    if not link.head:
        return
    if k < 0:
        return

    #  2. 如果数据合法；
    # 1).访问到链表的最后
    cur = link.head
    count = 1  # 链表的长度
    while cur.next:
        cur = cur.next
        count += 1
    # 2). 首尾相连
    cur.next = link.head

    # 3). 对k值进行处理:  k = k%len(link)
    k = k % count

    # 4).让指针移动到（len - k - 1）,
    pre = link.head  # 最终指向要断开节点的前一个节点
    for i in range(count - k - 1):
        pre = pre.next

    # 更新链表头结点
    link.head = pre.next

    # 5).断开链表循环的部分
    pre.next = None
    return link


if __name__ == '__main__':
    link = SingleLink()
    for item in range(5):  # 1 2 3 4 5
        link.append(item + 1)
    link.trvel()


    print("测试.........")
    link1 = rorateRight(link, 8)
    link1.trvel()
