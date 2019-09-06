# 产品经理
# 1). 方法一: 直接在代码里面修改: 代码过多或者项目太大, 修改内容过多, 不建议;
# 2). 方法二: 利用闭包


"""

import time
time.sleep(1)
start_time = time.time()
start_time
Out[5]: 1559377287.2677357
# 时间的格式: 时间戳(1970年到现在经历的秒数)
end_time = time.time()
end_time - start_time
Out[8]: 79.44625687599182

"""
import time
age = 19
def is_adult(fun):
    def wrapper():
        start_time = time.time()
        if age >= 18:
            fun()
        else:
            print("未成年")
        end_time = time.time()
        print("程序运行时间:%.3f" % (end_time - start_time))

    # 返回的是函数的引用
    return wrapper
@is_adult  # 语法糖====music = is_adult(music)
def music():
    time.sleep(1)
    print("正在听音乐.....")
@is_adult
def videos():
    print("正在看视频.....")


@is_adult
def game():
    print("正在玩游戏.....")


# # music=== is_adult函数的返回值是wrapper函数的引用(函数名)
# music = is_adult(music)
# music()

music()

# 此处省略1000个函数模块;
