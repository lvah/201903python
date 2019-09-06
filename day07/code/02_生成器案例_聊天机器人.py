def chat_robot():
    """
    聊天机器人
    :return:
    """
    # 这个变量存储的是机器人给用户的响应信息;
    response = ''
    # 死循环
    while True:
        # receive: 接收用户给机器人传过来的消息
        # response: 机器人给用户的响应信息;
        receive = yield response
        if '年龄' in receive:
            response = "年龄保密"
        elif '姓名' in receive:
            response = "我是聊天机器人Siri"
        elif receive.endswith('吗?'):
            response = receive.rstrip('吗?')
        else:
            response = '我听的不是很懂， 请换种说法'



# Robot是生成器(函数中包含yield关键字)
Robot = chat_robot()
# 调用next方法, 遇到yield停止
next(Robot)
# 用户可以一直给机器人发消息， 使用死循环
while True:
    send_data = input("[用户粉条]>>: ")
    if send_data == 'q' or send_data== 'quit':
        print("机器人累了， 需要休息......下次再聊")
        break
    response = Robot.send(send_data)
    print('[机器人]>>: ', response)