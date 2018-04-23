#!/usr/bin/python
# -*- coding:utf8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "0", "Test", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)


cursor.execute(sql)

# 关闭数据库连接
db.close()