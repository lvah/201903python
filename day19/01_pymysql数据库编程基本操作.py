import pymysql

# 1. 与mysql建立连接 mysql -h host/ip  -u root -p westos
conn = pymysql.connect(host='172.25.254.123', user='root', password='westos', db='pymysql')
# 2. 创建游标
cursor = conn.cursor()

# 3. sql操作
# # 3-1). 创建数据库表的操作
# create_sqli = 'create table student(id int, name varchar(20), age int, score float);'
# # 执行sql语句
# cursor.execute(create_sqli)


# # 3-2). 执行添加记录的操作
# insert_sqli = 'insert into student(name, score) values("小E", 78);'
# # 执行sql语句
# cursor.execute(insert_sqli)
# # 提交sql操作
# conn.commit()


# # # 3-3). 执行批量添加记录的操作
# import random
#
# insert_sqli = 'insert into student(name, score) values("%s", "%s");'
# for i in range(10):
#     name = "学生" + str(i + 1)
#     score = random.randint(50, 100)
#     sql = insert_sqli % (name, score)
#     print(sql)
#     cursor.execute(sql)
# # 提交sql操作
# conn.commit()


insert_sqli = 'insert into student(name, score) values(%s, %s);'
cursor.executemany(insert_sqli, [('A', 100), ('D', 90), ('E', 99)])
# 提交sql操作
conn.commit()


# 4. 关闭游标
cursor.close()
# 5.关闭连接
conn.close()
