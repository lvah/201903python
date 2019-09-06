import requests
from fake_useragent import  UserAgent



def get_page(url, options=None):
    """
    获取的网页源代码: 抓取代理
    :param url:
    :param options:
    :return:
    """

    print('[+] 正在抓取', url)
    try:
        headers = {
            'User-Agent':ua.random
        }
        response = requests.get(url, headers=headers)
        print('[+] 抓取成功', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('[-] 抓取失败', url)
        return None

if __name__ == '__main__':
    ua = UserAgent()
    url = 'https://www.jianshu.com/c/22f2ca261b85?order_by=commented_at&page=2'
    html = get_page(url)
    print(html)


