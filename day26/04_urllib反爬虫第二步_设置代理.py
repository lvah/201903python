"""
代理服务器的设置
    应用场景：使用同一个IP去爬取同一个网站上的网页，久了之后会被该网站服务器屏蔽。
    解决方法：使用代理服务器。 （使用代理服务器去爬取某个网站的内容的时候，在对方的网站上，显示的不是我们真实的IP地址，而是代理服务器的IP地址）


如何获取免费代理?
    pass
"""

from urllib.request import ProxyHandler, build_opener, urlopen, install_opener
import random

proxyes = [
    {'HTTPS': '163.204.247.157:9999'},
    {'HTTP': '163.204.246.39:9999'},
    {'HTTP': '163.204.243.135:9999'},
]
# url = 'http://www.baidu.com'
url = 'http://httpbin.org/get'
# 1. 调用类名创建IP代理的处理器
proxy_support = ProxyHandler(random.choice(proxyes))

# 2. build_opener === urlopen
opener = build_opener(proxy_support)
install_opener(opener)
# 3.打开url地址， 访问
response = opener.open(url)
print('>>>>>>')
content = response.read()
print(len(content))
print(content)
