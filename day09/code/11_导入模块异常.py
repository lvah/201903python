    # python2:
        # pickle: python实现的模块, 运行慢
        # cPickle: C语言封装的模块, 运行快
    # python3:
        # pickle实质上导入的是cPickle

# 这种方式不管在py2还是py3版本, 导入的都是cPickle, 让运行快一些;
try:
    import  cPickle as pickle
except:
    import  pickle



# # 编写的代码可以跨平台时, 可以这样处理
try:
    import os
    # 该方法在LINUX可以执行, Windows不可以执行
    print(os.uname())
except:
    import  platform
    print(platform.uname())




