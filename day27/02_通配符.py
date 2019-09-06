"""
通配符介绍:
    *: 0个或者任意个字符;
    ?: 代表单个字符
    [0-9]: 代表数字
    [a-z]: 小写字母
    [A-Z]: 大写字母
    [a-zA-Z] 字母
    [0-9a-zA-Z]: 字母或者数字


    [[:lower:]]
    [[:upper:]]
"""
import os
# 寻找/etc目录下以.conf结尾的文件
results1 = [filename for filename in os.listdir('/etc') if filename.endswith('.conf')]

import glob
results2 = glob.glob('/etc/*.conf')
print(results2)

# 寻找/etc/目录中以.conf结尾的并且文件名中包含大写字母的文件;
results3 = glob.glob('/etc/*[A-Z]*.conf', recursive=True)
print(results3)