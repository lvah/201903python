goods = [
    ["苹果", 2, 1000],
    ["电脑", 9999, 300],
    ["手机", 5999, 790]
]

top_price = max(goods,  key=lambda x: x[1])
print(top_price)
print("价格最高的商品名称: ", top_price[0])

low_count = min(goods, key=lambda x: x[2])
print("库存量最少的商品名称: ", low_count[0])

high_count = max(goods, key=lambda x: x[2])
print("库存量最多的商品名称: ", high_count[0])


# 将所有的偶数移动到前面， 将所有的奇数移动到最后
li =list(range(10))
sorted_li = sorted(li, key=lambda  num: 0 if num%2==0 else 1)
print(sorted_li)

