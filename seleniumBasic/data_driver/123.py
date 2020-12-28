# -*- coding:utf-8 -*-
# @Time : 2020-11-30 20:37
# @Author: Danica
# @File : 123.py

import MySQLdb
import pytest
comm=MySQLdb.connect(
    user= 'jkyun',
    passwd = 'Jkyun.123',
    db= '1_se_db',
    host = '192.168.88.35',
    port = 3306
    )
def get_data():
    sql_query='select * from user_table'
    my_data = []
    try:
        cursor = comm.cursor()
        cursor.execute(sql_query)
        lst =cursor.fetchall()
        for data in lst:
            data=(data[0],data[1],data[2])
            my_data.append(data)
        return my_data
    finally:
        cursor.close()
        comm.close()

# print(get_data())

@pytest.mark.parametrize('id,name,passwd',get_data())
def test(id,name,passwd):
    print(id,name,passwd)

if __name__ == '__main__':
    pytest.main(['-sv', '123.py'])



