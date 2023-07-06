# -*- coding: utf-8 -*-            
# @Time : 2023/7/5 17:52
# @name : 黄谷芬
# @FileName: mysql.py
# @Software: PyCharm
import time

import pymysql

class Sql(object):

    @classmethod
    def conn_mysql(self):
        hostname = '175.178.52.106'  # 本机ip地址
        username = 'root'
        password = 'Wanxun123&*('
        dab = 'jiumao_backup2'  # 数据库名称
        charset = "utf8"
        conn = pymysql.connect(host=hostname, user=username, password=password, db=dab, charset=charset)
        return conn

    @classmethod
    def sql_update(self, conn, sql):
        """修改语句"""
        # conn = self.conn_mysql()
        cursor = conn.cursor()
    # sql = "update yabei_member set real_name=NULL , id_card=NULL, is_real_name=2, cert_begin_date=NULL, cert_end_date=NULL where user_name='15892037169'"
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
    # 5.获取结果
    # data1 = cursor.fetchone() # 一条数据
    # # cursor.execute("update yabei_member set real_ ")
    # print(f"查询一条数据的结果为{data1}") # 查询一条数据
    # 6.关闭，释放资源
    @classmethod
    def sql_quit(self, conn):
        """关闭数据库连接"""
        cursor = conn.cursor()
        cursor.close() # 游标关闭
        conn.close() # 连接关闭

    @classmethod
    def sql_select(self, conn, sql):
        """查询语句"""
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        return data