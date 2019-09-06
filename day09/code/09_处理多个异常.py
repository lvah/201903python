# import sys
#
# try:
#     10/0
#     f = open('passwd')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     # sys.exc_info(): 获取异常信息
#     print(sys.exc_info())
#     print("Unexpected error:", sys.exc_info()[0])
#     # # 抛出异常, 本来可以正确执行的代码让报错;
#     # raise




# 为了实现读取文件一定要关闭文件对象;=====一般不这么使用====> 使用的是with语句(安全上下文)
try:
    f = open('testfile', 'w')
    print(f.read())
except IOError as e:
    print("读取文件错误:", e)
else:
    print("运行正确")
finally:
    f.close()
    print("文件操作结束")





try:
    print(a)
    10/0
    print('westos')
# 如果有多个异常处理时, 使用元组; as e其实就是对异常起了个别名, e存储的是错误的详细信息;
except (NameError, ZeroDivisionError) as e:
    print("错误:",  e)


