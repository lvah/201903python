"""
python3:
    urllib
    urllib.request

python2:
    urllib
    urllib2

"""


from urllib import  request
from urllib import error
from urllib import parse

try:
    url = 'http://www.baidu.com:80'
    obj = parse.urlparse(url)
    # print(obj)
    response = request.urlopen(url)
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
    # print(str_content)
