# GET
import requests

# url = 'http://www.baidu.com'
# response = requests.get(url)
# print(response.text)  # 文本
# print(response.content)# 二进制
# # print(response.json())  # 返回的是json字符串， 转成python可以识别的字典;


# # POST
# url = 'http://httpbin.org/post'  # 专门用来测试post方法的网站
# response = requests.post(url, data={'name':'westos', 'age':10})
# print(response.text)


# # PUT
# url = 'http://httpbin.org/put'  # 专门用来测试post方法的网站
# response = requests.put(url, data={'name':'westos', 'age':10})
# response = requests.put(url, data={'name':'zhihu'})
# print(response.text)


# # DELETE
# url = 'http://httpbin.org/delete'
#
# response = requests.delete(url, data={'name':'westos', 'age':10})
# print(response.text)

# url解析
# url = 'https://movie.douban.com/subject/26794435/photos?type=R&start=90&sortby=like&size=a&subtype=a'
url = 'https://movie.douban.com/subject/26794435/photos'
params = {
    'type': 'R',
    'start': 90,
    'sortby': 'like',
    'subtype': 'a'
}

response = requests.get(url, params=params)
with open('douban.html', 'wb') as f:
    f.write(response.content)
