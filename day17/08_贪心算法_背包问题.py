# datas中每个元素代表一个古董，每个列表第一个元素代表古董重量，第二个元素代表古董价值
datas = [[4, 3], [2, 8], [9, 18], [5, 6], [5, 8], [8, 20], [5, 5], [4, 6], [5, 7], [5, 15]]
m = 30 # 毛驴运载能力
w = 0 # 获取的总价值
# 计算出每件宝物的性价比，按照从高到低排序
for i in range(len(datas)):
	price = datas[i][1] / datas[i][0]
	datas[i].append(price)  # 增加性价比
datas.sort(key=lambda data: data[2], reverse=True) # 按性价比排序
# 按性价比从大到小选取宝物，直到达到毛驴的运载能力
for data in datas:
	if data[0] <= m:
		w += data[1]
		m -= data[0]
	else:
		w += data[2] * m  # 取走宝物的一部分
		break
print('总价值：',w)
