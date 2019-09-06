# 实现http客户端的程序， 获取百度的页面信息;
import socket


#1. 创建socket对象,  HTTP(应用层协议): TCP(传输曾协议)， 默认情况下IPv4和TCP；
client = socket.socket()


# 2. 连接服务端
# http://www.baidu.com  80
# https://www.baidu.com 443
client.connect(('www.qq.com', 80))

# 3. 给服务器发送消息, 消息内容: 获取百度主页页面
client.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')

# 4. 接收服务端返回的内容
recv_data = client.recv(1024*10)



# 5. 检测是否为百度页面
with open('baidu.html', 'wb') as f:
	f.write(recv_data)


# 6. 关闭socket对象
client.close()

