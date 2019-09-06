import socket



# 1. 创建socket对象
#       family: AF_INET(IPv4)   AF_INET6(IPv6)      ========= 网络层协议
#       type: # SOCK_STREAM(TCP)   SOCK_DGRAM(UDP) ========== 传输层协议
#       Linux： 可以认为是一个文件；
socketObj = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print(socketObj.getsockname())

#2.  关闭socket对象
socketObj.close()

# 2. socket基本使用
import os
os.system('hostname')

hostname = socket.gethostname()
print("主机名:", hostname)

print(socket.gethostbyname('localhost'))


