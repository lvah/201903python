""""



"""
import time
import gc
# 关闭python自动实现的垃圾回收机制;
gc.disable()

while True:	
	time.sleep(0.0003)
	# 申请两个内存空间， 变量list1和变量list2分别指向不同的内存空间, 引用计数全为1；
	list1 = []
	list2 = []
	
	# 在容器list1里面存储了list2， list2的引用计数加1；
	list1.append(list2)
	# 在容器list2里面存储了list1， list1的引用计数加1；
	list2.append(list1)
	
	
	# 删除list1和list2
	del list1
	del list2



