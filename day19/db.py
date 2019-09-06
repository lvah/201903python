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


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(30), unique=True)

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    # 创建数据表
    Base.metadata.create_all(engine)


    # 创建初始化数据
    u1 = User(name='user1', password='123')
    u2 = User(name='user2', password='123')
    session.add_all([u1, u2])
    session.commit()
    print("初始化数据成功........")





