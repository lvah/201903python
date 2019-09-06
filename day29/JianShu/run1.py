"""

"""

from fake_useragent import  UserAgent
import requests

url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
url = 'https://www.douban.com/'
ua = UserAgent()
headers = {
    'User-Agent':ua.random
}
data = {
    'ck':'',
    'username':'18829266581',
    'password':'gf132590',
    'remember':'false',
    'ticket':''
}
s = requests.session()
s.post(url=url_basic, headers=headers, data=data)
response = s.get(url=url, headers=headers)
with open('douban.html' , 'wb') as f:
    f.write(response.content)