#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql as pymysql

# 连接数据库
# conn = pymysql.connect('localhost', 'root', '123456')

# 也可以使用关键字参数
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='monoculardata', charset='utf8')

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)

# 也可以使用字典进行连接参数的管理
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'passwd': 'root',
#     'db': 'yu_sq',
#     'charset': 'utf8'
# }
# conn = pymysql.connect(**config)

# 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
#conn.autocommit(1)  # conn.autocommit(True)

# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。

# try:
#     # 创建数据库
#     DB_NAME = 'test'
#     cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
#     cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % DB_NAME)
#     conn.select_db(DB_NAME)
#
#     # 创建表
#     TABLE_NAME = 'user'
#     cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' % TABLE_NAME)
#
#     # 批量插入纪录
#     values = []
#     for i in range(20):
#         values.append((i, 'kk' + str(i)))
#     cursor.executemany('INSERT INTO user values(%s,%s)', values)

    # # 查询数据条目
    # count = cursor.execute('SELECT * FROM users')
    # print('total records:', cursor.rowcount)

#     # 获取表名信息
#     desc = cursor.description
#     print("%s %3s" % (desc[0][0], desc[1][0]))
#
#     cursor.scroll(10, mode='absolute')
#     results = cursor.fetchall()
#     for result in results:
#         print(result)
#
# except:
#     import traceback
#
#     traceback.print_exc()
#     # 发生错误时回滚
#     conn.rollback()
# finally:
#     # 关闭游标连接
#     cursor.close()
#     # 关闭数据库连接
#     conn.close()
