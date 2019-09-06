class Student(object):
    # 函数的默认值必须是不可变数据类型
    def __init__(self, name, scores=(100, 60)):
        self.name = name
        self.scores = list(scores)

    # 索引的时候, 是对成绩进行索引/切片的;
    def __getitem__(self, index):
        # print(index)
        # 如果是查看索引, 传递的index是索引值;
        # 如果是切片, index是slice对象;
        return  self.scores[index]

    # 对指定索引index修改值; s[0] = 89 ====> index=0, value=89
    def __setitem__(self, index, value):
        self.scores[index] = value

    def __delitem__(self, index):
        del self.scores[index]

    # 设置该类创建的对象是可迭代对象(生成器 ---> 迭代器 ---> 可迭代对象)
    # 生成器都是迭代器; 迭代器都是可迭代对象; 可迭代对象不一定是迭代器; eg:str, list.
    # iter(): j将可迭代对象转换程迭代器;
    def __iter__(self):
        return  iter(self.scores) # 迭代器
        # return  iter([1, 2, 3, 4, 5])



s = Student('westos')
for item in s:
    print(item)



# print(s[0])
# print(s[1])
# print(s[1:])
# print(s[:-1])



# print(s[:2])

# print("before:", s[0])
# s[0] = 89
# print("after:", s[0])
#
#
# print('delete before:', s.scores)
# del s[-1]
# print('delete after:', s.scores)



