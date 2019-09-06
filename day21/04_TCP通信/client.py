
import socket

# 1. 创建服务端socket对象
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


# 2. 连接服务端
client.connect(('172.25.254.197', 9998))


# 3.给服务端发送消息
client.send(b'hello server')



# 4. 接收服务端发送的消息
recv_data = client.recv(1024).decode('utf-8')
print("接收服务端发送的消息:", recv_data)


# 5. 关闭socket对象
client.close()