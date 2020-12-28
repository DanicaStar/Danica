# -*- coding:utf-8 -*-
# @Time : 2020-12-03 18:58
# @Author: Danica
# @File : mysql_data.py
import MySQLdb
import pytest
conn=MySQLdb.connect(
    user='jkyun',
    passwd='Jkyun.123',
    host='192.168.88.35',
    port=3306,
    db='1_se_db'
)
def get_data():
    query_sql='select * from user_table'
    lst=[]
    try:
        cursor=conn.cursor()
        cursor.execute(query_sql)
        r=cursor.fetchall()
        for data in r:
            data=(data[0],data[1],data[2])
            lst.append(data)
        return lst
    finally:
        cursor.close()
        conn.close()

@pytest.mark.parametrize('id,name,passwd',get_data())
def test(id,name,passwd):
    print(id,name,passwd)


if __name__ == '__main__':
    pytest.main(['-sv', 'mysql_data.py'])
