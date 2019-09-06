"""
with语句工作原理:
        python中的with语句使用于对资源进行访问的场合，
        保证不管处理过程中是否发生错误或者异常都会自动
        执行规定的(“清理”)操作，释放被访问的资源，
        比如有文件读写后自动关闭、线程中锁的自动获取和释放等。
"""

with open('doc/passwd') as f:
    print("with语句里面：", f.closed)
    print(f.read(10))
print("with语句外面：", f.closed)