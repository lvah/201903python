import os
from os.path import isabs, abspath, join

# 1. 判断是否为绝对路径---'/tmp/hello', 'hello.png', 'qq/hello.mp3'
print(isabs('/tmp/hello'))
print(isabs('hello.py'))

# 2. 生成绝对路径
# filename = 'hello.py'
filename = '/tmp/hello.py'
if not isabs(filename):
    print(abspath(filename))

# 3. 'hello.png'
# 返回一个绝对路径： 当前目录的绝对路径+ 文件名/目录名

# '/tmp/hello' , 'python.txt'   ==== /tmp/hello/python.txt
# C:\tmp\hello\python.txt
print(join('/tmp/hello', 'python.txt'))

# 4.获取目录名或者文件名




# 5. 创建目录/删除目录


# 6. 创建文件/删除文件


# 7. 文件重命名(mv)


# 8. 判断文件或者目录是否存在


# 9. 分离后缀名和文件名

# 10. 将目录名和文件名分离
