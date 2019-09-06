import socket


def handler(clientSocketObj):
	# 5. 接收客户端传递的消息
	recv_data = clientSocketObj.recv(1024)
	print("*"*10)
	print(recv_data)
	# 6. 恢复消息
	clientSocketObj.send(b'HTTP/1.1 200 OK\r\n\r\n')
	clientSocketObj.send(b'<h1 style="color:green">index</h1>')



def webServer():
	# 1. 创建socket对象
	server = socket.socket()
	# 2.  绑定IP和端口
	server.bind(('0.0.0.0', 8082))
	# 3. 监听
	server.listen(5)
	print("自定义的HTTP服务8082开启.........")


	while True:
		# 4. 接收客户端连接
		clientSocketObj, clientAddress = server.accept()
		import threading
		t = threading.Thread(target=handler, args=(clientSocketObj, ))
		t.start()

	



if __name__ == '__main__':
	webServer()

