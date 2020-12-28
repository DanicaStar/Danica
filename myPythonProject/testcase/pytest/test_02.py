# -*- coding:utf-8 -*-
# @Time : 2020-11-14 15:10
# @Author: Danica
# @File : test_02.py
import pytest
class TestLogincase():
    # def __init__(self):      不能使用此方法

    def test01(self):
        print('test01')
        self.add()
        assert 1==1


    def add(self):
        print('add')
        assert 1==1

    def test02(self):
        print('test02')
        assert 1 == 2
if __name__ == '__main__':
    pytest.main(['-vs','test_01.py'])