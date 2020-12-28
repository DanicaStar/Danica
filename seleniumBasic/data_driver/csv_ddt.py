# -*- coding:utf-8 -*-
# @Time : 2020-12-03 17:31
# @Author: Danica
# @File : csv_ddt.py
import csv
import pytest
def get_data():
    with open('csv_data.csv', 'r') as file:
        lst=csv.reader(file)
        my_data=[]
        for data in lst:
            my_data.append(data)
        return my_data

@pytest.mark.parametrize('name',get_data())
def test(name):
    print(name)

if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'csv_ddt.py'])












