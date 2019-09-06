import socket

udpserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpserver.bind(('0.0.0.0', 9999))
print('QQ用户A上线.........')
while True:
    # 返回的是元组， 一个个元素是客户端发送的信息， 第二个元素是客户端和服务端交互的地址(IP, port)
    recv_data, address = udpserver.recvfrom(1024)
    # print(address)
    print("B:>> ", recv_data.decode('utf-8'))
    if recv_data == b'quit':
        print("聊天结束.......")
        break
    # 发送的消息必须是bytes类型
    #   bytes -->  str    bytesObj.decode('utf-8')
    #    str   --> bytes   strObj.encode('utf-8')
    send_data = input('A: >> ').encode('utf-8')
    if not send_data:
        continue
    udpserver.sendto(send_data, address)

udpserver.close()
