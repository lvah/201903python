class Node(object):
    """二叉树节点对象的封装"""

    def __init__(self, element):
        self.element = element
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return '<Node:%d>' % (self.element)


class BinarySortTree(object):
    """二叉排序树的封装"""

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, item):
        """
        树里面插入元素
            1. 先判断树是否为空， 直接让根结点指向新的节点
            2. 如果不为空:
                从根结点开始访问， 判断一下item和节点的大小;
                    如果大于节点元素， 往右孩子节点添加；
                    如果小于节点元素， 往左孩子节点添加；
        """
        node = Node(item)
        if self.root is None:
            self.root = node
        bt = self.root
        while True:
            rootItem = bt.element
            # 如果添加的元素是否大于根结点元素：
            if item > rootItem:
                # 如果根结点的右子树为空， 直接添加节点到右子树即可；
                if bt.rchild is None:
                    bt.rchild = node
                # 如果根结点的右子树不为空， 将右子树节点作为新的根结点， 循环继续判断;；
                bt = bt.rchild
            elif item < rootItem:
                if bt.lchild is None:
                    bt.lchild = node
                bt = bt.lchild
            # 如果插入的元素和根结点相等， 不做操作;
            else:
                return

    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if not self.root:
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                node = queue.pop(0)
                print(node.element, end=',')
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)
            print()

    def search(self, root, key):
        """
        搜索指定元素是否在树里面
            key: 用户搜索的元素
        """
        if root is None:
            return False
        # 如果找到节点元素和用户搜索的值相等， 直接返回节点对象
        if root.element == key:
            return root
        # 如果找到节点元素大于用户搜索的值， 直接返回节点对象
        elif root.element > key:
            return self.search(root.lchild, key)
        else:
            return self.search(root.rchild, key)

    def searchDetail(self, root, parent, key):
        """
        搜索指定元素是否在树里面, 如果有， 则
        返回3个值:
            1. Bool: 是否找到该元素;
            2. node: 找到元素对应的节点
            3. parent: 找到的元素对应的父节点;
        """
        if root is None:
            return False, root, parent
        # 如果找到节点元素和用户搜索的值相等， 直接返回节点对象
        if root.element == key:
            return True, root, parent
        # 如果找到节点元素大于用户搜索的值， 直接返回节点对象
        elif root.element > key:
            return self.searchDetail(root.lchild, root, key)
        else:
            return self.searchDetail(root.rchild, root, key)

    def delete(self, key):
        """
        删除二叉排序树的节点元素:
            1). 如果要删除的节点是叶子，直接删；
            2). 如果只有左子树或只有右子树，则删除节点后，将子树链接到父节点即可；
        :param key:
        :return:
        """
        # 1. 查找删除元素对应的节点, isExists是否找到该节点元素， node是找到的节点对象， parent：元素节点的父节点
        isExists, node, parent = self.searchDetail(self.root, None, key)

        if not isExists:
            print("要删除的元素%d不存在" % (key))
            return

        # 如果深处的是根节点， 不处理
        if node == self.root:
            print("不能删除根结点")
            return
        # 1). 如果要删除的节点是叶子，直接删；
        if node.lchild is None and node.rchild is None:
            # 判断删除的节点是父节点左孩子还是右孩子
            if parent.lchild == node:
                parent.lchild = None
            else:
                parent.rchild = None

        # 2). 如果只有左子树或只有右子树，则删除节点后，将子树链接到父节点即可；
        # 如果只有左子树
        if node.lchild is not None and node.rchild is None:
            # 如果node是parent的左子树：
            if parent.lchild == node:
                parent.lchild = node.lchild
            else:
                parent.rchild = node.lchild

        # 如果只有右子树
        if node.rchild is not None and node.lchild is None:
            # 如果node是parent的左子树：
            if parent.lchild == node:
                parent.lchild = node.rchild
            else:
                parent.rchild = node.rchild

        # 如果有左右子树
        # 方法一: 令结点 node 的左子树为其双亲结点的左子树；结点 node的右子树为其自身直接前驱结点的右子树
        if node.lchild is not None and node.rchild is not None:
            # 如何找到node的直接前驱节点, 找到后， 将直接前驱节点的右子树指向node的右子树;
            # 当前节点左子树的最右节点
            # 分类讨论， 删除的是父节点的左孩子还是右孩子
            if parent.lchild == node:
                parent.lchild = node.lchild
            else:
                parent.rchild = node.lchild

            prevNode = node.lchild
            while prevNode.rchild:
                prevNode = prevNode.rchild
            # prev指的是node节点的直接前驱(中徐遍历时，node节点前面的节点)
            prevNode.rchild = node.rchild

if __name__ == '__main__':
    # sortedTree = BinarySortTree()
    # nums = [3, 5, 7, 2, 1]
    # for num in nums:
    #     sortedTree.add(num)
    #
    # sortedTree.breadth_travel()
    #
    # print("搜索:")
    # print(sortedTree.search(sortedTree.root, 2))
    #
    # print("详细搜索:")
    # isExist, node, parentNode = sortedTree.searchDetail(sortedTree.root, None, 2)
    # print("找到的节点:", node)
    # print("搜索节点的父节点:", parentNode)
    #
    # print("删除节点")
    # sortedTree.delete(3)
    # sortedTree.breadth_travel()

    sortedTree = BinarySortTree()
    nums = [45, 12, 53, 3, 37, 100, 24, 52, 61, 90, 78]
    for num in nums:
        sortedTree.add(num)
    sortedTree.breadth_travel()
    # 删除右左右子树的节点;
    sortedTree.delete(53)
    sortedTree.breadth_travel()
