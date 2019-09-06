"""
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
现在改用协程(yield)，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高。
"""
import random
import  time
def Consumer(name):
    """消费者"""
    goods = ["电视", "手机", '电脑']
    # buy_name = input("请输入购买物品:")
    buy_name = random.choice(goods)
    print("[%s]需要购买%s" %(name, buy_name))
    while True:
        # 将yield后面的buy_name发送给生产者, 生产者获取生产的信息
        game  = yield buy_name
        print("[%s]购买%s成功" %(name, game))

def Produder(name):
    """生产者"""
    # []生成一个列表， 列表里面是10个生成器(Consumer)
    # ()生成一个生成器， 列表里面是10个生成器(Consumer)
    consumers = (Consumer("消费者%s" %(i+1)) for i in range(10))
    for consumer in consumers:
        # next方法的返回值就是Consumer里面yield后面跟的值;
        buy_name = next(consumer)
        print("工程师[%s]正在生产%s" %(name, buy_name))
        time.sleep(1)
        print("工程师[%s]生产%s成功" % (name, buy_name))
        # 爬虫中返回的内容是的内容;
        # 将生产好的数据发送给消费者
        consumer.send(buy_name)
def main():
    Produder("高梦飞")
main()


