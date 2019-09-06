
filename = 'doc/passwd'
# 1). 以读写的方式打开文件;默认文件指针指向末尾;
f = open(filename, 'a+')

# 2). *******************************文件操作*************************************************
# 2-1). 移动指针位置:
"""
seek(offset, from)有2个参数:
    offset:偏移量
    from:方向   0:表示文件开头; 1:表示当前位置; 2:表示文件末尾
"""
f.seek(0, 0)

# 2-2). 读操作
"""
# 8G日志文件  ------->  电脑内存4G
读取小文件(<1G)def read(self, n: int = -1) -> AnyStr:    默认读取到文件末尾， 返回的是一个字符串;
"""
# content = f.read()
# print(content)


"""
读取大文件:  readline;每次读取一行

"""
# print('******')
# # 死循环
# while True:
#     # 每次只读取一行内容， 如果不能读取到内容， break跳出;
#     content = f.readline()
#     if not content:
#         break
#     else:
#         print(content, end='')


"""
读取大文件:  readlines;每次读取多行
"""
content = f.readlines()
print(content)



# 2-3). 写操作
f.write("写入文件内容")
f.writelines(['第一个\n', '第二个\n'])


# 2-4). 定位
print(f.tell())
f.seek(0, 0)
print(f.tell())
# f.seek(-3, 2)
# print(f.tell())
# 3). 关闭文件对象
f.close()