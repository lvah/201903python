import requests


def searchBaidu():
    keyword = input("请输入搜索的关键字: ")
    baiduUrl = 'https://www.baidu.com/s'
    params = {
        'wd': keyword
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '}
    try:
        # 如果响应的状态码为404并不会抛出一场， 那么如何让处理?
        response = requests.get(baiduUrl, params=params, headers=headers)
        response.raise_for_status()   # 如果返回的状态码不是200， 那么抛出异常
        response.encoding = response.apparent_encoding   # 自动判断网也的编码格式， 便于response.text知道如何实现解码
    except Exception as e:
        print('[-] 爬取失败:', e)
    else:
        print('[+]' + response.url, "爬取成功....")
        print(len(response.text))
        # print(response.text)
if __name__ == '__main__':
    searchBaidu()