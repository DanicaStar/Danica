# -*- coding:utf-8 -*-
# @Time : 2020-11-14 16:18
# @Author: Danica
# @File : test_07.py
'''
模块级别（setup_module / teardown_module）开始于模块始末，全局的
函数级别（setup_function / teardown_function）只对函数用例生效（不在类中）
类级（setup_class / teardown_class）只在类中前后运行一次（在类中）
方法级（setup_method / teardown_method）开始于方法始末（在类中）
类里面（setup / teardown）运行在调用方法的前后
'''

import pytest
class TestCase01():

    @classmethod
    def setup_class(cls):
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')

def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')

def test_01():
    print('test_01')

def test_02():
    print('test_02')

if __name__ == '__main__':
    pytest.main(['-sv','test_07.py'])
