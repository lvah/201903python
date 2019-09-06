"""
先来看一道题:
	如果 a+b+c=1000，且 a2+b2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?


a: 0~1000
b: 0~1000-a
c: 1000-a-b
"""
import time
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001 - a):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
end_time = time.time()
print('run: %.6f' %(end_time-start_time))