# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item


class AddScoreNum(object):
    """在原有评分的基础上加1"""

    def process_item(self, item, spider):
        if item['score']:
            score = float(item['score'])
            item['score'] = str(score + 1)
            return item
        else:
            raise Exception("没有爬去到score")


class JsonWriterPipeline(object):
    """爬虫之前打开文件对象， 爬虫之后， 关闭文件对象"""

    def open_spider(self, spider):
        self.file = open('douban.json', 'w')

    def process_item(self, item, spider):
        # dict(item): 将item对象转成字典
        # json.dumps: 将字典序列化成json字符串;
        # indent=4: 存储是缩进为4；
        # ensure_ascii=False: 解决中文乱码问题
        line = json.dumps(dict(item), indent=4, ensure_ascii=False)
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class MysqlPipeline(object):
    """编写MySQL存储插件"""

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapyProject',  # 数据库名
            user='root',  # 数据库用户名
            passwd='westos',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True,
            autocommit=True
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        self.cursor.execute("create table if not exists douBanTop("
                            "title varchar(50) unique, "
                            "score float , "
                            "quote varchar(100), "
                            "director varchar(100), "
                            "comment_num int, "
                            "release_date varchar(10));")

    def process_item(self, item, spider):
        insert_sqli = "insert into douBanTop(title, score, quote,director) values ('%s', '%s', '%s', '%s')" % (
            item['title'], item['score'], item['quote'], item['director'],)
        print(insert_sqli)
        try:
            self.cursor.execute(insert_sqli)
            # 提交sql语句
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
        return item  # 必须实现返回

    def close_spider(self, spider):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):  # 單個的item對象;
        """
        自動請求獲取圖片信息並下載;
        :param item:
        :param info:
        :return:
        """
        print("item: ", item)
        yield scrapy.Request(item['image_url'])



    #
    # def item_completed(self, results, item, info):
    #     """
    #     :param results:
    #         [(True,  {'url': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1454261925.jpg',
    #             'path': 'full/e9cc62a6d6a0165314b832b1f31a74ca2487547a.jpg',
    #             'checksum': '5d77f59d4d634b795780b2138c1bf572'})]
    #     :param item:
    #     :param info:
    #     :return:
    #     """
    #     # for result in results:
    #     #     print("result: ", result)
    #     image_paths = [x['path'] for isok, x in results if isok]
    #     # print("image_paths: ", image_paths[0])
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #
    #     item['image_path'] = image_paths[0]
    #     return item
