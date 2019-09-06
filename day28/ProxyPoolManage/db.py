"""
db.py模块处在整个系统的中心位置，与其它的任意模块都有着紧密的联系。
该模块仅定义了一个RedisClient()类，该类定义了对Redis队列进行操作的几个通用方法(add,decrease等 )

"""

import random
import re
import redis
from config import *
from errors import PoolEmptyError
class RedisClient(object):
    """
    存储数据到Redis数据库中
    清空整个 Redis 服务器的数据：flushall
    清空当前库中的所有 key：flushdb
    """

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis密码
        """
        # decode_responses=True:这样写存的数据是字符串格式
        self.db = redis.StrictRedis(host=host,
                                    port=port,
                                    password=password,
                                    decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        # 有序集合的格式: 'set name' value1  score1 value2 score2  value3 score3
        """
        if not re.match('\d+\.\d+\.\d+\.\d+:\d+', proxy):
            print('代理不符合规范', proxy, '丢弃')
            return
        # zscore: 返回有序集 key 中，成员 member 的 score 值。
        if not self.db.zscore(REDIS_KEY, proxy):
            # Redis Zadd 命令用于将一个或多个成员元素及其分数值加入到有序集当中。
            # ZADD KEY_NAME SCORE1 VALUE1.. SCOREN VALUEN
            return self.db.zadd(REDIS_KEY, {proxy: score})

    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果不存在，按照排名获取，否则异常
        :return: 随机代理
        """
        # Zrangebyscore 返回有序集合中指定分数区间的成员列表。有序集成员按分数值递增(从小到大)依次排序排列。
        result = self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
        if len(result):
            return random.choice(result)
        else:
            # ZRANGE: 递增排列
            # ZREVRANGE: 递减排列
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return random.choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理值减一分，小于最小值则删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        # Redis Zscore 命令返回有序集中，成员的分数值。
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            # zincrby 对有序集合中指定成员的分数加上增量 increment, 正数是增加， 负数是减少;
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            # zrem: 用于移除有序集中的一个或多个成员，不存在的成员将被忽略。
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        获取数量
        :return: 数量
        """
        # zard 命令用于计算集合中元素的数量。
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

    def batch(self, count=5, start=0, stop=None):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        if not stop: stop = start + count
        return self.db.zrevrange(REDIS_KEY, start, stop)
