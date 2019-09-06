# int
# float
# complex
# bool
# str
# list
# tuple
# set
# dict


class Password(object):
    def __init__(self, url, pwd):
      self.url = url
      self.pwd = pwd
      self.count = 10

    # int(对象名)会自动调用
    def __int__(self):
        return  int(self.count)

    def __float__(self):
        return  float(self.count)

p1 = Password('www.baidu.com', 'westos')
print(int(p1))
print(float(p1))
