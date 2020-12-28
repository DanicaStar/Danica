# -*- coding:utf-8 -*-
# @Time : 2020-11-26 20:08
# @Author: Danica
# @File : test_non_pom.py

from selenium import webdriver
import unittest
import time
class TeatBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()


    def test_baidu(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

