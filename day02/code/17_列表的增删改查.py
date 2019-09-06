services = ['vsftpd', 'httpd', 'sshd', 'firewalld']

# **********************添加元素***********************
# 添加mysql到列表最后中, 追加元素
# services.append('mysql')
# print(services)

# # extend拉伸, 追加多个元素到列表中;
# services.extend(['mysql', 'network'])
# print(services)

# # insert: 添加元素到指定位置;
# services.insert(0, 'mysql')
# print(services)



# **************************删除元素**************************
# # clear： 晴空列表里面的所有元素;
# services.clear()
# print(services)


# # pop：弹出， 默认删除最后一个元素; 当然可以通过传值指定要删除的元素;
# services.pop()
# print(services)
# # 删除第一个元素, 索引是0；
# services.pop(0)
# print(services)

# # remove根据元素值进行删除;
# services.remove('httpd')
# print(services)



# ******************修改元素（索引和切片）****************************
# 根据索引修改
# print(services[0])
# services[0] = 'vsftp'
# print("正在修改......")
# print(services)

# 根据切片修改
# print(services)
# services[:2] = ['http', 'https']
# print("正在修改......")
# print(services)


# *********************查看***********************
# 1). 索引
# 2). 切片
# 3). 出现次数
# 4). 索引值
#
# print(services.count('vsftpd'))
# print(services.index('vsftpd'))


# ************** 其他操作**********************
copyServices = services.copy()
print(id(services))
print(id(copyServices))

services.sort()
print(services)


numbers = [1,2,23,1,2,34,56,1,23]
numbers.sort()
print(numbers)

