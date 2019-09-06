"""
双向链表的封装
"""


class Node(object):
    """
    双向链表节点的封装
    """

    def __init__(self, element):
        self.element = element  # 数据域
        # 指针域
        self.next = None  # 指向后继节点的指针
        self.prev = None  # 指向前驱节点的指针

    def __str__(self):
        return self.element


class DuLinkList(object):
    """
    双向链表的封装
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断双向链表是否为空"""
        return self.head == None

    def __len__(self):
        """获取双向链表的长度"""
        if self.is_empty():
            return 0
        cur = self.head
        linkLen = 0
        while cur:
            cur = cur.next
            linkLen += 1
        return linkLen

    def travel(self):
        """遍历链表元素"""
        if not self.is_empty():
            cur = self.head
            while cur.next != None:
                print(cur.element, end=',')
                cur = cur.next
            print(cur.element)
        else:
            print("空链表")

    def add(self, item):
        """
        头部添加元素
            1. 先创建一个保存item值的节点
            2. 将新节点的链接域next指向头节点，即head指向的位置
            3. 将链表的头head指向新节点
        """
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, item):
        """
        尾部添加元素
            1. 先判断链表是否为空，若是空链表，则将head指向新节点
            2. 若不为空，则找到尾部，将尾节点的next指向新节点
        """
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, index, item):
        """
        指定位置添加元素
            1. 若指定位置index为第一个元素之前，则执行头部插入
            2. 若指定位置超过链表尾部，则执行尾部插入
            3. 否则， 找到指定位置
        """
        if index <= 0:
            self.add(item)
        elif index >= len(self):
            self.append(item)
        else:
            node = Node(item)
            count = 0  # 当前位置
            cur = self.head
            while count < index - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
            node.prev = cur
            cur.next.prev = node

    def remove(self, item):
        """
        删除指定元素的节点：
         1 2 3 4 5
         1. 如果删除的是头结点， 指针直接指向头结点的下一个节点;
         2. 如果删除的不是头结点， 一直循环， 知道找到要删除的节点元素;
        """
        if self.is_empty():
            return
        pre = None
        cur = self.head
        # 如果删除的是头结点， 指针直接指向头结点的下一个节点;
        if cur.element == item:
            self.head = self.head.next
        else:
            while cur:
                if cur.element != item:
                    pre = cur
                    cur = cur.next
                else:
                    # 判断删除的是否为尾部节点， 如果是， 则直接让pre.next指向为None;
                    if not cur.next:
                        pre.next = None
                        break

                    else:
                        # pre.next = pre.next.next
                        pre.next = cur.next
                        cur.next.prev = pre
                        break


    def search(self, item):
        cur = self.head
        while cur:
            if cur.element == item:
                return  True
            cur = cur.next
        else:
            return  False

if __name__ == '__main__':
    # 实例化双向链表对象
    link = DuLinkList()
    # 长度获取
    print("链表长度: ", len(link))
    # 遍历链表
    link.travel()
    print("链表是否为空? ", link.is_empty())

    # print("添加头结点：")
    # for item in range(5):
    #     link.add(item)  #  4 3 2 1 0
    #
    # # 长度获取
    # print("链表长度: ", len(link))
    # # 遍历链表
    # link.travel()
    # print("链表是否为空? ", link.is_empty())

    print("追加结点：")
    for item in range(5):
        link.append(item)  # 0  python 1  2 3 4

    # 长度获取
    print("链表长度: ", len(link))
    # 遍历链表
    link.travel()
    print("链表是否为空? ", link.is_empty())

    print("指定位置插入元素")
    link.insert(1, 'python')
    # 长度获取
    print("链表长度: ", len(link))
    # 遍历链表
    link.travel()
    print("链表是否为空? ", link.is_empty())

    print("删除元素")  # 0  python 1  2 3 4
    link.remove(4)
    link.travel()


    print("查找元素:")
    print(link.search(1))
    print(link.search(10))
