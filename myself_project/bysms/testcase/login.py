# -*- coding:utf-8 -*-
# @Time : 2021-01-21 19:27
# @Author: Danica
# @File : login.py
from selenium import webdriver

url=' http://127.0.0.1/mgr/sign.html'
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)


def login(user,pwd,expect):
    username = driver.find_element_by_id('username')
    passwd = driver.find_element_by_id('password')
    button=driver.find_element_by_class_name('btn')
    username.send_keys(user)
    passwd.send_keys(pwd)
    button.click()
    alert=driver.switch_to.alert
    if expect==alert.text:
        alert.accept()


login('','88888888','请输入用户名')
