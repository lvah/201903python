from scipy.interpolate  import lagrange
x = [3, 6, 9]
y = [10, 8, 4]
lagrange(x,y)
#poly1d([ -0.11111111,   0.33333333,10. ])
# 如果U7>:*? (tyyyyyyyyyyyy(要进行插值操作,可以:

print(lagrange(x, y)(10))
# 2.222222