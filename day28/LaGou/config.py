"""
配置文件的内容
"""
from fake_useragent import UserAgent

Host = 'www.lagou.com'
Origin = 'https://www.lagou.com'
Referer = 'https://www.lagou.com/jobs/list_python'
Connection = 'keep-alive'
Accept = 'application/json, text/javascript, */*; q=0.01'
ua = UserAgent(verify_ssl=False)
ThreadCount = 50
pages = 5
csvFileName = 'lagou.csv'
keyword = 'java'