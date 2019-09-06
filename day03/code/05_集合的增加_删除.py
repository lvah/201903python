allow_users = {'user1', 'user2', 'user3', 'user1'}

# *******************************增加***************************
# # 添加一个元素到集合里面;
# allow_users.add('user4')
# print(allow_users)

# # update添加多个元素到集合中;
# allow_users.update({'user4', 'user5', 'user6'})
# print(allow_users)


# ****************************删除********************************
# # remove删除指定的元素, 如果元素不存在， 则报错
# allow_users.remove('user1')
# print(allow_users)
#
# # remove删除指定的元素,  如果元素不存在， 则什么也不做
# allow_users.discard('user1')
# print(allow_users)

# # pop随机删除集合元素
# delete_user = allow_users.pop()
# print(allow_users)
# print("随机删除的元素:", delete_user)

# # clear： 清空集合元素
# allow_users.clear()
# print(allow_users)

# 如果要对集合排序， 需要先转成列表;
nums = {2, 3, 1, 2, 3, 5, 7, 8, 3, 22, 2}
nums = list(nums)
# 默认从小到大进行排序， reverse=True由大到小进行排序;
nums.sort(reverse=True)
print(nums)
