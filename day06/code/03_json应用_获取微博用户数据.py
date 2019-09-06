"""
任选一个取写:
    1. 获取指定的用户 微博发布的内容;
    2. 获取西安未来5天的天气.-----(找API)
"""


# 导入爬取网页内容的模块
import  requests
import  json


def get_weibo_user_info(id):  # ‘’
    # 1). 通过微博网址的分析(1. 设置为手机端，才有API； 2. Network (All, IMG ***XHR**), F5)
    url = "https://m.weibo.cn/api/container/getIndex?is_hot[]=1&is_hot[]=1&jumpfrom=weibocom&type=uid&value=%s" %(id)
    # 2). 获取指定网址的内容， text方法返回的是字符串类型;
    content = requests.get(url).text
    if not content:
        print("Error: 页面爬取错误")
        return  None
    # 3). 将json】格式的字符串转换成python的数据类型(字典)
    python_content_dict = json.loads(content)

    # 4). 获取用户的信息
    # 用户信息的内容(是一个字典)
    userinfo = python_content_dict.get('data').get('userInfo')
    if userinfo:

        name = userinfo['screen_name']
        desc = userinfo['description']
        gender = "女" if userinfo['gender'] == 'f' else "男"
        followers = userinfo['followers_count']
        follow = userinfo['follow_count']

        # 将用户信息持久化保存到文件中;
        with open('doc/user.txt', 'a+') as f:
            f.write('%s:%s:%s:%s:%s\n' %(name, desc, gender, followers, follow))

        # 3). 用户信息显示
        print("""
        微博用户 %s
        用户描述: %s        
        用户性别: %s
        关注者数量： %s
        被关注者的数量: %s
        """ %(name, desc, gender, followers, follow))
    else:
        print('Error: 该用户%s不存在' %(id))


def main():
    # ids = ['5652937891', '5305630013', '001', '233jjjjj']

    ids = []
    for i in range(10):
        id = '56529378' + str(i+1)
        ids.append(id)
    for id in ids:
        get_weibo_user_info(id)   # 调用函数, id



main()