import pandas as pd
import numpy as np
import string

# &**********series中的where方法运行结果和numpy中完全不同;
s1 = pd.Series(np.arange(5), index=list(string.ascii_lowercase[:5]))
# print(s1.where(s1 > 3))

# 对象中不大于3的元素赋值为10；
print(s1.where(s1 > 3, 10))

# 对象中大于3的元素赋值为10；
print(s1.mask(s1 > 3, 10))
