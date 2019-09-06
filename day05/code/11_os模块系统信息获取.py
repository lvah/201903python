import os

# 1). 返回操作系统类型， 值为posix，是Linux操作系统, 值为nt， 是windows操作系统
print(os.name)
os_name = 'Linux' if os.name =='posix' else 'Windows'
print("当前操作系统: %s" %(os_name))

# 2). 操作系统的详细信息
detail_info = os.uname()
print(detail_info)
print("主机名:", detail_info.nodename)
print("硬件架构:", detail_info.machine)
print("系统名称:", detail_info.sysname)
print("Linux内核的版本号:", detail_info.release)

# 3). 系统环境变量等价于Linux的env命令
print(os.environ)

# 4). 通过key值获取环境变量对应的value值
print(os.environ['PATH'])

