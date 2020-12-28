# -*- coding:utf-8 -*-
# @Time : 2020-11-30 19:57
# @Author: Danica
# @File : data_driver1.py
import unittest
from selenium import webdriver
from time import sleep
from ddt import data,ddt

@ddt()
class case01(unittest.TestCase):
    def setUP(self):
       print ('测试用例开始了')

    @data('小丸子', '哆啦A梦', '卡布奇诺')
    def test1(self,data):
        url = 'https://www.baidu.com'
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.find_element_by_id('kw').send_keys(data)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @data(('username1','pwd1'),('username2','pwd2'),('username3','pwd3'))
    def test_02(self,data):
        url=''
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.find_element_by_id('user').send_keys(data[0])
        self.driver.find_element_by_id('pwd').send_keys(data[1])


    def tearDown(self):
        self.driver.quit()
        print('测试用例结束了')

if __name__ == '__main__':
    unittest.main()



