import requests


def get_content(url):
    """获取指定网页的页面信息"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '}
    try:
        # 如果响应的状态码为404并不会抛出一场， 那么如何让处理?
        response = requests.get(url,  headers=headers)
        response.raise_for_status()   # 如果返回的状态码不是200， 那么抛出异常
        response.encoding = response.apparent_encoding   # 自动判断网也的编码格式， 便于response.text知道如何实现解码
    except Exception as e:
        print('[-] 爬取失败:', e)
    else:
        # print('[+]' + response.url, "爬取成功....")
        # print(len(response.text))
        return  response.text



def parser_content(html):
    """解析页面内容: 获取博客名称和博客链接"""
    # 1. 实例化soup对象
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    # 2. 分析页面， 获取内容;
    # 获取所有的博客内容, 用列表保存
    print(soup.title.text)
    article_lists =  soup.body.find('ul', class_='colu_author_c').find_all('li')
    # print(article_lists)
    # print(soup.body.prettify())
    # print(soup.body.div)
    f = open('csdn.md', 'w')
    for article in article_lists:
        # 获取标题
        blogName = article.h4.a.text
        # 获取链接
        blogUrl = article.h4.a.get('href')
        f.write('- [%s](%s)\n' %(blogName, blogUrl))
    f.close()




if __name__ == '__main__':
    url = 'https://blog.csdn.net/cainiaoayue/article/list/'
    content = get_content(url)
    parser_content(content)