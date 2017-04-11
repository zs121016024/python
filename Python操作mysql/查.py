#!/usr/bin/env python
# coding:utf-8




import pymysql   #导入pymysql模块

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='demo', port=3306)  ###创建链接

cur = conn.cursor()   ###获取游标
"""
######INSERT / UPDATE / DELETE 操作步骤和以下步骤一样
cur.execute('''INSERT INTO `users`(`name`, `age`) VALUE ('zhangsong', 20)''')   #执行sql


conn.commit()       #提交事务
cur.close()         #关闭游标对象



    非查询请求的四个步骤：
        1、创建连接
        2、获取游标
        3、执行sql
        4、提交事务
        游标对象在close之前，可以反复使用
"""


###select语句，可通过以下几种方式获取到数据

#1.fetchall() 方法，返回行的元组，所有都数据都返回
cur.execute('''SELECT * FROM `users` WHERE `age` <= 20''')   #执行select sql
data = cur.fetchall()
print(data)

#2.fetchmany(num)方法，返回行的元组，可以指定返回前N行，相当于fetchall[:N]
cur.execute('''SELECT * FROM `users` WHERE `age` <= 20''')   #执行select sql
data = cur.fetchmany(2)
print(data)

#3.fetchone()方法，返回首行元组，相当于fetchall[0]
cur.execute('''SELECT * FROM `users` WHERE `age` <= 20''')   #执行select sql
data = cur.fetchone()
print(data)


###每行数据也是一个元组，元组内容由sql决定
cur.execute('''SELECT `name`, `age` FROM `users` WHERE `age` >= 30''')   #执行sql
data = cur.fetchall()
print(data)


###注意： fetchall, fetchmany, fetchone 的差异是在客户端决定的， 无论执行那个， 数据都会全部发送到客户端， 如果要限制返回数据的行数，
###       应该在sql里限制， 而不是通过fetch方法
cur.execute('''DESC users''')
data = cur.fetchall()
print(data)



#######如何让返回数据带列名（返回字典）

from pymysql.cursors import DictCursor

cur = conn.cursor(cursor=DictCursor)
cur.execute('SELECT * FROM `users`')
data = cur.fetchall()
print(data)





