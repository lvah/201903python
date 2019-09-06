class Node(object):
    """
    二叉树节点对象封装的类
    """

    def __init__(self, element):
        self.element = element
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return self.element


    def __repr__(self):
        return  self.element


class Tree(object):
    """二叉树的封装"""

    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        """往二叉树里面添加元素"""
        node = Node(item)
        #  #如果树是空的,则对根节点赋值
        if not self.root:
            self.root = node
        else:
            # 先找树的根节点, 存储到变量queue中
            queue = []
            queue.append(self.root)
            while queue:
                item = queue.pop(0)
                if not item.lchild:
                    item.lchild = node
                    return
                elif not item.rchild:
                    item.rchild = node
                    return
                else:
                    queue.append(item.lchild)
                    queue.append(item.rchild)

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


    def preorder(self, root):
        """先序遍历: 根左右"""
        if root == None:
            return
        print(root.element, end=', ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.element, end=', ')
        self.inorder(root.rchild)

    def lastorder(self, root):
        """递归实现后序遍历"""
        if root == None:
            return
        self.lastorder(root.lchild)
        self.lastorder(root.rchild)
        print(root.element, end=', ')


    def depth(self, root):
        """求二叉树的深度"""
        if root == None:
            return  0
        lcount = self.depth(root.lchild) + 1  # 树左侧的深度
        rcount = self.depth(root.rchild) + 1
        return  lcount if lcount > rcount else rcount


    def mirror(self, root):
        """对于二叉树进行一个镜像：左右子树交换"""
        if root == None:
            return  None
        self.mirror(root.lchild)
        self.mirror(root.rchild)
        root.lchild, root.rchild = root.rchild, root.lchild

if __name__ == '__main__':
    tree = Tree()
    for item in range(10):
        tree.add(item + 1)
    print("创建树成功")

    #
    # print("层次遍历".center(30, '*'))
    # tree.breadth_travel()


    print("先序遍历")
    root = tree.root
    tree.preorder(root)


    print("\n后序遍历")
    root = tree.root
    tree.lastorder(root)



    print("进行树的镜像".center(50, '*'))
    tree.mirror(root)
    print("层次遍历".center(30, '*'))
    tree.breadth_travel()




