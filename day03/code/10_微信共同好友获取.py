# 导入微信模块
import itchat

#  1). 登录A用户的微信, 获取好友信息
# 微信登录
itchat.auto_login()
# 获取好友信息, 好友信息是一个列表;
friends1 = itchat.get_friends()

# 拿出好友信息的UserName
contactList1 = set()
# 依次遍历所有的好友信息, 将每个好友的昵称添加到集合contactList1中.
for friend in friends1[1:]:
    contactList1.add(friend['NickName'] + friend['Signature'])

# 登出微信号
itchat.logout()

#  2). 登录B用户的微信, 获取好友信息
# 微信登录
itchat.auto_login()
# 获取好友信息
friends2 = itchat.get_friends()

# 拿出好友信息的UserName
contactList2 = set()
# 依次遍历所有的好友信息, 将每个好友的昵称添加到集合contactList2中.
for friend in friends2[1:]:
    contactList2.add(friend['NickName'] + friend['Signature'])
# 登出微信号
itchat.logout()

#  3). 求两个用户好友信息之间的交集, 共同好友统计
commonFriendsCount = len(contactList1 & contactList2)
print(commonFriendsCount)
