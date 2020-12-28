# -*- coding:utf-8 -*-
# @Time : 2020-12-03 18:42
# @Author: Danica
# @File : json_ddt.py
import json
import pytest
def get_data():
    with open('json_data.json','r') as file:
        data=json.load(file)
        my_data=[]
        my_data.extend(data['keys'])
        return my_data

@pytest.mark.parametrize('name',get_data())
def test(name):
    print(name)

if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'json_ddt.py'])
