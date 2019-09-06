"""

>>> # 录入数据
...
>>> username = input('Username:')
Username:root
>>> username == 'root'
False
>>> 'root      '.rstrip()
'root'
>>> username = input('Username:').rstrip()
Username:root
>>> username == 'root'
True
>>> '\n\thello\n\t'.strip()
'hello'
>>> s = 'hello world jdjdfjsf jfjf'
>>> s.replace(' ', '')
'helloworldjdjdfjsfjfjf'
>>> s.replace('he', 'westos')
'westosllo world jdjdfjsf jfjf'


"""