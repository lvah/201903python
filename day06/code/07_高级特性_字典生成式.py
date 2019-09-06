"""

  大小写计数合并 : 已知字典{'A':10, 'b':5, 'a':2}, 合并后为{'a':12, 'b':5}
      key值最终全部为小写.
"""

d= {
    'A':10,
    'a':40,
    'b':10,
    'c':2,
    'C':5
}

# 合并字典; d.get(key.lower(), 0)， 如果key'值不存在，默认返回0;
dict_result = {key.lower():d.get(key.lower(), 0) + d.get(key.upper(), 0)for key, value in d.items()}
print(dict_result)