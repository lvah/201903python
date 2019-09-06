class Stack(object):
    """
    根据列表的数据结构封装栈的数据结构
    """
    # 构造方法
    def __init__(self):
        # 定义一个空栈， 用来存储栈的元素
        self.__stack = []

    # len(stackobj)自动会调用该方法
    def __len__(self):
        return  len(self.__stack)
    def push(self, item):
        """入栈"""
        self.__stack.append(item)
        print("元素[%s]入栈成功" % (item))

    def pop(self):
        """出栈, 判断栈是否为空"""
        if not self.is_empty():
            # 获取出栈的元素
            item = self.__stack.pop()
            print("元素[%s]出栈成功" % (item))
        else:
            raise Exception("栈为空")

    def top(self):
        """获取栈顶元素"""
        if not self.is_empty():
            # 获取出栈的元素
            item = self.__stack[-1]
            print("栈顶元素为: [%s] " % (item))
        else:
            raise Exception("栈为空")

    def length(self):
        """获取栈的元素个数"""
        return len(self.__stack)

    def is_empty(self):
        """判断栈是否为空"""
        return len(self.__stack) == 0


stack = Stack()
stack.push(5)
print(len(stack))
stack.push(3)
stack.pop()
stack.is_empty()
stack.pop()
stack.is_empty()
print(len(stack))

