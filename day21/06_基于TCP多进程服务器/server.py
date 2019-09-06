# 实现多进程的方式:
#       1. 实例化对象
#       2. 继承子类
#       注意: 一定要确定多进程要处理的任务


# 任务: 处理客户端请求并为其服务
def dealWithClient(clientSocketObj, clientAddress):
    while True:
        # 5. 接收客户端发送的消息
        recv_data = clientSocketObj.recv(1024).decode('utf-8')
        print(clientAddress[0] + str(clientAddress[1]) + ':> ' + recv_data)
        if recv_data == 'quit':
            break
    clientSocketObj.close()


import socket
from multiprocessing import Process

# 1. 创建服务端socket对象
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2. 绑定地址和端口(IP:port)
server.bind(('0.0.0.0', 9997))

# 3. 监听是否有客户端连接?listen
server.listen(5)
print('server start .........')

while True:
    # 4.接收客户端的连接accept
    clientSocketObj, clientAddress = server.accept()
    # dealWithClient(clientSocketObj)
    p = Process(target=dealWithClient, args=(clientSocketObj, clientAddress))
    p.start()

# server.close()
