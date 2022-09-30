# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 11:31 上午
# @Author  : danica
# @FileName: get_sql.py
# @Software: PyCharm


import pymysql
import logging
import os


# 定义连接对象  类方法
class ReadDB:
    src_path = os.path.dirname(os.path.abspath(__file__))
    conn = None

    def __init__(self, host='127.0.0.1', user='root', password='123456', db='test', port=3306, charset='utf8'):

        """
        :param host: 数据库服务器主机
        :param user: 数据库用户名
        :param passwd: 数据库密码
        :param db: 数据库名称
        :param port: 端口号，整数类型
        :param link_type: 连接类型，用于设置输出数据是元组还是字典，默认字典 link_type=0
        :return 游标
        """

        try:
            if self.conn == None:
                self.conn = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    db=db,
                    port=port,
                    charset=charset,
                )  # 创建数据库连接，返回元组
                # 获取游标对象方法
                self.cursor = self.conn.cursor()
        except pymysql.Error as e:
            print('创建数据库连接失败|MySQL Error %d :%s' % (e.args[0], e.args[1]))
            logging.basicConfig(
                filename=self.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(e)

    # 关闭游标对象方法
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭连接对象方法
    def close_conn(self):
        if self.conn:
            self.conn.close()
            # 注意：关闭连接对象后，对象还存在内存中，需要手动设置为None
            self.conn = None

    # 查询数据库
    def search_sql(self, sql):
        """
        :param sql: SQL 查询语句
        :return: 返回查询的数据
        """
        try:
            # 执行方法
            self.cursor.execute(sql)
            results = []
            # 获取执行结果
            datas = self.cursor.fetchall()  # 读取所有数据，但是所有数据放在一个元组
            for data in datas:
                results.append(data)
            # print(results)
            result = {'code': '0000', 'message': '执行通用操作成功', 'data': results}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message': '执行通用操作异常', 'data': []}
            print('数据库错误|op_sql %d :%s' % (e.args[0], e.args[1]))
            logging.basicConfig(
                filename=self.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(e)
        # 返回执行结果
        return result

    # 新增、修改、删除
    def execute_sql(self, sql):
        """
        :param sql:  新增/修改/删除的sql语句
        :return: 执行操作的结果
        """
        try:
            # 执行方法
            self.cursor.execute(sql)
            # 提交事务
            self.conn.commit()
            result = {'code': '0000', 'message': '执行数据操作成功'}
        except Exception as e:
            # 回滚事务
            self.conn.rollback()
            result = {'code': '9999', 'message': '执行插入数据操作异常'}
            print('数据库错误|insert_data %d %s' % (e.args[0], e.args[1]))
            logging.basicConfig(
                filename=self.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result

    def __del__(self):
        # 关闭有标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接
        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    sql1 = 'SELECT * FROM test.user;'
    sql2 = "update test.user set username='王wu2' where id=1 "
    sql3 = "delete from test.user where id=1 "
    sql4 = "INSERT INTO test.user values(2, '王五',  '1022-09-29', 2, '上海')"
    test = ReadDB()
    print(test.execute_sql(sql2))
    print(test.search_sql(sql1))
