"""
西刺代理IP定向爬虫
    需求分析: 获取代理的IP和端口
"""
import re

import requests
# User-Agent随机选择代理模块;
from fake_useragent import  UserAgent
# 线程池
from concurrent.futures import  ThreadPoolExecutor


def get_content(url):
    """数据采集"""
    try:
        headers = {
            'User-Agent': ua.random,

        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
    except Exception as e:
        print("网页" + url + "爬取错误:", e)
        return  ''
    else:
        # response.text     : 如果普通的页面， 用text， 返回字符串的内容
        # response.content  : 如果不是普通的页面(图片， 视频), 用content, 返回的时二进制内容;
        return  response.text

def html_parser(html):
    """数据解析: IP：PORT"""
    """
    <tr class="odd">
      <td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn"></td>
      <td>113.89.53.247</td>
      <td>9999</td>
    </tr>
    """
    # 1. 获取每一行代理IP的详细内容;
    # re.S: 表示“.”（不包含外侧双引号，下同）的作用扩展到整个字符串，包括“\n”。
    # .代表除了\n之外的任意单个字符;
    tr_pattern = re.compile(r'<tr class=.*?>(.*?)</tr>', re.S)
    trs = tr_pattern.findall(html)
    # 2. 获取这一行IP代理的ip和port;
    """
     <td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn"></td>
      <td>113.89.53.247</td>
      <td>9999</td>
    """
    IPpattern = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  # \.代表时真实的点字符串， 进行转义， 否则代表任意单个字符;
    PortPattern = re.compile(r'<td>(\d+)</td>')
    for tr in trs:
        ip = IPpattern.findall(tr)[0]
        port = PortPattern.findall(tr)[0]
        yield  ip, port



def task(page):
    """
    多线程执行的任务: 数据采集和数据分析， 返回ip和port
    :return:
    """
    print("正在爬取第%d页" %(page))
    url = 'https://www.xicidaili.com/nt/%s' % (page)
    html = get_content(url)
    results = html_parser(html)
    return  results



if __name__ == '__main__':
    pages = 5
    threadCount = 10
    filename = 'xici.csv'
    # 创建用户代理的对象， 通过random属性随机获取一个User-Agent, 用于反爬虫处理;
    ua = UserAgent()

    with ThreadPoolExecutor(threadCount) as pool:
        taskResults = pool.map(task, range(1, pages+1))

    fw = open(filename, 'w')
    count = 0
    for taskResult in taskResults:
        for item in taskResult:
            count += 1
            fw.write(",".join(item) + '\n')
            # item: ('121.13.252.61', '41564')
            # print(item)
    print(count)
    fw.close()