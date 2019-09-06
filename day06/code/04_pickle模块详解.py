"""
json :
    序列化(编码): python对象编码成json字符串
    反序列化(解码): 将json字符串转成python对象
pickle:
    序列化(编码): python对象编码成pickle的bytes类型数据
    反序列化(解码): 将pickle的bytes类型数据转成python对象

"""
import  json
import  pickle

nums = range(1, 10)
print(type(nums))
# json不能成功的序列化
# json_nums = json.dumps(nums)
# print(json_nums)
pickle_nums = pickle.dumps(nums)
print(pickle_nums)
print("序列化:", type(pickle_nums))

unpickle_nums = pickle.loads(pickle_nums)
print(unpickle_nums)
print("反序列化:", type(unpickle_nums))


import  time
now_time = time.localtime()
print(now_time)
print(type(now_time))