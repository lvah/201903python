import socket

udpclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("QQ用户B上线.........")
while True:
    send_data = input('B:>> ').encode('utf-8')
    if not send_data:
        continue
    udpclient.sendto(send_data, ('172.25.254.197', 9999))
    if send_data == b'quit':
        print("聊天结束.....")
        break
    recv_data, address = udpclient.recvfrom(1024)
    print("A:>> ", recv_data.decode('utf-8'))

udpclient.close()
