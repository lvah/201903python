import telnetlib

import requests
from requests.exceptions import ConnectionError
# colorama是一个python专门用来在控制台、命令行输出彩色文字的模块，可以跨平台使用。
from colorama import Fore, Back, Style

"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0'
}
def get_page(url, options=None):
    """
    获取的网页源代码: 抓取代理
    :param url:
    :param options:
    :return:
    """
    if not options:
        options = {}
    headers = dict(base_headers, **options)
    print(Fore.GREEN + '[+] 正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        print(Fore.GREEN + '[+] 抓取成功', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print(Fore.RED + '[-] 抓取失败', url)
        return None





def test_proxy_vaild(proxy):
    """
    测试代理IP是否可用
    :param proxy: ip:port
    :return:
    """
    ip, port = proxy.split(":")
    try:
        tn = telnetlib.Telnet(ip, int(port))
    except Exception as e:
        # print(e)
        return False
    else:
        return True

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    get_page(url)
