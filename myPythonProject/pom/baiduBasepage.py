# -*- coding:utf-8 -*-
# @Time : 2020-12-10 19:50
# @Author: Danica
# @File : baiduBasepage.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class BaiduBasePage(object):
    def __init__(self,url):
        self.driver=webdriver.Chrome()
        self.driver.get(url)

    def get_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,text,*loc):
        self.get_element(*loc).send_keys(text)

    def click_element(self,*loc):
        self.get_element(*loc).click()

    def get_title(self):
        print(self.driver.title)


class BaiduBase(BaiduBasePage):
    def baiduTest(self):
        loc1=(By.ID,'kw')
        loc2 = (By.ID, 'su')
        text='小丸子'
        self.input_text(text,*loc1)
        self.click_element(*loc2)
        self.get_title()
        sleep(3)
if __name__ == '__main__':
    url = 'https://www.baidu.com'
    baidu=BaiduBase(url)
    baidu.baiduTest()
