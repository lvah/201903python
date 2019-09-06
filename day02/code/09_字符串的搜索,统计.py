"""
>>> # 字符串的搜索,统计
...
>>>
>>> s = 'hello python hello java'
>>> help(s.find)

>>> s.find('hello')
0
>>> s.find('llo')
2
>>> help(s.find)

>>> s.find('llo', 6)
15
>>> s.find('llokk')
-1
>>> s.index('hello')
0
>>> s.index('helfcr')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> s.count('hello')
2
>>>
KeyboardInterrupt

"""