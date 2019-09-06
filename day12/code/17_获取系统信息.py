# 获取系统信息的模块
import psutil
import  time


# m每隔一秒绘制CPU的占有率;  如何持久化保存? 如何将时间和对应的cpu占有率匹配;
while True:
    # 获取当前时间和cpu占有率
    t  = time.localtime()
    cur_time = '%d:%d:%d' %(t.tm_hour, t.tm_min, t.tm_sec)
    cpu_res = psutil.cpu_percent()
    # print(cpu_res)


    # 保存到文件中;
    with open('cpu.txt', 'a+') as f:
        f.write('%s %s\n' %(cur_time, cpu_res))
    time.sleep(1)