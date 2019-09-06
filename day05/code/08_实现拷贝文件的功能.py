
import  os
def copy(source_file, dst_file):
    """
    实现拷贝文件的操作
    思路:
        cp /etc/passwd /etc/hello
        1. 判断拷贝的文件是否存在?
        2. 如果存在， 将源文件的内容读出来， 写入目标文件
    """
    if os.path.exists(source_file):
        # 将源文件的内容读出来
        f = open(source_file)
        content = f.read()
        f.close()
        # 写入目标文件
        dst_f = open(dst_file, 'w')
        dst_f.write(content)
        dst_f.close()
        print("拷贝%s为%s成功" %(source_file, dst_file))
    else:
        print("源文件%s不存在" %(source_file))
copy('/etc/passwd', 'doc/passwd-备份')