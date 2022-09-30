# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 9:37 上午
# @Author  : danica
# @FileName: main.py
# @Software: PyCharm


# -*- coding:utf-8 -*-
# @Time : 2021-01-10 14:56
# @Author: Danica
# @File : opmysql.py




import pymysql,logging
from seleniumBasic.data_driver.mysql import config
class OperationDbInterface():
    def __init__(self,host='192.168.88.35',user='jkyun',passwd='Jkyun.123',db='1_se_db',port=3306, link_type=0):
        '''

        :param host: 数据库服务器主机
        :param user: 数据库用户名
        :param passwd: 数据库密码
        :param db: 数据库名称
        :param port: 端口号，整数类型
        :param link_type: 连接类型，用于设置输出数据是元组还是字典，默认字典 link_type=0
        :return 游标
        '''

        try:
            if link_type==0:
                self.conn=pymysql.connect(
                    host=host,
                    user=user,
                    passwd=passwd,
                    db=db,
                    port=port,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor
                )   #创建数据库连接，返回字典
            else:
                self.conn = pymysql.connect(
                    host=host,
                    user=user,
                    passwd=passwd,
                    db=db,
                    port=port,
                    charset='utf8'
                ) #创建数据库连接，返回元组
            self.cur=self.conn.cursor()
        except pymysql.Error as e:
            print('创建数据库连接失败|MySQL Error %d :%s'%(e.args[0],e.args[1]))
            logging.basicConfig(
                filename=config.src_path+'/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger=logging.getLogger(__name__)
            logger.exception(e)

    def op_sql(self,condition):
        '''
        :param condition: SQL语句
        :return: SQL语句
        '''

        try:
            self.cur.execute(condition)
            self.conn.commit()
            results=[]
            datas=self.cur.fetchall()
            for data in datas:
                results.append(data)
            print(results)
            result={'code':'0000','message':'执行通用操作成功','data':results}
        except pymysql.Error as e:
            self.conn.rollback()

            result = {'code': '9999', 'message': '执行通用操作异常', 'data':[]}
            print('数据库错误|op_sql %d :%s' % (e.args[0], e.args[1]))
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result

    def select_one(self,condition):
        try:
            rows_affect=self.cur.execute(condition)
            if rows_affect>0:
                mysql_data=[]
                datas=self.cur.fetchall()
                for result in datas:
                    mysql_data.append(result)
                result={'code':'0000','message':'执行单条查询操作成功','data':mysql_data}
            else:
                result = {'code': '0000', 'message': '执行单条查询操作成功', 'data': []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message': '执行单条查询异常', 'data':[]}
            print('数据库错误|select_one %d:%s'%(e.args[0],e.args[1]))
            logging.basicConfig(
                filename=config.src_path+'/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger=logging.getLogger(__name__)
            logger.exception(e)
        return result
    def select_all(self,condition):
        try:
            rows_affect=self.cur.execute(condition)
            if rows_affect>0:
                self.cur.scroll(0,mode='absolute')    #将鼠标光标放到初始位置
                mysql_data=[]
                datas=self.cur.fetchall()
                for data in datas:
                    mysql_data.append(data)
                result={'code':'0000','message':'执行多条查询操作成功','data':mysql_data}
            else:
                result = {'code': '0000', 'message': '执行多条查询操作成功', 'data': []}
        except pymysql.Error as e:
            self.conn.rollback()
            result={'code': '9999', 'message': '执行多条查询异常', 'data': []}
            print('数据库错误|select_all %d %s '%(e.args[0],e.args[1]))
            logging.basicConfig(
                filename=config.src_path+'/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d]%(levelname)s %(message)s'
            )
            logger=logging.getLogger(__name__)
            logger.exception(e)
        return result

    def insert_data(self,condition,params):
        '''
        :param condtion:  inser语句
        :param params: insert数据
        :return: 字典形式批量插入数据结果
        '''
        try:
            results=self.cur.executemany(condition,params)
            self.conn.commit()
            result={'code':'0000','message':'执行插入数据操作成功','data':results}
        except pymysql.Error as e:
            self.conn.rollback()
            result={'code':'9999','message':'执行插入数据操作异常','data':[]}
            print('数据库错误|insert_data %d %s'%(e.args[0],e.args[1]))
            logging.basicConfig(
                filename=config.src_path+'/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger=logging.getLogger(__name__)
            logger.exception(e)
        return result

    def __del__(self):
        if self.cur !=None:
            self.cur.close()
        if self.conn !=None:
            self.conn.close()

if __name__ == '__main__':
    mysql=OperationDbInterface()
    # print(mysql.select_one('select * from user_table'))
    # print(mysql.select_all('select * from user_table'))
    # print(mysql.op_sql('update user_table set pwd="hahaha" where username="danica"'))
    # print(mysql.op_sql('select * from user_table'))
    print(mysql.insert_data('insert into user_table(id,username,pwd)values(%s,%s,%s)',[(41,'张三1','zhangsan1'),(51,'王五1','wangwu1'),(61,'李四1','lisi1')]))


