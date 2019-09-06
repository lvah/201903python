import itchat
itchat.auto_login(hotReload=True)
# 1). 根据好友的备注名称进行搜索, 获取该好友的详细信息;返回的是列表, 列表里面嵌套字典;
result = itchat.search_friends(remarkName="陈辉")

# 2). 要给固定好友发送消息， 就是要获取改好友的UserName
username = result[0].get('UserName')
# 3). 给指定的好友发送消息
itchat.send("你是谁?", toUserName=username)
