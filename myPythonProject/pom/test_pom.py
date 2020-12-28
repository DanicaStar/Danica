# -*- coding:utf-8 -*-
# @Time : 2020-11-26 20:15
# @Author: Danica
# @File : test_pom.py

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BaiduPage():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.input_element=(By.ID,'kw')
        self.btn_element=(By.ID,'su')

    def goto_baidu(self,url):
        self.driver.get(url)

    def test(self,url,text):
        self.driver.get(url)
        self.driver.find_element(*self.input_element).send_keys(text)
        self.driver.find_element(*self.btn_element).click()
        sleep(5)
        #松耦合



class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.baiduPage=BaiduPage()

    def test_search(self):
        self.baiduPage.test('http://www.baidu.com','小丸子')

if __name__ == '__main__':
    unittest.main()