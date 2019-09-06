# 创建爬虫项目

```
scrapy  startproject DouBan

```


# 项目结构

```

DouBan/
├── DouBan
│   ├── __init__.py
│   ├── items.py            # 设置的是数据库存储的模版
│   ├── middlewares.py      # 中间件信息
│   ├── pipelines.py        # 数据存储的模块
│   ├── __pycache__
│   ├── settings.py 
│   └── spiders             # 爬虫目录核心
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg

```


- settings.py

```python
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DouBan (+http://www.yourdomain.com)'
# 设置随机的用户代理;
from fake_useragent import  UserAgent
ua = UserAgent()
USER_AGENT = ua.random

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False
```


cd DouBan/
scrapy  genspider douban 'douban.com'