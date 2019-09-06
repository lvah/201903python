# 定义全局变量
allMoney = 100
operator = []

def save_money(money): # 必选参数
	"""存钱"""
	global allMoney
	print("存钱前:", allMoney, operator)
	allMoney +=  money
	# 为什么operator不需要声明为全局变量?
	operator.append('存钱操作')
	print("存钱后:", allMoney, operator)


def view_money():
	"""查询金额"""
	#allMoney = 500
	operator.append("查询金额操作")
	print("查询金额:", allMoney, operator)


if __name__ == '__main__':
	save_money(50)
	view_money()
