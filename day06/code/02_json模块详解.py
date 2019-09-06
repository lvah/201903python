"""
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。

JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯(包括C、C++、Java、JavaScript、Perl、Python等)。

这些特性使JSON成为理想的数据交换语言。易于人阅读和编写，同时也易于机器解析和生成(一般用于提升网络传输速率)。


"""
import  json
# 1). 创建python对象
users = {}
for item in range(100):
    users['user%s' %(item)] = '密码'


# 2). 将python对象编码为json对象
# """
# indent=4 -----缩进为4
# ensure_ascii=False---如果显示中文需要设置
# separators=None  -- 修改默认分隔符
#         ``separators`` should be an ``(item_separator, key_separator)``
#         tuple.  The default is ``(', ', ': ')``
#
# sort_keys  -----        对字典的key值进行排序
# """
# import  json
# json_users = json.dumps(users, indent=4, ensure_ascii=False, separators=('*', '-'), sort_keys=True)
# print(json_users)
# print(type(json_users))



# # 3). 将python对象编码为json格式的字符串， 并保存到指定文件中;
# with open('doc/users.json', 'w') as f:
#     json.dump(users, f, indent=4, ensure_ascii=False)



# 4).  loads
# with open('doc/users.json') as f:
#     content = f.read()
# user_obj = json.loads(content)
# print(user_obj)
# print(type(user_obj))



# 5). load
with open('doc/users.json') as f:
    user_obj = json.load(f)
print(user_obj)
print(type(user_obj))
