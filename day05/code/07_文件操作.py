"""


   ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first(1).文件不存在则创建文件； 2）.文件存在， 清空文件内容)
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists(1).文件不存在则创建文件； 2）.文件存在， 不会清空文件内容)
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================


        是否有读权限?    是否有写权限?     文件不存在，是否会创建文件?        文件操作会清空文件内容么?
r           yes         no                  no                              no
w           no          yes                 yes                             yes
a           no          yes                 yes                             no
w+          yes         yes                 yes                             yes
a+          yes         yes                 yes                             no
r+          yes         yes                 no                              no


rb, wb, ab, wb+, ab+, rb+
"""
# 1). 打开文件doc/passwd(相对路径), /home/kiosk/201905python/day05/doc/passwd(绝对路径)
#  默认打开是r权限
f = open('doc/passwd', 'a+')
# 2). 对文件做操作
print(f.mode)
print(f.read())
f.seek(0, 0)
print(f.read())
f.write('hello')  # io.UnsupportedOperation: not writable
# 3). 关闭文件对象
f.close()