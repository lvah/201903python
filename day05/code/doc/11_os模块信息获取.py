import os

# 1). 返回操作系统类型， 值为posix，是Linux操作系统, 值为nt， 是windows操作系统
print(os.name)
print('Linux' if os.name=='posix' else 'Windows')

# 2). 操作系统的详细信息
info = os.uname()
print(info)
print(info.sysname)
print(info.nodename)

# 3). 系统环境变量
print(os.environ)

# 4). 通过key值获取环境变量对应的value值
print(os.environ.get('PATH'))
print(os.getenv('PATH'))