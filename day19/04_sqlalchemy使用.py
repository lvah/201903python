from sqlalchemy import create_engine, Column, Integer, SmallInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ModuleNotFoundError: No module named 'MySQLdb'
# python2: MySQLdb
# python3: pymysql

engine = create_engine("mysql+pymysql://root:westos@172.25.254.123/pymysql",
                       encoding='utf8',
                        # echo=True
                       )
# 创建缓存对象
Session = sessionmaker(bind=engine)
session = Session()

# 声明基类
Base = declarative_base()

class Person(Base):
    __tablename__ =  'persons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), unique=True)

    def __repr__(self):
        return  self.name

if __name__ == '__main__':
    # 创建数据表
    Base.metadata.create_all(engine)


    # # 添加单条数据
    # p = Person(id=1, name="粉条", email='fentiao@westos.org')
    # # 先将数据写入缓存;
    # session.add(p)
    # # 将缓存中的数据提交到数据库并执行
    # session.commit()

    #
    # #  添加多条数据
    # p1 = Person(name='A')
    # p2 = Person(name='B')
    # # 先将数据写入缓存;
    # session.add_all((p1, p2))
    # # 将缓存中的数据提交到数据库并执行
    # session.commit()

    # 查找数据
    # select * from students where ()

    # results = session.query(Person).all()  # 查找表的所有数据
    # print(results)

    # results = session.query(Person).first()  # 查找表的第一条数据
    # print(results)

    # obj = session.query(Person).filter_by(name='粉条').first()
    # print("邮箱地址:", obj.email)


    # # 删除数据，没有first/all方法， 默认返回的是要执行的sql语句;
    # obj = session.query(Person).filter_by(name='B').first()
    # print(obj)
    # # session.delete(obj)
    # # session.commit()


    # 更新数据: 更新姓名为B的邮箱为hello@qq.com
    obj = session.query(Person).filter_by(name='B').first()
    obj.email = 'hello.qq.com'
    session.add(obj)
    session.commit()


    # SQL
    # 对象  ------   SQL  -----MYSQL
    # 读取数据信息: mysql -----SQL ------对象

