"""
浏览器的模拟
    应用场景：有些网页为了防止别人恶意采集其信息所以进行了一些反爬虫的设置，而我们又想进行爬取。
    解决方法：设置一些Headers信息（User-Agent），模拟成浏览器去访问这些网站。
"""

from urllib import request
from urllib import error
from urllib import parse
try:
    url = 'http://www.baidu.com:80'
    obj = parse.urlparse(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '}

    # 实例化请求对象， 修改请求的头部信息;
    requestObj = request.Request(url, headers=headers)
    # urlopen方法可以打开一个url地址， 也可以打开一个请求对象(一般为了修改请求头部)
    response = request.urlopen(requestObj)
    print("访问的网站是: ", obj.netloc)
except error.HTTPError as e:
    print(e.code, e.reason, e.headers)
except error.URLError as e:
    print(e.reason)
else:
    bytes_content = response.read()
    print(type(bytes_content))
    str_content = bytes_content.decode('utf-8')
    print(type(str_content))
    # 请求对象拥有的方法:
    # 相应对象拥有的方法:
    # print(dir(requestObj))
    # print(dir(response))
    print("请求头部信息:", requestObj.headers)
    print("响应头部信息: ", response.headers)
    print("响应的状态码: ", response.code)
