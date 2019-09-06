"""
测试代理IP是否可用？
"""

# -*- coding: utf-8 -*-

import telnetlib

print('------------------------connect---------------------------')

ip = '123.139.56.238'
try:
    tn = telnetlib.Telnet(ip, port='9999', timeout=10)
except Exception as e:
    print(e)
    print('error')

else:
    print('ok')

print('-------------------------end----------------------------')
