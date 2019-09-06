def red():
    print("显示红色的字体.......")

def blue():
    print("显示蓝色的字体.......")



#  __name__是一个特殊的变量， 如果不是作为模块导入执行的话， 返回的是__main__; 否则为模块名
if __name__ == '__main__':
    red()
    blue()
    print(__name__)

