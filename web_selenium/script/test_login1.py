# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:20 上午
# @Author  : danica
# @FileName: test_login1.py
# @Software: PyCharm


import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')

    def test_login01(self):
        print('记住密码登陆')

    def test_login02(self):
        print('不记住密码登陆')


if __name__ == '__main__':
    unittest.main()
