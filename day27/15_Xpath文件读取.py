
from lxml import  etree
filename = 'doc/hello.html'
import os
print(os.path.exists(filename))
#利用etree.HTML,将字符串解析为HTML文档
html = etree.parse(filename)
# # 按字符串序列化HTML文档
result = etree.tostring(html)
print(result)