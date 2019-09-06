"""

>>> s='hello'
>>> s.lower()
'hello'
>>> s.upper()
'HELLO'
>>> s.title()
'Hello'
>>> s = 'Hello WoRld'
>>> s.swapcase()
'hELLO wOrLD'
>>> s.capitalize()
'Hello world'
>>> s.title()
'Hello World'
>>> S
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'S' is not defined
>>> s
'Hello WoRld'
>>> s.isalnum()
False
>>> s = 'hello'
>>> s.isalnum()
True
>>> s.istitle()
False
>>> s = 'Hello'
>>> s.istitle()
True
>>> s = 'Hello world'
>>> s.istitle()
False
>>> s = ''
>>> s.isspace()
False
>>> s = ' '
>>> s.isspace()
True
>>> s = '\t'
>>> s.isspace()
True

"""