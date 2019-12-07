#coding=utf-8
import pymysql

class MysqlHelper:
    def __init__(self,host='localhost',port=3306,db='monoculardata',user='root',passwd='123456',charset='utf8'):
        self.conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)

    def insert(self,sql,params):
        return self.__cud(sql,params)

    def update(self,sql,params):
        return self.__cud(sql,params)

    def delete(self,sql,params):
        return self.__cud(sql,params)

    def __cud(self,sql,params=[]):
        try:
            #用来获得python执行Mysql命令的方法,也就是我们所说的操作游标
            #cursor 方法将我们引入另外一个主题：游标对象。通过游标扫行SQL 查询并检查结果。
            #游标连接支持更多的方法，而且可能在程序中更好用。
            cs1 = self.conn.cursor()
            #真正执行MySQL语句
            rows=cs1.execute(sql, params)
            self.conn.commit()
            #完成插入并且做出某些更改后确保已经进行了提交，这样才可以将这些修改真正地保存到文件中。
            cs1.close()
            self.conn.close()
            return rows #影响到了哪行
        except Exception as e:
            print (e)
            self.conn.rollback()

    def fetchone(self, sql, params=[] ):
        #一次只返回一行查询到的数据
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql , params)
            row = cs1.fetchone()
            #把查询的结果集中的下一行保存为序列
            #print(row)
            #row是查询的值
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print("None", e)

    def fetchall(self,sql,params):
        #接收全部的返回结果行
        #返回查询到的全部结果值
        try:
            cs1=self.conn.cursor()
            cs1.execute(sql,params)
            rows=cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print("None",e)