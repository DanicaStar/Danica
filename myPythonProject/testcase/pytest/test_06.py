# -*- coding:utf-8 -*-
# @Time : 2020-11-14 16:04
# @Author: Danica
# @File : test_06.py
import pytest
@pytest.fixture()
def init():
    print('init.....')
    # return 1

def test1(init):
    print('test1')

def test2(init):
    print('test2')

if __name__ == '__main__':
    pytest.main(['-sv','test_06.py'])