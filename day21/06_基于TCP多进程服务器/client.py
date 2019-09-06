import socket

# 1. 创建服务端socket对象
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 2. 连接服务端
client.connect(('172.25.254.197', 9997))

while True:
    # 3.给服务端发送消息
    send_data = input('client: >> ').encode('utf-8')
    if not send_data:
        continue
    client.send(send_data)
    if send_data == 'quit':
        break

# 5. 关闭socket对象
client.close()
