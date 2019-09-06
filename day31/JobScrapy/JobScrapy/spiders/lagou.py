# -*- coding: utf-8 -*-
import itertools
import requests
import urllib
from urllib.parse import quote

import scrapy

from JobScrapy import settings


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    # 得到城市名
    citynames = settings.CITY_NAME
    # 职业类型
    job_names = settings.JOB_NAME
    # 返回元素的笛卡尔积的元组。
    # eg. itertools.product([1,2,3],[100,200])  =====> [(1, 100), (1, 200), (2, 100), (2, 200), (3, 100), (3, 200)]
    url_params = [param for param in itertools.product(citynames, job_names)]
    origin_url = 'https://www.lagou.com/jobs/list_'  # eg: https://www.lagou.com/jobs/list_职位名
    url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&city=%s&needAddtionalResult=false'

    allowed_domains = ['lagou.com']
    start_urls = [url]

    def start_requests(self):
        '''从self.parms开始组合url并且生成request对象'''
        print("正在执行......")
        for url_param in self.url_params:
            """
            url_param[0]: 城市名称
            url_param[1]: 职位名称
            
            """
            # 将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。
            url = self.url % quote(url_param[0])
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Encoding': 'gzip, deflate',
            }
            # print(self.origin_url + url_param[1])
            # session = requests.Session()
            # # 用session对象发出get请求,设置cookies
            # response = session.get(self.origin_url + url_param[1], headers=headers, timeout=3)  # 请求首页获取cookies
            #
            # cookies = session.cookies  # 为此次获取的cookies
            #
            cookies = "user_trace_token=20190814095612-10bc22bf-c0da-4928-9f33-96074d0c06b2; LGUID=20190814095614-b2b58738-be36-11e9-a500-5254005c3644; _gat=1; PRE_UTM=m_cf_cpc_360_pc; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fcommunal.html%3Futm_source%3Dm_cf_cpc_360_pc%26m_kw%3D360_cpc_zz_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; JSESSIONID=ABAAABAAAFCAAEGCB9A0BF4807067DDD19AA15F06C24DF6; WEBTJ-ID=08212019%2C134608-16cb2b601818a-0d6bbb566d5be1-38710e57-1879680-16cb2b60182485; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=0804fbc081627f095436636651e183bdcbc2c7a060; _gid=GA1.2.1922026474.1566366369; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565574293,1565747805,1566366314; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566366379; _ga=GA1.2.1070077883.1565747804; LGSID=20190821134429-be8384a4-c3d6-11e9-8b14-525400f775ce; LGRID=20190821134546-ebebf479-c3d6-11e9-8b14-525400f775ce; SEARCH_ID=a90ac642554f483a9f52345c5b7a1bf1"
            # print("cookies: ", cookies)
            headers['cookies'] = cookies
            yield scrapy.FormRequest(url=url,
                                     formdata={'pn': '1', 'kd': url_param[1]},
                                     method='POST',
                                     # cookies=cookies,
                                     headers=headers,
                                     meta={'page': 1, 'kd': url_param[1]},
                                     dont_filter=True)

    def parse(self, response):
        print(len(response.text))
