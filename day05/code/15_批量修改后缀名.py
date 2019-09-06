import os


def add_ad(suffix):
    """

    :param suffix:
    :return:
    """


def modify_suffix(dirname, old_suffix, new_suffix):
    """
    'hello.png'  ----'hello.jpg'
    img .png .jpg
    :param dirname: 操作的目录
    :param old_suffix: 原先的后缀名
    :param new_suffix: 新的后缀名
    :return:
    """
    # 0-1).判断源后缀名是否以点开头， 如果不是，则添加;
    if not old_suffix.startswith('.'):
        old_suffix = '.' + old_suffix
    # 0-2). 判断新的后缀名是否以点开头， 如果不是，则添加;
    if not new_suffix.startswith('.'):
        new_suffix = '.' + new_suffix
    # 1. 判断查找的目录是否存在， 如果不存在， 显示报错
    if not os.path.exists(dirname):
        print("Error: 目录%s不存在" % (dirname))
    # 2. 如果文件存在，做如下操作:
    else:
        # 2-1). 列出指定目录的所有文件名;
        filenames = os.listdir(dirname)
        # 2-2). 依次遍历目录的每一个文件；
        for filename in filenames:
            # 2-3). 如果文件是以old_suffix结尾，则对改文件重命名;
            if filename.endswith(old_suffix):
                # 修改后缀名
                # 2-3-1). 将后缀名和文件名本身分隔开； hello.png === hello .png, 并生成新的文件名
                new_filename = os.path.splitext(filename)[0] + new_suffix
                full_old_filename = os.path.join(dirname, filename)
                full_new_filename = os.path.join(dirname, new_filename)
                # 2-3-2). 重命名
                os.rename(full_old_filename, full_new_filename)
                print("重命名【%s】 为【%s】成功!" % (filename, new_filename))


modify_suffix('img', '.jpg', '.png')
