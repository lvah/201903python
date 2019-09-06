# -*- coding: utf-8 -*-

"""
# 1. item.py文件的功能?
item.py主要目标是从非结构化来源（通常是网页）提取结构化数据。Scrapy爬虫可以将提取的数据作为Python语句返回。

# 2. 为什么使用item.py?
虽然方便和熟悉，Python dicts缺乏结构：很容易在字段名称中输入错误或返回不一致的数据，特别是在与许多爬虫的大项目。

# 3. item.py文件的优势?
- 定义公共输出数据格式，Scrapy提供Item类。
- Item对象是用于收集所抓取的数据的简单容器。
- 提供了一个类似字典的 API，具有用于声明其可用字段的方便的语法。

"""
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class DoubanItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     title = scrapy.Field()
#     rating_num = scrapy.Field()


class DouBanMovieItem(scrapy.Item):
    """
    确定要爬取的数据的类型和名称，包含:
        电影名称( title) ;
        电影评分( score) ;
        电影评语( quote) ;
        电影导演( director) ，
        上映日期(release_date)
        评论数(comment_num)
    通过 Field( ) 方法来声明数据字段。
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 电影名称
    score = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 电影评语
    director = scrapy.Field()  # 电影导演
    release_date = scrapy.Field()  # 上映日期
    comment_num = scrapy.Field()  # 评论数
    image_url = scrapy.Field()  # 图片的url地址
    detail_url = scrapy.Field()  # 电影详情页信息;
    image_path = scrapy.Field()  # 下載的封面本地存儲位置
    length = scrapy.Field()   # 电影时长
