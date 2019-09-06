"""
if实现switch语句
"""
# grade = input("请输入等级:")
# if grade == 'A':
#     print("优秀")
# elif grade == 'B':
#     print("良好")
# elif grade == 'C':
#     print("及格")
# else:
#     print("无效的成绩")


"""
通过字典实现switch语句
"""
gradeDic = {'A': "优秀", 'B': "良好", 'C': "及格"}
grade = input("请输入等级:")  # A B

# 方法一: 根据key值获取value值: gradeDic[grade]
#       如果key值存在， 返回value值;
#       如果key值不存在， 报错;

# if grade in gradeDic:
#     print(gradeDic[grade])
# else:
#     print("无效的成绩")



# 方法二: 根据key值获取value值: dic.get(key)
#       如果key值存在， 返回value值;
#       如果key值不存在，返回None或者你指定的默认值;
print(gradeDic.get(grade, "无效的成绩"))