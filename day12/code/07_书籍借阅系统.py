"""
书籍借阅系统需求分析:
    1. 书籍的属性信息: 书名, 作者, 借阅状态(借出数量, 未借的数量)
    2. 书籍借阅需要的操作:
            1). 录入书籍信息;
            2). 借阅书籍信息
            3). 归还书籍
            4). 查询书籍信息
            5). 退出
"""

from colorFont import *
from prettytable import PrettyTable


class Book(object):
    def __init__(self, name, author, borrowed=0, borrow=0):
        """

        :param name: 书籍名称
        :param author: 作者
        :param borrowed: 已经借出的书籍数量
        :param borrow: 未借出的书籍数量
        """
        self.name = name
        self.author = author
        self.borrowed = borrowed
        self.borrow = borrow

    # 书籍信息的字符串显示
    def __str__(self):
        return '<Book: %s>' % (self.name)


class BookManage(object):
    books = []


    def __iter__(self):
        return  (book.name for book in self.books)

    def init(self):
        """初始化书籍信息的函数, 添加书籍信息"""
        self.books.append(Book("Python核心编程", 'Linus', 5, 0))
        self.books.append(Book("数据结构与算法", 'Guido', 0, 10))
        self.books.append(Book("Java核心编程", 'Linus', 5, 10))
        print(OKGREEN + "初始化书籍信息成功" + END)

    def find(self, name):
        """
        根据用户传入的书籍名称判断书籍是否存在, 如果存在, 返回该书籍对象; 如果不存在, 返回None
        :param name:
        :return:
        """
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def borrowBook(self):
        # 删除字符串左右的空格
        name = input("借阅书籍名称:").strip()
        # 查找书籍, 如果存在, 返回书籍对象, 不存在, 返回None;
        book = self.find(name)
        if book:
            if book.borrow > 0:
                # 未借出书籍数量减1;
                book.borrow -= 1
                print(OKGREEN + "书籍借阅成功" + END)
            else:
                print(WARNING + "书籍%s库存不足" % (book.name) + END)
        else:
            print(ERROR + "书籍%s不存在" % (name) + END)

    def returnBook(self):
        name = input("归还书籍名称:").strip()
        book = self.find(name)
        if book:
            book.borrow += 1
            print(OKGREEN + "书籍归还成功")

        else:
            print(ERROR + "书籍%s不存在" % (name))

    def show(self):
        print("书籍信息显示".center(50, '*'))
        table = PrettyTable()
        table.field_names = [ "编号", "书籍名称", "作者", '已借出数量', '库存数量']
        for index, book in enumerate(self.books):
            table.add_row([index+1,  book.name, book.author, book.borrowed, book.borrow])
        print(table)

def main():
    # 创建书籍管理的对象
    bm = BookManage()

    # 先初始化书籍信息
    bm.init()
    # for item in bm:
    #     print(item)


    prompt = """
                    书籍借阅管理系统
            
            1). 录入书籍信息;
            2). 借阅书籍信息
            3). 归还书籍
            4). 查询书籍信息
            5). 退出
    
    
    
    请输入你的选择:"""


    while True:
        choice = input(prompt)
        if choice == '1':
            pass
        elif choice == '2':
            bm.borrowBook()
        elif choice == '3':
            bm.returnBook()
        elif choice == '4':
            bm.show()
        elif choice == '5':
            exit(0)
        else:
            print("请输入正确的选项")

if __name__ == '__main__':
    main()
