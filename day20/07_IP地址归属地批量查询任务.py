import requests
import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from threading import Thread


def task(ip):
    """获取指定IP的所在城市和国家并存储到数据库中"""
    # 获取网址的返回内容
    url = 'http://ip-api.com/json/%s' % (ip)
    try:
        response = requests.get(url)
    except Exception as e:
        print("网页获取错误:", e)
    else:
        # 默认返回的是字符串
        """
        {"as":"AS174 Cogent Communications","city":"Beijing","country":"China","countryCode":"CN","isp":"China Unicom Shandong Province network","lat":39.9042,"lon":116.407,"org":"NanJing XinFeng Information Technologies, Inc.","query":"114.114.114.114","region":"BJ","regionName":"Beijing","status":"success","timezone":"Asia/Shanghai","zip":""}
        """
        contentPage = response.text
        # 将页面的json字符串转换成便于处理的字典;
        data_dict = json.loads(contentPage)
        # 获取对应的城市和国家
        city = data_dict.get('city', 'null')  # None
        country = data_dict.get('country', 'null')

        print(ip, city, country)
        # 存储到数据库表中ips
        ipObj = IP(ip=ip, city=city, country=country)
        session.add(ipObj)
        session.commit()


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:westos@172.25.254.123/pymysql",
                           encoding='utf8',
                           # echo=True
                           )
    # 创建缓存对象
    Session = sessionmaker(bind=engine)
    session = Session()

    # 声明基类
    Base = declarative_base()


    class IP(Base):
        __tablename__ = 'ips'
        id = Column(Integer, primary_key=True, autoincrement=True)
        ip = Column(String(20), nullable=False)
        city = Column(String(30))
        country = Column(String(30))

        def __repr__(self):
            return self.ip


    # 创建数据表
    Base.metadata.create_all(engine)

    # 1.1.1.1 -- 1.1.1.10
    threads = []
    for item in range(10):
        ip = '1.1.1.' + str(item + 1)  # 1.1.1.1 -1.1.1.10
        # task(ip)
        # 多线程执行任务
        thread = Thread(target=task, args=(ip,))
        # 启动线程并执行任务
        thread.start()
        # 存储创建的所有线程对象;
        threads.append(thread)

    [thread.join() for thread in threads]
    print("任务执行结束.........")
    print(session.query(IP).all())
