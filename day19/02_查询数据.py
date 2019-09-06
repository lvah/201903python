import pymysql

# 1. 与mysql建立连接 mysql -h host/ip  -u root -p westos
conn = pymysql.connect(host='172.25.254.123', user='root', password='westos', db='pymysql')
# 2. 创建游标
cursor = conn.cursor()

# # 3. 查询数据
# select_sqli = 'select * from student'
# affectedRows = cursor.execute(select_sqli)
# print(affectedRows)
#
#
# # 3-1. 获取查询的数据
# print(cursor.fetchone())
# # 将游标移动到记录的最开始位置
# cursor.scroll(0, mode='absolute')
# print(cursor.fetchmany(2))
# # 将游标移动到当前记录的下一个记录的位置;
# cursor.scroll(1)
# print(cursor.fetchall())



# 3. 查询数据: 如果没有查询到返回0；
select_sqli = 'select * from student where name="A"'
affectedRows = cursor.execute(select_sqli)
print(affectedRows)
# 4. 关闭游标
cursor.close()
# 5.关闭连接
conn.close()
