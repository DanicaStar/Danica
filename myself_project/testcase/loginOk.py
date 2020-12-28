# -*- coding:utf-8 -*-
# @Time : 2020-12-22 19:09
# @Author: Danica
# @File : loginOk.py
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestLogin():
    def userlogin(self):
        self.driver=webdriver.Chrome()
        url='http://localhost:8080/jpress/user/login'
        self.driver.maximize_window()
        self.driver.get(url)
        user=self.driver.find_element_by_name('user')
        user.clear()
        user.send_keys('admin')
        passwd=self.driver.find_element_by_name('pwd')
        passwd.clear()
        passwd.send_keys('123456')
        button=self.driver.find_element_by_class_name('btn')
        button.click()
        return self.driver
# test=TestLogin()
# test.userlogin()