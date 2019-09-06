"""
编写一个函数来验证输入的字符串是否是有效的 IPv4 ?
    1). IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。
	比如，172.16.253.1；
    2). IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的， 127.0.0.1是合法的。
"""

# 172.25.254.250
# 1). 用户输入Input: strip去除字符串开头和结尾的空格(广义的空格, \n,\t,空格)
IP = input("IPV4：").strip()

# 2). 分割IP
# ['172', '258', '254', '250']
splitIp = IP.split('.')
# 3). 判断IP是否由四部分组成
if len(splitIp) != 4:
    print("Not IPV4")
else:
    # 4). for循环依次遍历每一个元素是否合法;
    for item in splitIp:  # item='172'; item='25'.....
        # 将字符串的‘172’转换成整形的172，进行比较;
        # 如果没有在0～255只见， 直接跳出循环;
        # IPv4 地址内的数不会以 0 开头: len(item)!=1 and item.startswith('0')
        # 5). 条件判断: 范围是否在0~255之间， 是否以0开头;
        if (not 0 <= int(item) <= 255) or (len(item)!=1 and item.startswith('0')):
            print('Not IPv4')
            break
    else:
        print('IPV4')


