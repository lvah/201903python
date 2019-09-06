# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request

from DouBan.items import DouBanMovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'  # 爬虫名称， 随便起， 但是不能重复;
    allowed_domains = ['douban.com', 'doubanio.com']  # 允许爬去的网站;
    # start_urls = ['http://douban.com/'] # 种子URL， 最开始要爬去的url地址， 通过引擎传递给调度器。
    start_urls = [
        'https://movie.douban.com/top250'
    ]
    url = 'https://movie.douban.com/top250'

    def parse(self, response):
        item = DouBanMovieItem()
        # <ol class="grid_view">
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            # 电影名称( title): <span class="title">肖申克的救赎</span>
            # extract()将对象转换成字符串
            item['title'] = movie.xpath(
                './/span[@class="title"]/text()'
            ).extract()[0]

            # 电影评分( score): <span class="rating_num" property="v:average">9.7</span>
            item['score'] = movie.xpath(
                './/span[@class="rating_num"]/text()'
            ).extract()[0]

            # 电影评语( quote): 有的电影没有短评， 存储空字符串即可;
            quote = movie.xpath(
                './/span[@class="inq"]/text()'
            ).extract()
            item['quote'] = quote[0] if quote else ''

            # 电影导演( director)
            """
            info:
                ['导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano\xa0\xa0\xa0主...', '2011\xa0/\xa0剧, '', '\n                            ']
            """
            info = movie.xpath(
                './/div[@class="bd"]/p/text()'
            ).extract()

            director = info[0].split('主演')[0].strip()
            item['director'] = director

            # 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1454261925.jpg'
            item['image_url'] = movie.xpath('.//div[@class="pic"]/a/img/@src').extract()[0]
            # print("image url: ", item['image_url'])


            item['detail_url'] = movie.xpath('.//div[@class="hd"]//a/@href').extract()[0]
            # print("detail url: ", item['detail_url'])
            # 上映日期(release_date):
            yield item

        """
        <span class="next">
        <link rel="next" href="?start=50&amp;filter=">
        <a href="?start=50&amp;filter=">后页&gt;</a>
        </span>
        """
        # nextLink = response.xpath('.//span[@class="next"]/link/@href').extract()  # 返回的是列表
        # if nextLink:
        #     nextLink = nextLink[0]
        #     print('Next Link: ', nextLink)
        #     yield Request(self.url + nextLink, callback=self.parse)
        #
        #
