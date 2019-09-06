import pprint
import time
import  pandas as pd
import requests
from config import *
from concurrent.futures import ThreadPoolExecutor
import  logging


# 灵活配置日志级别,日志格式,输出位置
logging.basicConfig(level=logging.DEBUG,  # 日志类型为DEBUG或者比DEBUG级别更高的类型保存在日志文件中;
                   format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename='lagou.log',
                   filemode='w')


def getPositionIDPage(url_start, url_parse, page=1, kd='python'):
    """

 获取PositionId列表所在页面, 返回的时json数据;
   :param url_start:   图形界面拉勾网职位信息的url地址;为了获取随机的session;
   :param url_parse: 真实返回json格式的url地址
   :param page: 访问的页数
   :param kd: 搜索的关键字
   :return: json数据格式的文本信息;
   """
    # 构造请求头(headers)
    headers = {'User-Agent': ua.random,
               'Host': Host,
               'Origin': Origin,
               'Referer': Referer,
               'Connection': Connection,
               'Accept': Accept

               }

    # 构造表单
    data = {
        'first': False,
        'pn': str(page),
        'kd': kd

    }

    try:
        # requests库的session对象能够帮我们跨请求保持某些参数,
        # 也会在同一个session实例发出的所有请求之间保持cookies。
        # 创建一个session对象
        session = requests.Session()
        # 用session对象发出get请求,设置cookies
        session.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
        cookie = session.cookies  # 为此次获取的cookies
        # 用session对象发出另外一个post请求,获取cookies , 返回响应信息
        response = session.post(url=url_parse,
                                headers=headers,
                                data=data,

                                )
        time.sleep(1)
        # 响应状态码为4xx客户端错误,或者5xx服务器错误响应,来抛出异常:
        response.raise_for_status()
        response.encoding = response.apparent_encoding
    except Exception as e:
        logging.error("页面" + url_parse + "爬取失败:", e)
    else:
        logging.info("页面" + url_parse + "爬取成功" + str(response.status_code))
        return response.json()


def analyse_PositionID(html):
   """
  根据获取的页面解析每一个招聘页面详情都有一个所属的ID索引
  :param html:
  :return:
  """
   # tag = 'positionId'
   positions = html['content']['positionResult']['result']
   df = pd.DataFrame(positions)
   return df




def task(page):
    # 拉勾网页面
    url_start = 'https://www.lagou.com/jobs/list_%s' %(keyword)
    # 真实的拉勾网url地址
    url_parse = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult = false'
    # 获取指定页拉勾网的职位信息, 返回的是json反序列化的结果
    html = getPositionIDPage(url_start, url_parse, page=page, kd=keyword)
    # pprint.pprint(content)
    # 解析页面, 返回DataFrame格式的数据;
    df = analyse_PositionID(html)
    return df
if __name__ == '__main__':
    with ThreadPoolExecutor(ThreadCount) as pool:
        results = pool.map(task, range(1, pages+1))
    total_df = pd.concat(results, axis=0)
    total_df.to_csv(csvFileName, index=False,sep=',', header=True )