# 导入模块
import itchat

# 1). 微信扫码登录, hotReload=True热加载, 如果扫描一次二维码登录, 之后会有缓存, 执行代码不需要扫码;
itchat.auto_login(hotReload=True)

# 2). 实现微信信息的获取
# 获取的好友信息(列表存储), 第一个是你自己的信息;
friends = itchat.get_friends()

#
# print(type(friends))
# # 获取自己的信息
# print(friends[0]['NickName'])


# 3). 统计男女个数
male = female = other = 0
# 好友是指除了自己之外的其他用户; [1:]
for friend in friends[1:]:
    # 获取性别
    sex = friend['Sex']
    # 1-男
    if sex == 1:
        # male = male + 1
        male +=  1
    elif sex == 2:
        female += 1
    else:
        other += 1


print("""
            %s的微信好友男女个数统计
    好友总数: %s
    男性: %s 个
    女性: %s 个
    保密: %s 个            
""" %(friends[0]['NickName'], len(friends[1:]), male, female, other))

