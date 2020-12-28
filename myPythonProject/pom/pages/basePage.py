# -*- coding:utf-8 -*-
# @Time : 2020-12-08 19:42
# @Author: Danica
# @File : basePage.py
from selenium import webdriver
class BasePage():
    def __init__(self,url):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def get_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,text,*loc):
        self.get_element(*loc).send_keys(text)

    def click_element(self,*loc):
        self.get_element(*loc).click()

    def get_title(self):
        print(self.driver.title)

    def clear(self,*loc):
        self.get_element(*loc).clear()
