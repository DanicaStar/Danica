# -*- coding:utf-8 -*-
# @Time : 2020-12-12 14:11
# @Author: Danica
# @File : 3_webdriver_prop.py
from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        # 2、打开谷歌浏览器
        driver = webdriver.Chrome()
        # 3、窗口最大化
        driver.maximize_window()
        # 4、输入网址：百度、京东、淘宝
        driver.get('http://www.baidu.com')
        driver.get('http://www.jd.com')
        driver.get('http://www.taobao.com')
        sleep(3)

    def prop(self):   #属性
        print(self.driver.mame)   #浏览器名称
        print(self.driver.current_url)   #当前的url
        print(self.driver.title)
        print(self.driver.window_handles)   #当前句柄
        print(self.driver.page_source)   #页面源码
        #self.driver.qiut()

    def method(self):  # 方法
        self.driver.back()  # 后退到京东
        sleep(3)
        self.driver.back()  # 后退到百度
        sleep(3)
        self.driver.forward()  # 前进到京东
        sleep(3)
        self.driver.forward()  # 前进到淘宝
        sleep(3)
        self.driver.refresh()  # 页面刷新
        sleep(3)

if __name__ == '__main__':
    case=TestCase()
    # case.prop()
    case.method()