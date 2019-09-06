"""
# 0. 概括
    - 获取页面: urllib, requests
    - 解析页面信息: 正则表达式, BeautifulSoup4(BS4)
# 1. BS4简介
    Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个
    工具箱，通过解析文档为tiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
    你不需要考虑编码方式，除非文档没有指定一个编一下原始编码方式就可以了。
# 2. BS4的4种对象
        Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,
        每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .
        ## 2-1. BeautifulSoup对象
        ## 2-2. Tag对象
            Tag就是html中的一个标签，用BeautifulSoup就能解析出来Tag的具体内容，
            具体的格式为soup.name,其中name是html下的标签。


"""
from bs4 import BeautifulSoup

html = """
<html>
<head><title>story12345</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister1" id="link2">python</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Java</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 1. 实例化BeautifulSoup对象
# https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id7
soup = BeautifulSoup(html, 'lxml')  # 使用lxml解析器进行解析，速度快。
# print(soup)
# print(soup.prettify())    # 按照指定的缩进格式补齐并显示html;
# 2. 根据标签名称获取信息
# print(soup.title)
# print("网页的标题: ", soup.title.text)  # 获取指定标签里面的文本信息
# print(soup.title.name)

#
# # 获取的标签包含多个时， 默认返回第一个;
# print(soup.a)
# # 获取指定标签的属性(3种)
# print(soup.a['href'])
# print(soup.a['class'])
# print(soup.a['id'])
# print(soup.a.get('id'))
# # attrs获取a标签的所有属性
# print(soup.a.attrs['href'])



# # 3. 修改标签里面的属性信息
# print(soup.a['href'])
# soup.a['href'] = 'http://www.baidu.com'
# print(soup.a)



# 4. 找到符合条件的所有标签
# tagObj = soup.find_all('a')
# print(tagObj)
# print(len(tagObj))


tagObj = soup.find_all('a', class_='sister')
print(tagObj)
print(len(tagObj))


tagObj = soup.find_all('a', id='link1')
print(tagObj)
print(len(tagObj))