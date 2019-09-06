import numpy as np

data = np.random.random((3, 4))

# 转换数据结构 # 2,6
data = data.reshape((2, 6))

print(data)
print("转置: ", data.T)
print("转置: ", data.transpose())
print("转置: ", data.swapaxes(1, 0))