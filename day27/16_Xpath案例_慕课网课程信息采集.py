import re

import requests
# User-Agent随机选择代理模块;
from fake_useragent import  UserAgent
from lxml import etree
import  pandas as pd
# 线程池
from concurrent.futures import  ThreadPoolExecutor

def get_content(url):
    """数据采集"""
    try:
        headers = {
            'User-Agent': ua.random,

        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
    except Exception as e:
        print("网页" + url + "爬取错误:", e)
        return  ''
    else:
        # response.text     : 如果普通的页面， 用text， 返回字符串的内容
        # response.content  : 如果不是普通的页面(图片， 视频), 用content, 返回的时二进制内容;
        return  response.text

def html_parser(html):
    """
    数据解析: 获取页面的课程名称， 课程简介， 学习人数,
    :param html:
    :return:
    """
    # 1. 获取页面上每个课程的详细信息;
    """
    <div class="course-card-container">详细的课程信息对应的html.......</div>
    """
    html = etree.HTML(html)
    courseDetails =html.xpath('//div[@class="course-card-container"]')
    # print(courseDetails)

    # 2. 遍历所有的课程， 依次提取每个课程的标题， 学习人数， 详细信息
    for courseDetail in courseDetails:
        # 2-1. 标题
        """
        <h3 class="course-card-name">初识HTML+CSS</h3>
        """
        # 默认返回的时列表, e.g: ['初识HTML+CSS'], 访问它的第0个索引是我们想要的内容;
        title = courseDetail.xpath('.//h3[@class="course-card-name"]/text()')[0]
        # print(title)

        # 2-2. 学习人数
        """
        <div class="course-card-info">
					<span>入门</span><span><i class="imv2-set-sns"></i>1056599</span>
		</div>
        """
        # 默认返回的是列表, 格式如下: ['入门', '1056602']
        studentNum = courseDetail.xpath('.//div[@class="course-card-info"]/span/text()')[-1]
        # print(studentNum)

        # 2-3. 课程的详细信息
        """
        <p class="course-card-desc">HTML+CSS基础教程8小时带领大家步步深入学习标签用法和意义</p>
        """
        courseInfo = courseDetail.xpath('.//p[@class="course-card-desc"]/text()')[0]
        # print(courseInfo)

        # 2-4. 获取详细的url地址
        """
        <a target="_blank" href="/learn/9" class="course-card">
        """
        # print( courseDetail.xpath('./a/@href'))
        course_url = "https://www.imooc.com" + courseDetail.xpath('./a/@href')[0]
        # yield  title, studentNum, courseInfo, course_url


        # 用字典存储
        result = [{
            'title': title,
            'studentNum': studentNum,
            'courseInfo': courseInfo,
            'course_url': course_url
        }]


        df = pd.DataFrame(result)
        yield  df

def save_data(df):
    """
    数据存储
    :return:
    """
    df.to_csv(csv_filename, sep=',', header=True, index=False)
    print("写入文件%s成功...." %(csv_filename))

def task(page):
    """
    多线程执行的任务
    :param page:
    :return:
    """
    url = 'https://www.imooc.com/course/list?page=%s' %(page)
    html = get_content(url)
    df = html_parser(html)
    return  df

if __name__ == '__main__':
    ua = UserAgent()
    threadCount = 5
    pages = 3
    csv_filename = 'doc/mooc.csv'

    with ThreadPoolExecutor(threadCount) as pool:
        # 存储的是任务的返回值
        # results里面有几个元素
        results = pool.map(task, range(1, pages+1))

    # results的个数取决于任务个数， 比如任务数为5， 返回的结果也为5个;
    # result里面包含多个df对象;
    # for result in results:
    #     print(result)


    total_df = pd.DataFrame({})
    for result in results:
        for item in result:
            print(item)
            # # 拼接获取的所有信息, axis=0代表往跨行（down)，而axis=1代表跨列（across)
            total_df = pd.concat([item, total_df], axis=0)
    print(total_df)
    save_data(total_df)