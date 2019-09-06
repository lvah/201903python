"""


>>> filename = 'hello.py'
>>> filename.endswith('.py')
True
>>> url = 'http://www.westos.org'
>>> url.startswith('http')
True

>>> import os
>>> os.system('date')
Sun May 12 13:45:05 CST 2019

>>> filenames = os.listdir('/home/kiosk/pythonCode')
>>> for filename in filenames:
...     if filename.endswith('.py'):
...             print(filename)
...
base_user_login.py
collect_info.py
fahren2celsius.py
is_adult.py
try_count.py
is_adult_if.py
linux_cmd_prompt.py
odd_sum.py
num_fact.py
user_login.py
hello.py



"""