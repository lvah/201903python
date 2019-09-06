"""
生成验证码: 一般是4位组成， 有字母(大写，小写)，数字
"""
import string
import  random
import  os
def generate_code(length=4):
    """
    默认生成4位验证码: 由两个大写字母，一个小写字母和一个数字组成;
    :param length:
    :return:
    """
    # 从某个序列里面随机获取几个元素；
    # code_li = random.sample(string.ascii_letters + string.digits, length)
    code_li = random.sample(string.ascii_uppercase, 2) + random.sample(string.ascii_lowercase, 1) \
              + random.sample(string.digits, 1)
    # 将生成的验证码顺序打乱;
    random.shuffle(code_li)
    # 将列表拼接成字符串
    return  "".join(code_li)

def create_files():
    dirname = 'img'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print("目录%s创建成功" %(dirname))


    # 循环100次，创建100个文件
    for count in range(100):
        # 随机生成文件名
        filename = generate_code() + '.png'
        full_filename = os.path.join(dirname, filename )
        os.mknod(full_filename)
        print("%s创建成功" %(full_filename))

create_files()