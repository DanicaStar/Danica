# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:20 上午
# @Author  : danica
# @FileName: test_register.py
# @Software: PyCharm

import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')

    def test_register01(self):
        print('全部填写注册')

    def test_register02(self):
        print('部分填写注册')


if __name__ == '__main__':
    unittest.main()
