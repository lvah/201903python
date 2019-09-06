"""
单链表的封装
"""


class Node(object):
    """
    单链表节点的封装
    """

    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLink(object):
    """
    单链表的封装
    """

    def __init__(self):
        # 默认情况下链表为空， 没有任何元素
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def __len__(self):
        """
        链表长度:
            1. 如果当前链表为空， 直接返回0；
            1. 如果当前链表不为空， 依次遍历链表的每一个元素，计算长度
        """
        if self.is_empty():
            return 0
        else:
            cur = self.head
            length = 0
            while cur != None:
                length += 1
                cur = cur.next
            return length

    def trvel(self):
        """遍历链表"""
        if not self.is_empty():
            cur = self.head
            while cur.next != None:
                print(cur.element, end=',')
                cur = cur.next
            print(cur.element)
        else:
            print("空链表")

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

    def add(self, item):
        """
        头部添加元素
            1. 先创建一个保存item值的节点
            2. 将新节点的链接域next指向头节点，即head指向的位置
            3. 将链表的头head指向新节点
        """
        node = Node(item)
        node.next = self.head
        self.head = node

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

    def remove(self, item):
        """
        删除指定元素的节点：
         1 2 3 4 5
        """
        pass

    def search(self, item):
        """
        判断查找的元素在节点中是否存在， 返回Bool类型
        """
        pass



if __name__ == '__main__':
    # 实例化单链表对象
    link = SingleLink()
    # 长度获取
    print("链表长度: ", len(link))
    # 遍历链表
    link.trvel()
    print("链表是否为空? ", link.is_empty())

    print("添加元素:")
    link.append(1)
    link.append(2)
    link.add(3)
    link.insert(1, 'hello')
    # 3 'hello' 1 2

    # 长度获取
    print("链表长度: ", len(link))
    # 遍历链表
    link.trvel()
    print("链表是否为空? ", link.is_empty())
