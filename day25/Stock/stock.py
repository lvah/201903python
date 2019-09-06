"""
股票数据的定向爬虫
"""

import requests


def get_html(url):
    """获取指定url的源代码"""
    # 客户端向服务端发起请求(request)
    # 服务端向客户端返回一个响应(response)
    try:
        # 反爬虫的第一步： 模拟浏览器
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
        }
        response = requests.get(url, headers=headers)

    except Exception as e:
        print(e)
    else:
        return response.text


if __name__ == '__main__':
    # url = 'http://stockpage.10jqka.com.cn/HK1810/'
    # url = 'http://quote.eastmoney.com/hk/01810.html'
    url = 'http://www.cbrc.gov.cn/chinese/jrjg/index.html'
    content = get_html(url)
    print(content)
