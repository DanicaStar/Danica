# -*- coding:utf-8 -*-
# @Time : 2021-01-10 14:56
# @Author: Danica
# @File : opmysql.py




import MySQLdb,logging
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
                self.conn=MySQLdb.connect(
                    host=host,
                    user=user,
                    passwd=passwd,
                    db=db,
                    port=port,
                    charset='utf8',
                    cursorclass=MySQLdb.cursors.DictCursor
                )   #创建数据库连接，返回字典
            else:
                self.conn = MySQLdb.connect(
                    host=host,
                    user=user,
                    passwd=passwd,
                    db=db,
                    port=port,
                    charset='utf8'
                ) #创建数据库连接，返回元组
                self.cur=self.conn.cursor()
        except MySQLdb.Error as e:
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
        :return: 字典形式
        '''

        try:
            self.cur.execute(condition)
            self.conn.commit()
            result={'code':'0000','message':'执行通用操作成功','data':[]}
        except MySQLdb.Error as e:
            self.conn.rollback()
            result = {'code': '9999', 'message': '执行通用操作异常', 'data': []}
            print('数据库错误|op_sql %d :%s' % (e.args[0], e.args[1]))
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result


