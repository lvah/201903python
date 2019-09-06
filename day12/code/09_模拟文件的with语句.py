class myopen(object):
    """为了模拟文件中with语句的实现机制"""
    def __init__(self, filename, mode='r'):
        self.name = filename
        self.mode = mode

    def __enter__(self):
        """当with语句开始值性时, 做的操作"""
        # 返回的时文件对象
        print('文件打开')
        self.f = open(self.name, self.mode)
        return  self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print("文件关闭")

with myopen('test1.txt', 'r') as f:
    print(f.read())



