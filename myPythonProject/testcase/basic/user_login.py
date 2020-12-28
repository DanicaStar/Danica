# -*- coding:utf-8 -*-
# @Time : 2020-10-27 20:23
# @Author: Danica
# @File : login.py

from time import sleep
from selenium import  webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUserLogin(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

        #测试登录，用户名错误
    def test_user_login_username_error(self):
        username=''
        pwd='123456'
        expected='账号不能为空'

        #输入用户名
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        #点击登录按钮
        self.driver.find_element_by_class_name('btn').click()

        #等待提示框
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        sleep(3)

        #python的断言
        assert alert.text==expected
        alert.accept()    #点击弹框
        sleep(3)

    #测试用户登录成功
    def test_user_login__ok(self):
        username='admin'
        pwd='123456'
        expected='用户中心'

        #输入用户名
        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        #点击登录按钮
        self.driver.find_element_by_class_name('btn').click()

        #等待提示框
        WebDriverWait(self.driver,5).until(EC.title_is(expected))
        sleep(3)

        #python的断言
        assert self.driver.title==expected
        sleep(3)
        self.driver.quit()

test=TestUserLogin()
# test.test_user_login__ok()
test.test_user_login_username_error()