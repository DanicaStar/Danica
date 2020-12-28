# -*- coding:utf-8 -*-
# @Time : 2020-11-14 15:17
# @Author: Danica
# @File : test_04.py
import pytest
class TestLogincase():
    @pytest.mark.do
    def test01(self):
        print('test01')
        assert 1==1

    @pytest.mark.undo
    def test02(self):
        print('test02')
        assert 1 == 2

if __name__ == '__main__':
    pytest.main(['-vs','test_01.py'])