import requests
import json
import itchat


def get_tuling_response(info):
    """
    根据用户提供的信息， 智能返回响应信息;
    :param info:
    :return:
    """
    # 图灵机器人官方提供的API地址;
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    # 要提交给图灵官网的信息;
    data = {
        "reqType": 0,  # 文字
        "perception": {
            "inputText": {
                "text": info
            },
        },
        "userInfo": {
            "apiKey": "ed2c06560d9b4672968c97735ce078cd",
            "userId": "hello"
        }
    }

    json_data = json.dumps(data)

    # 将信息提交给指定网址， 获得权限， 返回需要的内容;
    response = requests.post(api_url, json_data).text

    # response是一个json格式的信息， 提取需要的内容
    response_dict = json.loads(response)
    # 图灵机器人响应的文字信息
    tuling_say = response_dict.get("results")[0].get("values").get('text')
    return tuling_say

import itchat
# 时刻监控好友发送的文本信息， 并给予一个回复;
# isFriendChat=True: 是否监控微信好友发送的文本信息。
# isGroupChat=False： 是否监控群聊发送的文本信息。
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    """
    修改版： 只对指定的用户自动回复
    :param msg:
    :return:
    """
    fromUserName = msg.get('FromUserName')
    # 1). 根据好友的备注名称进行搜索, 获取该好友的详细信息;返回的是列表, 列表里面嵌套字典;
    result = itchat.search_friends(remarkName="陈辉")

    # 2). 要给固定好友发送消息， 就是要获取改好友的UserName
    username = result[0].get('UserName')
    if fromUserName == username:
        # print(msg)
        # with open('itchat.txt', 'w') as f:
        #     keys = msg.keys()
        #     for key in keys:
        #         f.write(key + '\n')

        send_text = msg.text  # 获取用户给你发送的信息
        tuling_text = get_tuling_response(send_text)
        print("接收的信息:", send_text)
        print("回复的信息:", tuling_text)

        return '[图灵机器人]: ' + tuling_text

itchat.auto_login(hotReload=True)
itchat.run()
