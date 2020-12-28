# -*- coding:utf-8 -*-
# @Time : 2020-12-12 14:12
# @Author: Danica
# @File : 4_element_prop.py
from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.driver.maximize_window()   #浏览器窗口最大化
        # self.driver.set_window_size('weight','height')   #浏览器窗口设置大小

    def test_element_prop(self):   #属性
        e=self.driver.find_element_by_id('t1')
        print(e.id)      #id
        print(e.tag_name)  #标签名
        print(e.size)    #size
        print(e.rect)    #坐标
        print(e.text)    #文本

        print(e.current_url)  # 获取当前页面地址
        print(e.title)  # 获取页面表头
        self.driver.quit()

    def test_element_method(self):   #方法
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')
        sleep(2)

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))   #获取元素value属性值
        print(e.is_displayed())  # 判断button是否可见
        print(e.is_enabled())  # 判断是否可用


        e.clear()
        self.driver.quit()

if __name__ == '__main__':
            case = TestCase()
            # case.prop()
            case.test_element_method()