# 获取网页内容的模块
import requests
import  json
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
            "userId": "lvah"
        }
    }

    json_data = json.dumps(data)

    # 将信息提交给指定网址， 获得权限， 返回需要的内容;
    response = requests.post(api_url, json_data).text

    # response是一个json格式的信息， 提取需要的内容
    response_dict = json.loads(response)
    # 图灵机器人响应的文字信息
    tuling_say = response_dict.get("results")[0].get( "values").get('text')
    return  tuling_say


    # 获取百度页面的内容
    # content = requests.get('http://www.baidu.com').text
    # print(content)

result = get_tuling_response("Python编程语言简单吗?")
print(result)

result1 = get_tuling_response("讲个笑话吧")
print(result1)
