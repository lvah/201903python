"""
代理服务器的设置
    应用场景：使用同一个IP去爬取同一个网站上的网页，久了之后会被该网站服务器屏蔽。
    解决方法：使用代理服务器。 （使用代理服务器去爬取某个网站的内容的时候，在对方的网站上，显示的不是我们真实的IP地址，而是代理服务器的IP地址）


如何获取免费代理?
    pass
"""

import requests
import random

proxies = [
    {'http': '123.139.56.238:9999'},
    {'http': '158.140.182.175:8080'},
    # {'http': '182.35.85.146:9999'},
    # {'http': '112.85.164.9:9999'},
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '}
# url = 'http://www.baidu.com'
url = 'http://httpbin.org/get'
proxy = random.choice(proxies)
print(proxy)
response = requests.get(url, headers=headers, proxies=random.choice(proxies))
print(response.text)
print(response.headers)