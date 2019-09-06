"""

生产者消费者模型当中有两大类重要的角色，一个是生产者（负责造数据的任务），另一个是消费者（接收造出来的数据进行进一步的操作）。

1. 为什么要使用生产者消费者模型？

     在并发编程中，如果生产者处理速度很快，而消费者处理速度比较慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个等待的问题，就引入了生产者与消费者模型。让它们之间可以不停的生产和消费。

2. 实现生产者消费者模型三要素：

    1、生产者

    2、消费者

    3、队列（或其他的容哭器，但队列不用考虑锁的问题）

3. 什么时候用这个模型？

程序中出现明显的两类任务，一类任务是负责生产，另外一类任务是负责处理生产的数据的（如爬虫）


4. 用该模型的好处？

1、实现了生产者与消费者的解耦和

2、平衡了生产力与消费力，就是生产者一直不停的生产，消费者可以不停的消费，因为二者不再是直接沟通的，而是跟队列沟通的。


"""

import  time
import  random
# 缓冲区列表， 存放生产的所有内容， 工作方式是先进先出(FIFO-first in first out)
"""
先进: list.append(element)
先出: element = list.pop(0)
"""
cacheList = []
# # 设置缓冲区的最大长度, 当缓冲区到达最大长度， 那么生产者就不能再生产了
cacheListLen = 5

def is_full():
    """
    判断缓冲区队列是否已经满了
    :return:
    """
    return  len(cacheList) == cacheListLen

def Producer(name):
    """
    生产者, 主要用于生产数据
    :return:
    """
    while True:
        if not is_full():
            print("生产者[%s]正在生产任天堂游戏机....." %(name))
            # 模拟生产者生产数据需要的时间, 随机休眠0～1秒,
            time.sleep(random.random())
            print("[%s] 已经生产任天堂游戏机完成" %(name))
            # 将生产的游戏机放入缓冲区
            cacheList.append('任天堂游戏机')
        else:
            print("生产足够多了.....")
            yield


def Consumer(name):
    """
    消费者， 用于处理/消费数据
    :return:
    """
    print("【%s】正在准备购买游戏机" %(name))
    while True:
        item = yield
        print("【%s】正在准备购买游戏机成功" %(name))


# producer是一个生成器
producer = Producer("高梦飞")
next(producer)

# 列表生成式, 生成消费者
consumers = [Consumer("消费者%s" %(i+1)) for i in range(10)]

# 依次遍历所有的消费者， 给提供游戏机
for consumer in consumers:
    if not cacheList:
        print("目前商店没有游戏机库存.....")
    else:
        #
        if not is_full():
            next(producer)
        else:
            item = cacheList.pop(0)
            next(consumer)
            consumer.send(item)


